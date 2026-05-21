import { z } from "zod";
import type { KeycloakClientApi } from "../keycloak-client.js";

export const ListClientsArgs = z.object({
  realm: z.string().optional(),
});

export async function listClients(api: KeycloakClientApi, args: z.infer<typeof ListClientsArgs>) {
  const clients = await api.listClients(args.realm);
  return clients.map((client) => ({
    clientId: client.clientId,
    enabled: client.enabled ?? true,
    publicClient: client.publicClient ?? false,
    protocol: client.protocol,
    redirectUriCount: client.redirectUris?.length ?? 0,
    webOriginCount: client.webOrigins?.length ?? 0,
  }));
}
