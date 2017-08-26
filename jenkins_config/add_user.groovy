#!groovy
import hudson.security.*
import jenkins.model.*

//Load XML
JenkinsCredentials = new XmlSlurper().parse("/tmp/stackData.xml")

//Change these when CloudFormation template is ready
jenkins_username = Cloudformation.jenkinsUsername.text()
jenkins_password = Cloudformation.jenkinsPassword.text()

//Load Jenkins class
def instance = Jenkins.getInstance()
def hudsonRealm = new HudsonPrivateSecurityRealm(false)
def users = hudsonRealm.getAllUsers()
users_s = users.collect { it.toString() }

// Create the admin user account if it doesn't already exist.
if (jenkins_username in users_s) {
    def user = hudson.model.User.get(jenkins_username);
    def password = hudson.security.HudsonPrivateSecurityRealm.Details.fromPlainPassword(jenkins_password)
    user.addProperty(password)
    user.save()
}
else {
    
	hudsonRealm.createAccount(jenkins_username, jenkins_password)
    instance.setSecurityRealm(hudsonRealm)
    def strategy = new FullControlOnceLoggedInAuthorizationStrategy()
    instance.setAuthorizationStrategy(strategy)
    instance.save()
}