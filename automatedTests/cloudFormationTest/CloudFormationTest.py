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
from pprint import pprint

#Stack Name
STACK_NAME="jwhiteStack"
#Stack Parameters
JENKINS_EC2_INSTANCE="t2.small"
JENKINS_PASSSWORD="qwer"
JENKINS_USERNAME="jwhite"
SSH_PEM_KEY_INPUT="jrw_key_pair"

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
DESCRIBE_STACK_CMD="aws cloudformation describe-stacks --stack-name "+STACK_NAME+" >> /tmp/stackOutput.json"
os.system(DESCRIBE_STACK_CMD)

