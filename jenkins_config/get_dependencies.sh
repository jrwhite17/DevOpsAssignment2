#!/bin/bash

###
#
# Configure Jenkins Server on RHEL EC2 instance.
# Author : Johnathan White
# Date : 20170820
#
###

JENKINS_HOME_DIR="/var/lib/jenkins"

#Update Packages
sudo yum update -y
#Install wget
sudo yum install wget -y
#Install Java
sudo yum install java -y


#Add the Jenkins repository to the yum repos
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
#Import Jenkins repository key
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
#Install Jenkins
sudo yum install jenkins -y
#Move configuration files to Jenkins directory
sudo mkdir $JENKINS_HOME_DIR/init.groovy.d
sudo mv DevOpsAssignment2/jenkins_config/*.groovy $JENKINS_HOME_DIR/init.groovy.d/.
#Move Deploy_ELK_Stack_Jenkins_Job.xml to /tmp/. so the create_job.groovy script knows where to find it
sudo mv DevOpsAssignment2/jenkins_config/Deploy_ELK_Stack_Jenkins_Job_config.xml /tmp/.
#Allow access to Deploy_ELK_Stack_Jenkins_Job_config to add defualt stack name
sudo chmod 777 /tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml

#Start Jenkins
sudo service jenkins start

#Install Git
sudo yum install git -y

#Get the EPEL.rpm
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
#Install EPEL
sudo yum install epel-release-latest-7.noarch.rpm -y
#Update just in case
sudo yum update -y

#Install pip
sudo yum install python-pip -y
#Install awscli
sudo pip install awscli --upgrade --user

#Restart Jenkins just in case
sudo service jenkins restart