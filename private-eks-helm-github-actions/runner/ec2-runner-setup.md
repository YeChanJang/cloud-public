# EC2 runner setup outline

1. Launch an EC2 instance in a subnet that can reach the EKS private endpoint.
2. Attach a security group that allows the required outbound traffic.
3. Install Git, AWS CLI, kubectl, and Helm.
4. Register the runner with labels: `self-hosted`, `linux`, `x64`, `private-eks`.
5. Confirm the runner can resolve and reach the private EKS endpoint.
6. Keep runner patching, hardening, and access control in your operations process.
