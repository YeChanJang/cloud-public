# Keycloak MCP Readonly Server

Readonly MCP server sample for inspecting Keycloak configuration with an AI Agent.

> This repository is a **sample project for a blog series**. It is not an official Keycloak or MCP project and is not production-ready as-is. The default design is intentionally readonly.

---

## Related articles

- [Part 1: Keycloak MCP concept and readonly server design](https://tistory-cloud.tistory.com/entry/Keycloak-MCP%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-AI-Agent%EB%A1%9C-%EC%9D%B8%EC%A6%9D-%EC%84%A4%EC%A0%95%EC%9D%84-%EC%A0%90%EA%B2%80%ED%95%98%EB%8A%94-%EC%9D%BD%EA%B8%B0-%EC%A0%84%EC%9A%A9-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0)
- [Part 2: Building Keycloak MCP tools with TypeScript](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-Realm-Client-User-%EC%A1%B0%ED%9A%8C-Tool%EC%9D%84-TypeScript%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0)
- [Part 3: Keycloak MCP security operation guide](https://tistory-cloud.tistory.com/entry/Keycloak-MCP-%EB%B3%B4%EC%95%88-%EC%9A%B4%EC%98%81-%EA%B0%80%EC%9D%B4%EB%93%9C-AI-Agent%EC%97%90%EA%B2%8C-%EC%9D%B8%EC%A6%9D-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%84-%EC%96%B4%EB%94%94%EA%B9%8C%EC%A7%80-%EB%B3%B4%EC%97%AC%EC%A4%84-%EA%B2%83%EC%9D%B8%EA%B0%80)

---

## What this example shows

- Wrap Keycloak Admin API as narrowly scoped MCP tools
- Expose readonly inspection tools to an AI Agent
- Check realms, clients, redirect URIs, limited users, and admin-like roles
- Keep dangerous write operations out of the MCP server
- Document security guardrails before connecting to production Keycloak

---

## What this example does not do

- It does not create, update, or delete Keycloak resources.
- It does not return client secrets.
- It does not reset user passwords.
- It does not provide production-grade authentication, authorization, auditing, or network controls.
- It does not replace human review for authentication system changes.

---

## Architecture

```text
AI Client / MCP Host
  |
  | MCP stdio tool call
  v
Keycloak MCP Readonly Server
  |
  | OAuth2 Client Credentials
  v
Keycloak Admin API
```

The MCP server is the safety boundary. Do not expose the Keycloak Admin API directly to an AI Agent.

---

## SDK version note

This sample targets the MCP TypeScript SDK v1 package:

```text
@modelcontextprotocol/sdk
```

The upstream TypeScript SDK repository also documents newer split packages on its main branch. If you migrate this sample to a newer SDK generation, re-check imports and tool registration APIs against the official MCP TypeScript SDK documentation.

---

## Folder structure

```text
src/                 MCP server and Keycloak client code
src/tools/           readonly MCP tool implementations
docs/                architecture, tool design, security model, operation checklist
examples/            MCP client config and sample prompts
scripts/             repository validation script
.env.example         local environment variable template
```

---

## Readonly tools

| Tool | Purpose | Notes |
|---|---|---|
| `list_realms` | List realms visible to the service account | Use only with limited service accounts |
| `list_clients` | List clients in a realm | Does not return client secrets |
| `check_redirect_uris` | Find risky redirect URI patterns | Flags wildcard and localhost patterns |
| `list_users` | List limited user metadata | Masks email values |
| `check_admin_roles` | List admin-like realm roles | Does not inspect all assignments yet |

---

## Prerequisites

- Node.js 20 or later
- A Keycloak test realm
- A dedicated Keycloak confidential client for this MCP server
- Client Credentials enabled for that client
- Minimal realm-management roles for readonly inspection

Do not start with a production realm. Test against a development realm first.

---

## Quick start

```bash
npm install
cp .env.example .env
npm run build
npm start
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
npm install
npm run build
npm start
```

Edit `.env` before running.

---

## Environment variables

```env
KEYCLOAK_BASE_URL=https://keycloak.example.com
KEYCLOAK_ADMIN_REALM=master
KEYCLOAK_TARGET_REALM=sample
KEYCLOAK_CLIENT_ID=mcp-readonly
KEYCLOAK_CLIENT_SECRET=replace-me
KEYCLOAK_ALLOW_WRITE_TOOLS=false
```

| Variable | Description |
|---|---|
| `KEYCLOAK_BASE_URL` | Base URL of your Keycloak server |
| `KEYCLOAK_ADMIN_REALM` | Realm used to issue the service account token |
| `KEYCLOAK_TARGET_REALM` | Default realm inspected by tools |
| `KEYCLOAK_CLIENT_ID` | Confidential client ID used by the MCP server |
| `KEYCLOAK_CLIENT_SECRET` | Client secret. Never commit a real value. |
| `KEYCLOAK_ALLOW_WRITE_TOOLS` | Must remain `false` in this sample |

---

## MCP client configuration

See:

```text
examples/claude-desktop-config.json
```

Replace the placeholder path and environment values before using it.

---

## Validation

Run static repository checks:

```bash
npm run validate
```

The validation script checks:

- required files exist
- JSON files parse correctly
- obvious secrets are not committed
- forbidden write-capable tool names are not registered

Build check:

```bash
npm run typecheck
npm run build
```

---

## Security posture

This project is intentionally readonly.

Recommended guardrails:

- Use a dedicated Keycloak service account.
- Grant only the minimum realm-management roles required for inspection.
- Do not expose this MCP server directly to the public internet.
- Do not connect production realms until development realm testing is complete.
- Log tool calls, target realm, and caller context.
- Mask user identifiers when possible.

Read more:

- `docs/security-model.md`
- `docs/operation-checklist.md`
- `docs/keycloak-permissions.md`

---

## Blog section mapping

| Blog post | Files |
|---|---|
| Part 1: Concept and architecture | `docs/architecture.md`, `docs/tool-design.md` |
| Part 2: Implementation | `src/`, `examples/claude-desktop-config.json`, `examples/prompts.md` |
| Part 3: Security operation guide | `docs/security-model.md`, `docs/operation-checklist.md`, `src/guardrails.ts` |

---

## References

- [Model Context Protocol TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Model Context Protocol documentation](https://modelcontextprotocol.io/)
- [Keycloak Server Administration Guide](https://www.keycloak.org/docs/latest/server_admin/)
- [Keycloak Admin REST API](https://www.keycloak.org/docs-api/latest/rest-api/)

---

## License

MIT License. See `LICENSE`.
