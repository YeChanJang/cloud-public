# Operation checklist

## Before connecting to production

- [ ] Tested against a development realm
- [ ] Dedicated service account created
- [ ] Minimum required Keycloak roles assigned
- [ ] No write tools registered
- [ ] Client secrets are not returned by any tool
- [ ] User fields are limited and masked
- [ ] MCP server is not publicly exposed
- [ ] Tool calls are logged
- [ ] Production usage approved by the security owner

## Local development

- [ ] `.env` exists only locally
- [ ] `.env` is ignored by Git
- [ ] `npm run validate` passes
- [ ] `npm run typecheck` passes
- [ ] Tool calls are tested against a sample realm

## Review questions

- Which realms can the MCP server access?
- Which tools can the AI Agent call?
- Can the server read user PII?
- Are audit logs retained?
- Who can configure or restart the MCP server?
- What happens if the AI answer is wrong?

## Production rule

AI output should be treated as an operational finding, not an approved change. Any Keycloak change should go through the existing change process.
