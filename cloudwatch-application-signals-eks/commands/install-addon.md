# Install the add-on

Use EKS Pod Identity for the CloudWatch agent role when possible.

```bash
aws eks create-addon \
  --addon-name amazon-cloudwatch-observability \
  --cluster-name {{CLUSTER_NAME}} \
  --pod-identity-associations serviceAccount=cloudwatch-agent,roleArn=arn:aws:iam::{{ACCOUNT_ID}}:role/{{ROLE_NAME}}
```

Attach the managed policy `CloudWatchAgentServerPolicy` to the IAM role before creating the add-on.
