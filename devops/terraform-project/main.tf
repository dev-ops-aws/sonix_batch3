resource "aws_instance" "ec2_instance" {
  ami           = "ami-12345678"  # Replace with your desired AMI ID
  instance_type = "var.instance_type"
  key_name      = "your-key-pair"  # Replace with your key pair name

  tags = {
    Name = "var.instance_name"
  }

  vpc_security_group_ids = [module.security_group.security_group_id]
}

module "security_group" {
  source = "./modules/security_group"
}
