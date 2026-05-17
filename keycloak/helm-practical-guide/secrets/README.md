# Secret examples

Use this folder as a reminder of one rule:

> **Create real Secrets outside Git. Commit only the names you reference from values files.**

## Admin password Secret

```bash
kubectl create secret generic {{KEYCLOAK_ADMIN_SECRET_NAME}} \
  --from-literal=admin-password='{{KEYCLOAK_ADMIN_PASSWORD}}'
```

## External database Secret

```bash
kubectl create secret generic {{KEYCLOAK_DB_SECRET_NAME}} \
  --from-literal=db-user='{{KEYCLOAK_DB_USER}}' \
  --from-literal=db-password='{{KEYCLOAK_DB_PASSWORD}}'
```

## TLS Secret for Ingress termination

```bash
kubectl create secret tls {{TLS_SECRET_NAME}} \
  --cert={{TLS_CERT_FILE}} \
  --key={{TLS_KEY_FILE}}
```

## Safety notes

- Do not commit generated Secret manifests.
- Do not commit private key files.
- Prefer a proper secret manager for production workflows.
