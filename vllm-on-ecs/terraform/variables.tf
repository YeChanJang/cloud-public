variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-2"
}

variable "cluster_name" {
  description = "ECS cluster name"
  type        = string
  default     = "vllm-gpu-cluster"
}

variable "service_name" {
  description = "vLLM ECS service name"
  type        = string
  default     = "vllm-openai"
}

variable "gpu_instance_types" {
  description = "GPU EC2 instance types for ECS capacity"
  type        = list(string)
  default     = ["g5.xlarge"]
}

variable "desired_capacity" {
  description = "Initial GPU instance desired capacity"
  type        = number
  default     = 1
}

variable "log_retention_days" {
  description = "CloudWatch log retention days"
  type        = number
  default     = 14
}
