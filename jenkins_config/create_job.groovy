import jenkins.model.*

def jobName = "Deploy_ELK_Stack"

//Deploy_ELK_Stack_Jenkins_Job_config.xml is located in /tmp
//Moved to this location in the userdata portion of the CloudFormation template
//def configXML = new FileInputStream('/tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml')

//Load XML
CloudformationData = new XmlSlurper().parse("/tmp/stackData.xml")
def stackName = CloudformationData.stackName.text()

//String s = new String(bytes, StandardCharsets.UTF_8);
//def xmlStream = new ByteArrayInputStream( configXML.getBytes() )

String xmlConfig = new File('/tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml').getText('UTF-8')

//Create Job
Jenkins.instance.createProjectFromXML(jobName, xmlConfig)