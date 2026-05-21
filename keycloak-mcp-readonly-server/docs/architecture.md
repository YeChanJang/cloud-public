# Architecture

```text
AI Client / MCP Host
  |
  | MCP stdio tool call
  v
Keycloak MCP Readonly Server
  |
  | OAuth2 Client Credentials token
  v
Keycloak Admin API
```

The MCP server acts as a narrow readonly boundary between an AI Agent and Keycloak Admin API.

## Why this boundary matters

An AI Agent should not receive a generic Keycloak admin token or a generic HTTP tool. It should receive only named inspection tools with small input schemas and limited outputs.

## Design principles

1. Start readonly.
2. Expose specific inspection tools instead of a generic HTTP proxy.
3. Return limited fields.
4. Mask user data where possible.
5. Block write operations by design.
6. Log tool calls before using this pattern in production.
7. Keep stdout reserved for MCP protocol messages and write operational logs to stderr.
