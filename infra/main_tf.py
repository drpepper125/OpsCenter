import json
import python_terraform as tf
import os
import ec2


def terraform_plan():
    cwd = os.getcwd()
    os.chdir('../terraform')    
    if os.path.exists('ec2_config.json'):
        print("Terraform configuration found.")
        t = tf.Terraform(working_dir=os.getcwd())
        init_return_code, init_stdout, init_stderr = t.init()
        if init_return_code != 0:
            print("Terraform init failed:")
            print(init_stderr)
            return
        return_code, stdout, stderr = t.plan()
        print("Terraform plan output:")
        print(stdout)
        if stderr:
            print("Terraform plan errors:")
            print(stderr)
        print("Terraform completed.")
    else:
        print("Terraform configuration not found.")
    os.chdir(cwd)

test_ec2 = ec2.EC2(
    ami="ami-12345678",
    instance_type="t2.micro",
    key_name="my-key-pair",
    security_group_ids=["sg-12345678"],
    subnet_id="subnet-12345678",
    region="us-west-2",
    name="my-ec2-instance",
    environment="development"
)
print(json.dumps(test_ec2.__dict__, indent=4))
with open('../terraform/ec2_config.json', 'w') as f:
    json.dump(test_ec2.__dict__, f, indent=4)

terraform_plan()