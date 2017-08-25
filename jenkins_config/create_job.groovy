import jenkins.model.*

def jobName = "Deploy_ELK_Stack"

//Deploy_ELK_Stack_Jenkins_Job_config.xml is located in /tmp
//Moved to this location in the userdata portion of the CloudFormation template
def configXML = new FileInputStream('/tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml')
def xmlStream = new ByteArrayInputStream( configXML.getBytes() )

//Create Job
Jenkins.instance.createProjectFromXML(jobName, xmlStream)