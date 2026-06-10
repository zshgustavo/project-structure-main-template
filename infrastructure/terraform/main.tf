# Terraform root module — customize for your cloud provider

terraform {
  required_version = ">= 1.5.0"

  # backend "s3" {
  #   bucket = "your-terraform-state"
  #   key    = "project-structure-main-template/terraform.tfstate"
  #   region = "us-east-1"
  # }
}

# module "environment" {
#   source = "./modules/environment"
#   env    = var.environment
# }