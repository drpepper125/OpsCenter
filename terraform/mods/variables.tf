variable "ec2_instance_mods_ami" {
    description = "AMI ID for the EC2 instance in the OpsCenter module"
    type        = string
  
}

variable "ec2_instance_mods_instance_type" {
    description = "Instance type for the EC2 instance in the OpsCenter module"
    type        = string
  
}

variable "ec2_instance_mods_key_name" {
    description = "Key pair name for the EC2 instance in the OpsCenter module"
    type        = string
  
}

variable "ec2_instance_mods_security_group_ids" {
    description = "Security group IDs for the EC2 instance in the OpsCenter module"
    type        = list(string)
  
}
variable "ec2_instance_mods_subnet_id" {
    description = "Subnet ID for the EC2 instance in the OpsCenter module"
    type        = string
  
}

variable "ec2_instance_mod_hostname" {
    description = "Hostname for the EC2 instance in the OpsCenter module"
    type        = string    
  
}

variable "ec2_instance_mod_environment" {
    description = "Environment for the EC2 instance in the OpsCenter module"
    type        = string
  
}