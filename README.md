# DevOps Assignment 2

### Objective:
Use CM tools such as Puppet, Ansible (preferable), or Chef to automate the installation of ELK. This script must be triggered Jenkins job to set up ELK.
 
### Deliverable:
A cloudformation template that launches a Jenkins AMI prepackaged with the job. When the job is run, it should automatically trigger the launch of an EC2 instance and install ELK.

### Prerequisites

Clone the github repository or download the "cloudformation_devops_assignment2.template" CloudFormation template manually.

```
git clone https://github.com/jrwhite17/DevOpsAssignment2
```

### Deploying the CloudFormation template

Log into the AWS console.  
Navigate to the CloudFormation service page.  
Click on the "Create Stack" button.  
Click on the "Upload a template to Amazon S3" radio button.  
Click on the "Choose File" button.  
Navigate to the directory housing the "cloudformation_devops_assignment2.template" and select "Open".

Note: If you cloned the github repository. The file location should be:
```
/DevOpsAssignment2/cloudformation/cloudformation_devops_assignment2.template
```

Specify a Stack name and fill out the necessary parameters for this for this deployment.  
Select the "Next" button to continue on to the Options page.  
Select the "Next" button to continue on to the Review page.  
If everything on the Review page looks satisfactory, click the "Create" button to execute the deployment.



## Running the tests

### TBD

## Authors

* **Johnathan White** - [Github](https://github.com/jrwhite17)

## Potential Improvements

* Configure Jenkins to use Https
* Deploy the ELK stack accross multiple EC2 instances
* Configure a Nginx reverse proxy for the ELK stack
* Improve deployment time by using a preconfigured Jenkins AMI

