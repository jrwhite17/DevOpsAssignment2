###
#
# Deploy Cloudformation template from AWS CLI.
# Author : Johnathan White
# Date : 20170826
# Configure AWS CLI credentials prior to running this script.
#
###

import json
import re
import time
import os
import subprocess
import requests
from pprint import pprint

#Function
def testJenkinsCFTemplate(stack_name,jenkins_ec2_instance,jenkins_password,jenkins_username,ssh_pem_key_input):
	#Stack Name
	STACK_NAME=stack_name
	#Stack Parameters
	JENKINS_EC2_INSTANCE=jenkins_ec2_instance
	JENKINS_PASSSWORD=jenkins_password
	JENKINS_USERNAME=jenkins_username
	SSH_PEM_KEY_INPUT=ssh_pem_key_input

	#Request stack
	CREATE_STACK_CMD = ("aws cloudformation create-stack \\"
	"--stack-name "+STACK_NAME+" \\"
	"--template-body file://../../cloudformation/cloudformation_devops_assignment2.template \\"
	"--parameters ParameterKey=JenkinsEC2Instance,ParameterValue="+JENKINS_EC2_INSTANCE+" \\"
	"ParameterKey=JenkinsPassword,ParameterValue="+JENKINS_PASSSWORD+" \\"
	"ParameterKey=JenkinsUsername,ParameterValue="+JENKINS_USERNAME+" \\"
	"ParameterKey=sshPemKeyInput,ParameterValue="+SSH_PEM_KEY_INPUT+"")
	os.system(CREATE_STACK_CMD)

	#Give Cloudformation time to deploy stack
	time.sleep(120)

	#Write Stack Output to /tmp/stackOutput.json
	DESCRIBE_STACK_CMD="aws cloudformation describe-stacks --stack-name "+STACK_NAME
	stack_output = subprocess.check_output(DESCRIBE_STACK_CMD, shell=True)

	#Load Json and Extract Jenkins URL
	stack_output_json = json.loads(stack_output)
	Jenkins_URL=str(stack_output_json['Stacks'][0]['Outputs'][0]['OutputValue'])

	pprint("Jenkins URL: " + Jenkins_URL)

	#Set timeout for 15 minutes
	jenkins_t_end = time.time() + 60 * 15
	predeploy_time = time.time()
	while time.time() < jenkins_t_end:
		try:
			r = requests.get(Jenkins_URL)
			if r.status_code == 200:
				pprint("Jenkins is running!")
				pprint((time.time()-predeploy_time)/60) #Minutes
				break
		except requests.ConnectionError, e:
			pass
			#Do nothing
		
	#Delete Stack
	DELETE_STACK_CMD="aws cloudformation delete-stack --stack-name "+STACK_NAME
	os.system(DELETE_STACK_CMD)
	
		
#MAIN
testJenkinsCFTemplate("test1","t2.small","root","root","jrw_key_pair")
testJenkinsCFTemplate("test2","t2.small","root","root","jrw_key_pair")
testJenkinsCFTemplate("test3","t2.small","root","root","jrw_key_pair")
testJenkinsCFTemplate("test4","t2.small","root","root","jrw_key_pair")
testJenkinsCFTemplate("test5","t2.small","root","root","jrw_key_pair")
testJenkinsCFTemplate("test6","t2.micro","root","root","jrw_key_pair")
testJenkinsCFTemplate("test7","t2.micro","root","root","jrw_key_pair")
testJenkinsCFTemplate("test8","t2.micro","root","root","jrw_key_pair")
testJenkinsCFTemplate("test9","t2.micro","root","root","jrw_key_pair")
testJenkinsCFTemplate("test10","t2.micro","root","root","jrw_key_pair")