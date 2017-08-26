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
def testELKUpdateCFTemplate(stack_name,jenkins_ec2_instance,jenkins_password,jenkins_username,elk_ec2_instance,ssh_pem_key_input):
	#Stack Name
	STACK_NAME=stack_name
	#Stack Parameters
	JENKINS_EC2_INSTANCE=jenkins_ec2_instance
	JENKINS_PASSSWORD=jenkins_password
	JENKINS_USERNAME=jenkins_username
	SSH_PEM_KEY_INPUT=ssh_pem_key_input
	ELK_EC2_INSTANCE=elk_ec2_instance

	#Jenkins
	#===============================
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

	DESCRIBE_STACK_CMD="aws cloudformation describe-stacks --stack-name "+STACK_NAME
	stack_output = subprocess.check_output(DESCRIBE_STACK_CMD, shell=True)

	#Load Json and Extract Jenkins URL
	stack_output_json = json.loads(stack_output)
	Jenkins_URL=str(stack_output_json['Stacks'][0]['Outputs'][0]['OutputValue'])

	pprint("Jenkins URL: " + Jenkins_URL)

	#Set timeout for 15 minutes
	t_end = time.time() + 60 * 15
	while time.time() < t_end:
		try:
			r = requests.get(Jenkins_URL)
			if r.status_code == 200:
				pprint("Jenkins is running!")
				pprint(t_end-time.time())
				break
		except requests.ConnectionError, e:
			pass
			#Do nothing

	#ELK
	#===============================	
	#Request stack
	CREATE_STACK_CMD = ("aws cloudformation create-stack \\"
	"--stack-name "+STACK_NAME+" \\"
	"--template-body file://../../cloudformation/cloudformation_devops_assignment2_ELK.template \\"
	"--parameters ParameterKey=JenkinsEC2Instance,ParameterValue="+JENKINS_EC2_INSTANCE+" \\"
	"ParameterKey=JenkinsPassword,ParameterValue="+JENKINS_PASSSWORD+" \\"
	"ParameterKey=JenkinsUsername,ParameterValue="+JENKINS_USERNAME+" \\"
	"ParameterKey=ELKStackEC2Instance,ParameterValue="+ELK_EC2_INSTANCE+" \\"
	"ParameterKey=sshPemKeyInput,ParameterValue="+SSH_PEM_KEY_INPUT+"")
	os.system(CREATE_STACK_CMD)

	#Give Cloudformation time to update stack
	time.sleep(120)

	
	DESCRIBE_STACK_CMD="aws cloudformation describe-stacks --stack-name "+STACK_NAME
	stack_output = subprocess.check_output(DESCRIBE_STACK_CMD, shell=True)

	#Load Json and Extract ELK URL
	stack_output_json = json.loads(stack_output)
	Elk_URL=str(stack_output_json['Stacks'][0]['Outputs'][1]['OutputValue'])

	pprint("ELK URL: " + Elk_URL)

	#Set timeout for 15 minutes
	t_end = time.time() + 60 * 15
	while time.time() < t_end:
		try:
			r = requests.get(Elk_URL)
			if r.status_code == 200:
				pprint("ELK is running!")
				pprint(t_end-time.time())
				break
		except requests.ConnectionError, e:
			pass
			#Do nothing
		
	#Delete Stack
	DELETE_STACK_CMD="aws cloudformation delete-stack --stack-name "+STACK_NAME
	os.system(DELETE_STACK_CMD)
		
#MAIN
testELKUpdateCFTemplate("testELK1","t2.small","root","root","t2.small","jrw_key_pair")
testELKUpdateCFTemplate("testELK2","t2.small","root","root","t2.small","jrw_key_pair")
testELKUpdateCFTemplate("testELK3","t2.small","root","root","t2.micro","jrw_key_pair")
testELKUpdateCFTemplate("testELK4","t2.small","root","root","t2.micro","jrw_key_pair")
testELKUpdateCFTemplate("testELK5","t2.micro","root","root","t2.small","jrw_key_pair")
testELKUpdateCFTemplate("testELK6","t2.micro","root","root","t2.small","jrw_key_pair")
testELKUpdateCFTemplate("testELK7","t2.micro","root","root","t2.micro","jrw_key_pair")
testELKUpdateCFTemplate("testELK8","t2.micro","root","root","t2.micro","jrw_key_pair")