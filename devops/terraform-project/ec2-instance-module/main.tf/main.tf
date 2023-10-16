provider "aws" {
  region = var.region
}

variable "region" {
  description = "AWS region"
}

variable "key_name" {
  description = "Name of the SSH key pair"
}

variable "subnet_id" {
  description = "ID of the subnet"
}

variable "security_group_name" {
  description = "Name of the security group"
}

variable "ami" {
  description = "ID of the AMI"
}

variable "instance_type" {
  description = "Type of EC2 instance"
  default     = "t2.micro"
}

resource "aws_key_pair" "key_pair" {
  key_name   = var.key_name
  public_key = file("~/.ssh/:UserspallaOneDriveDesktopSaipravali..pem")  # Update with the path to your public key
}

resource "aws_security_group" "security_group" {
  name        = var.security_group_name
  description = "Allow inbound SSH traffic"
  vpc_id      = var.subnet_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "ec2_instance_1" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  key_name      = aws_key_pair.key_pair.key_name
  security_groups = [aws_security_group.security_group.name]

  tags = {
    Name = "EC2-Instance-1"
  }
}

resource "aws_instance" "ec2_instance_2" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  key_name      = aws_key_pair.key_pair.key_name
  security_groups= [aws_security_group.security_group.name]

  tags = {
    Name = "EC2-Instance-2"
  }
}
