# terraform init
# terraform apply -> shows:
# anniej-access-key = <sensitive>
# anniej-secret-key = <sensitive>

# terraform output -raw anniej-secret-key

# terraform output -json > outputs.json
# The terraform output command simply parses the 
# state file and extracts the variables you asked.

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.12.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    iam = "http://localhost:4566"
  }
}

resource "aws_iam_user" "anniej" {
  name = var.user-annie
}

# AWS generates both the Access Key and Secret Key
resource "aws_iam_access_key" "anniej-access-key" {
  user = aws_iam_user.anniej.name
}

variable "user-annie" {
  type    = string
  default = "anniej"
}

output "anniej-access-key" {
  value     = aws_iam_access_key.anniej-access-key
  sensitive = true
}

output "anniej-secret-key" {
  value     = aws_iam_access_key.anniej-access-key.secret
  sensitive = true
}
