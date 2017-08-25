import jenkins.model.*

def jobName = "Deploy_ELK_Stack"

//Determine where this location will be..
//Could have the initial bash script place it in /tmp?
def configXML = new FileInputStream('/tmp/Deploy_ELK_Stack_Jenkins_Job_config.xml')


def xmlStream = new ByteArrayInputStream( configXML.getBytes() )

Jenkins.instance.createProjectFromXML(jobName, xmlStream)