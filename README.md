# DevOps Assignment 2

### Objective
Use CM tools such as Puppet, Ansible (preferable), or Chef to automate the installation of ELK. This script must be triggered Jenkins job to set up ELK.
 
### Deliverable
A cloudformation template that launches a Jenkins AMI prepackaged with the job. When the job is run, it should automatically trigger the launch of an EC2 instance and install ELK.

### Prerequisites

Clone the github repository or download the "
**cloudformation_devops_assignment2.template**
" CloudFormation template manually.

```
git clone https://github.com/jrwhite17/DevOpsAssignment2
```

### Deploying the CloudFormation Jenkins template
*Estimated Jenkins Deployment/Configuration Time (t2.small):*
**12 minutes**

* Log into the AWS console.  
* Navigate to the CloudFormation service page.  
* Click on the "Create Stack" button.  
* Click on the "Upload a template to Amazon S3" radio button.  
* Click on the "Choose File" button.  
* Navigate to the directory housing the "cloudformation_devops_assignment2.template" and select "Open".

Note: If you cloned the github repository. The file location should be:
```
/DevOpsAssignment2/cloudformation/cloudformation_devops_assignment2.template
```

* Specify a Stack name and fill out the necessary parameters for this deployment.  
* Select the "Next" button to continue on to the Options page.  
* Select the "Next" button to continue on to the Review page.  
* If everything on the Review page looks satisfactory, click the "Create" button to execute the deployment.

*The Jenkins server's URL can be found under the Stack's "Outputs" tab.*

### Deploying the ELK stack from Jenkins
*Estimated ELK Deployment/Configuration Time (t2.small):*
**6 minutes**

* Log into the Jenkins server using the credentials you provided to the initial CloudFormation template.  
* Click on the "Deploy_ELK_Stack" Jenkins job.  
* On the "Deploy_ELK_Stack" page, click the "Configure" tab.  
* Scroll down to "Build Environment" and enter your valid AWS credentials (Access Key & Secret Key).  
* Click the "Save" button.  
* On the "Deploy_ELK_Stack" page, click the "Build with Parameters" tab.  
* Specify a Stack name and fill out the necessary parameters for this deployment. (Note: If you use the same Stack name as you previously used on the CloudFormation deployment page, that stack will be updated with the new ELK stack.)  
* Click the "Build" button to execute the ELK stack deployment.  

*The ELK stack's URL can be found under the Stack's "Outputs" tab on the CloudFormation page.*


## Running Automated Tests

### Deploying the CloudFormation Jenkins template
*Tested on OS: RHEL7.4, Python: 2.7.5*  
*Requirement: AWS CLI is installed and configured to use valid credentials.*  

Description: This test executes the CloudFormation Jenkins template and evaluates how long the Jenkins deployment/configuration takes.  

* Clone the github repository and execute the following python2 script, "CloudFormationTest.py".  

Note: Here is an example of how you execute the automated test:
```
python DevOpsAssignment2\automatedTests\cloudFormationTest\CloudFormationTest.py
```

#### Tests *executed on 8/26/2017*  
| Stack Name | Pass/Fail | Jenkins EC2 Instance | Jenkins Deployment/Configuration Time (est. min) |
|------------|:---------:|:--------------------:|:-------------------------------------------:|
| test1      | Pass      | t2.small             | 2.84                                       |
| test2      | N/A      | t2.small             | N/A                                       |
| test3      | N/A      | t2.small             | N/A                                       |
| test4      | N/A      | t2.small             | N/A                                       |
| test5      | N/A      | t2.small             | N/A                                       |
| test6      | N/A      | t2.micro             | N/A                                       |
| test7      | N/A      | t2.micro             | N/A                                       |
| test8      | N/A      | t2.micro             | N/A                                       |
| test9      | N/A      | t2.micro             | N/A                                       |
| test10      | N/A      | t2.micro             | N/A                                       |

### Deploying the ELK stack from Jenkins*
**Note: This is not deploying the ELK stack from Jenkins, but simulating the AWS api call Jenkins makes when deploying the ELK stack*  
*Tested on OS: RHEL7.4, Python: 2.7.5*  
*Requirement: AWS CLI is installed and configured to use valid credentials.*  

Description: This test executes the CloudFormation update ELK template and evaluates how long the ELK deployment/configuration takes.  

* Clone the github repository and execute the following python2 script, "elkTest.py".  

Note: Here is an example of how you execute the automated test:
```
python DevOpsAssignment2\automatedTests\elkTest\elkTest.py
```



## Authors

* **Johnathan White** - [Github](https://github.com/jrwhite17)

## Notes
[Google Doc](https://docs.google.com/document/d/1o1o_rkduFHuvIolAd8G8mSbP2x8Q9r0qlCpKwVkSWFo/edit?usp=sharing)

## Potential Improvements

* Configure Jenkins and ELK to use Https
* Deploy the ELK stack accross multiple EC2 instances
* Configure a Nginx reverse proxy for the ELK stack
* Improve deployment time by using a preconfigured Jenkins AMI
* Create handoff of current Stack name to the Jenkins job Stack name default value 
**Completed**
* Create automated tests
**Completed**
* Create a new subnet for the ELK stack 
**Completed**
* Execute Ansible remotely from Jenkins server to the deployed EC2 instance
* Dynamically add ELK stack resources/config to previous CloudFormation template  
* Create parameter for EC2 deployment region