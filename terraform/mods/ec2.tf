resource "aws_instance" "ec2_instance_mods" {

  ami           = var.ec2_instance_mods_ami
  instance_type = var.ec2_instance_mods_instance_type
  key_name      = var.ec2_instance_mods_key_name

  vpc_security_group_ids = var.ec2_instance_mods_security_group_ids
  subnet_id              = var.ec2_instance_mods_subnet_id
  tags = {
    Name        = var.ec2_instance_mod_hostname
    Environment = var.ec2_instance_mod_environment
  }

  lifecycle {
    create_before_destroy = true
  }
  
}