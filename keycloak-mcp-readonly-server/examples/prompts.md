# Example prompts

## Realm inspection

```text
List the Keycloak realms this readonly MCP server can see.
```

## Client inspection

```text
List clients in the sample realm and summarize which clients are public clients.
```

## Redirect URI review

```text
Check the sample realm for risky redirect URI patterns and explain why each one needs review.
```

## User metadata review

```text
List enabled users matching "admin". Do not show raw email addresses.
```

## Admin role review

```text
Find admin-like realm roles and explain which ones should be reviewed before production use.
```
