# Keycloak Helm install checklist

## Before deployment

- [ ] Decide whether TLS terminates at Ingress or inside Keycloak.
- [ ] Prepare the Keycloak domain name.
- [ ] Create Kubernetes Secrets for the admin password and external database credentials.
- [ ] Confirm the RDS endpoint, database name, username, and network reachability.
- [ ] Replace every `{{PLACEHOLDER}}` in the selected values file.
- [ ] Decide how realm configuration will be imported and versioned.

## Production values review

- [ ] `production: true`
- [ ] `postgresql.enabled: false`
- [ ] `externalDatabase.*` points to the external database
- [ ] `hostnameStrict: true`
- [ ] `proxyHeaders` matches the reverse proxy design
- [ ] `ingress.tls: true`
- [ ] resource requests and limits are set
- [ ] probes are enabled
- [ ] metrics are enabled

## After deployment

- [ ] The pod becomes Ready.
- [ ] The public hostname opens over HTTPS.
- [ ] Redirect URLs use the expected hostname and scheme.
- [ ] Admin login works.
- [ ] The application realm exists as expected.
- [ ] Metrics endpoint is reachable from the monitoring stack.
- [ ] Logs do not show database, hostname, or proxy-header errors.

## Do not commit

- Real passwords
- Private keys
- Production domains if the repository is meant to stay generic
- Internal IP addresses or private database endpoints
