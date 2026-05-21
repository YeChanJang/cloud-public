import "dotenv/config";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { loadConfig } from "./config.js";
import { assertReadonlyTool } from "./guardrails.js";
import { audit } from "./audit.js";
import { KeycloakClientApi } from "./keycloak-client.js";
import { ListRealmsArgs, listRealms } from "./tools/list-realms.js";
import { ListClientsArgs, listClients } from "./tools/list-clients.js";
import { CheckRedirectUrisArgs, checkRedirectUris } from "./tools/check-redirect-uris.js";
import { ListUsersArgs, listUsers } from "./tools/list-users.js";
import { CheckAdminRolesArgs, checkAdminRoles } from "./tools/check-admin-roles.js";

const config = loadConfig();
const keycloak = new KeycloakClientApi(config);

const server = new McpServer({
  name: "keycloak-mcp-readonly-server",
  version: "0.1.0",
});

function jsonResult(value: unknown) {
  return {
    content: [
      {
        type: "text" as const,
        text: JSON.stringify(value, null, 2),
      },
    ],
  };
}

async function runReadonlyTool<T>(tool: string, realm: string | undefined, handler: () => Promise<T>) {
  assertReadonlyTool(tool);
  audit({ tool, realm, status: "start" });
  try {
    const result = await handler();
    audit({ tool, realm, status: "success" });
    return jsonResult(result);
  } catch (error) {
    audit({
      tool,
      realm,
      status: "error",
      message: error instanceof Error ? error.message : "unknown error",
    });
    throw error;
  }
}

server.tool("list_realms", "List Keycloak realms visible to the service account", ListRealmsArgs.shape, async () => {
  return runReadonlyTool("list_realms", undefined, () => listRealms(keycloak));
});

server.tool("list_clients", "List clients in a Keycloak realm with limited metadata", ListClientsArgs.shape, async (args) => {
  return runReadonlyTool("list_clients", args.realm, () => listClients(keycloak, args));
});

server.tool("check_redirect_uris", "Find potentially risky redirect URI patterns", CheckRedirectUrisArgs.shape, async (args) => {
  return runReadonlyTool("check_redirect_uris", args.realm, () => checkRedirectUris(keycloak, args));
});

server.tool("list_users", "List limited user metadata. Emails are masked.", ListUsersArgs.shape, async (args) => {
  return runReadonlyTool("list_users", args.realm, () => listUsers(keycloak, args));
});

server.tool("check_admin_roles", "List realm roles that appear admin-like and require review", CheckAdminRolesArgs.shape, async (args) => {
  return runReadonlyTool("check_admin_roles", args.realm, () => checkAdminRoles(keycloak, args));
});

const transport = new StdioServerTransport();
await server.connect(transport);
