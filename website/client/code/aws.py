#!/usr/bin/python

import boto3
ec2 = boto3.resource('ec2')

def ec2_instances():
    servers = []
    instances = ec2.instances.all()
    for instance in instances:
        name = instance.tags[0]['Value']
        status = instance.state['Name']
        private_ip = instance.private_ip_address
        if instance.public_ip_address == None:
            public_ip = "-"
        else:
            public_ip = instance.public_ip_address
        if instance.platform == "windows":
            system = "windows"
        else:
            system = "Linux"
        launch_time = instance.launch_time.strftime("%Y-%m-%d-%H")
        server = [ name , status , system , private_ip , public_ip , launch_time]
        servers.append(server)
    return servers

if __name__ == '__main__':
        ec2_instances()
