import jenkins.model.*

def jobName = "Deploy_ELK_Stack"

//Load XML
CloudformationData = new XmlSlurper().parse("/tmp/stackData.xml")
def stackName = CloudformationData.stackName.text()

//Add Stack Name to job config
def file = new File('/tmp/stackData.xml')
def newConfig = file.text.replace('DevOpsAssignment2STACK', stackName)
file.text = newConfig


//Deploy_ELK_Stack_Jenkins_Job_config.xml is located in /tmp
//Moved to this location in the userdata portion of the CloudFormation template
def configXML = new FileInputStream('/tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml')

def xmlStream = new ByteArrayInputStream( configXML.getBytes() )

//Create Job
Jenkins.instance.createProjectFromXML(jobName, xmlStream)



def copyAndReplaceText(source, dest, Closure replaceText){
    dest.write(replaceText(source.text))
}