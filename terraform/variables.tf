locals {
  bucket_name_prefix = "healthcare-facilities"
}

variable "region" {
  description = "AWS region for deployment of resources"
  type        = string
}

variable "bucket_name" {
  description = "The name of S3 bucket"
  type        = string
}

variable "environment" {
  description = "Environment setup either dev or prod"
  type        = string
}

variable "aws_account_id" {
  description = "AWS account number"
  type        = string
}
