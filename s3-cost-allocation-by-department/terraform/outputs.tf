output "bucket_name" {
  description = "Created S3 bucket name."
  value       = aws_s3_bucket.department.bucket
}

output "bucket_tags" {
  description = "Tags applied for cost allocation and operations."
  value       = local.common_tags
}
