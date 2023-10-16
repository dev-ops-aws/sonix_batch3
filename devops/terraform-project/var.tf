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
