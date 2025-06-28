locals {
  ec2_config_file = "${path.module}/ec2_config.json"
}
module "ec2_instance_mods" {
  source = "./mods/ec2"

  ec2_instance_mods_ami                = local.ec2_config_file.ami
  ec2_instance_mods_instance_type      = local.ec2_config_file.instance_type
  ec2_instance_mods_key_name           = local.ec2_config_file.key_name
  ec2_instance_mods_security_group_ids = local.ec2_config_file.security_group_ids
  ec2_instance_mods_subnet_id          = local.ec2_config_file.subnet_id
  ec2_instance_mod_hostname            = local.ec2_config_file.name
  ec2_instance_mod_environment         = local.ec2_config_file.environment
  
}