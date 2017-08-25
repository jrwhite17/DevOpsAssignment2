import jenkins.model.*

//Define what plugins will be pulled and install from this Groovy script
//Current plugins are: jenkins-cloudformation-plugin & github
def pluginParameter="jenkins-cloudformation-plugin github"
def plugins = pluginParameter.split()
println(plugins)
def instance = Jenkins.getInstance()
def pm = instance.getPluginManager()
def uc = instance.getUpdateCenter()
def installed = false

//Loop through each plugin and install
plugins.each {
  if (!pm.getPlugin(it)) {
    def plugin = uc.getPlugin(it)
    if (plugin) {
      println("Installing " + it)
      plugin.deploy()
      installed = true
    }
  }
}

instance.save()
if (installed)
instance.doSafeRestart()