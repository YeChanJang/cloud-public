# Self-hosted runner notes

Use a runner that can reach the private EKS API endpoint.

## Recommended labels

- `self-hosted`
- `linux`
- `x64`
- `private-eks`

## Minimum expectations

- outbound access to GitHub
- network path to the EKS private endpoint
- AWS CLI, kubectl, Helm installed
- least-privilege IAM role assumption through GitHub OIDC
