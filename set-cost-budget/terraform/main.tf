terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.12.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_budgets_budget" "cost" {
  name         = var.budget_name
  budget_type  = "COST"
  time_unit    = "MONTHLY"
  limit_amount = var.limit_amount
  limit_unit   = "USD"


  notification {
    comparison_operator        = "GREATER_THAN"
    threshold                  = var.threshold_amount
    threshold_type             = "ABSOLUTE_VALUE"
    notification_type          = "ACTUAL"
    subscriber_email_addresses = [var.alert_email]
  }
}

# In a real environment, you split these into main.tf 
# and variables.tf, and pass the actual email address 
# via a terraform.tfvars file or CI/CD environment variables.

variable "aws_region" {
  type    = string
  default = "us-east-1"
}

variable "budget_name" {
  type    = string
  default = "tjs-infra-budget"
}

variable "limit_amount" {
  type    = string
  default = "100"
}

variable "threshold_amount" {
  type    = number
  default = 100
}

variable "alert_email" {
  type    = string
  default = "john@example.com"
}
