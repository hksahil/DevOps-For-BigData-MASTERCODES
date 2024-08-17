## Two parts
#1. Provider -> Tells where to upload
#2. Resource -> Tells what to upload

# Commands to use
## terraform init
## terraform plan
## terraform apply
## terraform destroy

# Setting up Provider
provider "aws" {
  region = "eu-west-2"
  access_key = ""
  secret_key = ""
}

provider "github" {
  token = ""
}

# Setting up resource - S3 Bucket
resource "aws_s3_bucket" "bucket" {
  bucket = "my-terraform-bucket-example"
  tags = {
    Name        = "My bucket"
  }
}

# Setting up resources -> Database
resource "aws_db_instance" "default" {
  allocated_storage    = 10
  db_name              = "proddb"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "foo"
  password             = "foobarbaz"
}

# Setting up resources -> github repo
resource "github_repository" "example" {
  name        = "Code-Repoistory-using-Terrafrom"
  description = "Automated Repo"
  visibility = "public"
}

# Settup up resource - EC2 instance
resource "aws_instance" "server" {
  ami                     = "ami-0fc7a46876a675c5f"
  instance_type           = "t3.micro"
}
