# Private EKS Helm deployment with GitHub Actions

This example accompanies the [tistory-cloud blog](https://tistory-cloud.tistory.com/) and shows how to deploy a small Helm chart to a private Amazon EKS cluster by running the workflow on a self-hosted runner inside the VPC.

## What this repository demonstrates

- Private EKS requires the deployment command to run from a network path that can reach the private API endpoint.
- A self-hosted runner can execute GitHub Actions jobs from inside the VPC.
- OIDC can be used so the workflow assumes an AWS role without storing long-lived AWS access keys.
- Helm validation should run before deployment.

## Folder structure

- `.github/workflows/deploy-private-eks.yaml` - deployment workflow
- `chart/` - minimal sample Helm chart
- `values/` - dev and prod values examples
- `runner/` - self-hosted runner notes
- `docs/` - architecture, prerequisites, credentials, troubleshooting, checklist

## Quick start

1. Prepare a private EKS cluster.
2. Place a self-hosted runner in a network that can reach the cluster private endpoint.
3. Configure GitHub OIDC and an IAM role for the workflow.
4. Add the required GitHub secrets:
   - `AWS_ROLE_TO_ASSUME`
   - `EKS_CLUSTER_NAME`
5. Run the workflow manually and choose `dev` or `prod`.

## Related blog post

- [GitHub Actions로 Private EKS에 Helm 배포 자동화하는 방법: self-hosted runner 구성부터 배포까지](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80)
