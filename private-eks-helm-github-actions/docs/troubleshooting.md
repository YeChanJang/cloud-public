# Troubleshooting

## Job stays queued
Check whether a runner with the `private-eks` label is online.

## `aws eks update-kubeconfig` fails
Check OIDC trust policy, assumed role permission, and cluster name.

## EKS API is unreachable
Check DNS resolution, route path, and security groups from the runner host.

## Helm deployment fails
Run `helm lint` and `helm template` locally or in the workflow before deployment.
