terraform {
  backend "s3" {
    bucket = "faizulkarim-demo-tfstate-bucket"
    key    = "eks/terraform.tfstate"
    region = "ap-south-1"
  }
}


