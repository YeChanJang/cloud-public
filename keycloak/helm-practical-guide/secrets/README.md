# Secret examples

Create real Secrets outside Git and reference only their names from values files.

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

Do not commit generated Secret manifests or private key files to this repository.
