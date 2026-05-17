# Verify the add-on

```bash
aws eks describe-addon --cluster-name {{CLUSTER_NAME}} --addon-name amazon-cloudwatch-observability
kubectl get pods -n amazon-cloudwatch
```

Check that the add-on is active and that the CloudWatch components are running before you expect telemetry to appear.
