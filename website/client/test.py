#!/usr/bin/python
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("code")
import aws 
servers = aws.ec2_instances()
print servers
