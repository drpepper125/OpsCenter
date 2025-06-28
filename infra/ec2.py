import json

class EC2:
    def __init__(self, ami, instance_type, key_name, security_group_ids, subnet_id, region, name, environment):
        self.ami = ami
        self.instance_type = instance_type
        self.key_name = key_name
        self.security_group_ids = security_group_ids
        self.subnet_id = subnet_id
        self.region = region
        self.name = name
        self.environment = environment

