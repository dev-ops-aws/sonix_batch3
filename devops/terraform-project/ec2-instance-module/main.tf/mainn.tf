provider "aws" {
  region = "ap-south-1"
}

module "ec2_instances" {
  source = "./ec2-instance-module"

  region               = "ap-south-1"
  key_name             = "Saipravali."
  subnet_id           = "subnet-0512e177d2ed9b92f"
  security_group_name = "launch-wizard-2"
  ami                 = "ami-0a0f1259dd1c90938"
  instance_type       = "t2.micro"
}