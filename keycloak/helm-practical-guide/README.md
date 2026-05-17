# Keycloak Helm practical guide

This folder contains public example files for the blog article series about installing and operating Keycloak with Helm.

## What is included

- `values/values-dev.example.yaml` - a small development-oriented example
- `values/values-prod.example.yaml` - a production-oriented example using placeholders
- `realm/demo-realm-realm.json` - a minimal realm import example
- `docs/install-checklist.md` - deployment and verification checklist

## Before you use these files

1. Copy the example file you need.
2. Replace every `{{PLACEHOLDER}}` value with your own environment-specific value.
3. Create Kubernetes Secrets separately. Do not hard-code passwords into values files.
4. Review your TLS termination design before deploying.

## Placeholder rule

The public files in this folder intentionally use placeholders such as:

- `{{KEYCLOAK_DOMAIN}}`
- `{{RDS_HOST}}`
- `{{TLS_SECRET_NAME}}`
- `{{KEYCLOAK_DB_SECRET_NAME}}`
- `{{KEYCLOAK_ADMIN_SECRET_NAME}}`

These placeholders are not rendered automatically by Helm. Replace them before deployment.
