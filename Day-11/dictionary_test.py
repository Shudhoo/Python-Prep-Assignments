# This is an example of Dictionary Data Type 

# The below declared is list of dictionaries !!
ec2_instances = [{
    "instance_type": "t2.micro",
    "region": "us-east-1",
    "key_name": "test.ppk",
    "ami-id": "ami-5476897656789"
},
{
    "instance_type": "t2.medium",
    "region": "us-west-2",
    "key_name": "project.ppk",
    "ami-id": "ami-5764564789345"
},
{
    "instance_type": "t2.small",
    "region": "eu-west-1",
    "key_name": "demo.ppk",
    "ami-id": "ami-0987698756789"
}]

print(ec2_instances[2]["instance_type"])