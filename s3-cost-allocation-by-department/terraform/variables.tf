variable "aws_region" {
  description = "AWS region for the S3 bucket."
  type        = string
  default     = "ap-northeast-2"
}

variable "bucket_name" {
  description = "Globally unique S3 bucket name."
  type        = string
}

variable "department" {
  description = "Department name used for cost allocation."
  type        = string
}

variable "environment" {
  description = "Deployment environment such as dev, stage, or prod."
  type        = string
}

variable "cost_center" {
  description = "Finance cost center code."
  type        = string
}

variable "enable_versioning" {
  description = "Whether to enable versioning for the bucket."
  type        = bool
  default     = true
}
