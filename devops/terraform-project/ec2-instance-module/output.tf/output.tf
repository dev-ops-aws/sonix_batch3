output "public_dns_ec2_instance_1" {
  value = aws_instance.ec2_instance_1.public_dns
}

output "public_dns_ec2_instance_2" {
  value = aws_instance.ec2_instance_2.public_dns
}
