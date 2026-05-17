# Deployment checklist

- [ ] Runner is online with the expected labels.
- [ ] Runner can resolve and reach the private EKS endpoint.
- [ ] GitHub OIDC role trust is restricted to the intended repository and environment.
- [ ] `helm lint` passes.
- [ ] `helm template` renders as expected.
- [ ] The target namespace and release name are correct.
- [ ] Production deployments use approval controls if required.
