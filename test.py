from mozrunner import FirefoxRunner
from profile import Profile
import time

class Test(object):
    preferences = {}

    extensions = {}

    env = {}

    dry_run_profile = False

    args = []

    def __init__(self):
        return

    def run(self, profile=Profile(), runner=FirefoxRunner()):
        self.initialize_profile(profile)

        if(self.dry_run_profile):
          profile.initialize(runner)

        runner.profile = profile

        if(self.arg_injections):
            for i in range(0, len(self.args)):
                self.args[i] = self.args[i] % eval(self.arg_injections[i])

        runner.cmdargs = self.args

        runner.start()
        #time.sleep(10)
        #runner.stop()    

        # collect output
        return

    def initialize_profile(self, profile):
        for extension in self.extensions:
            profile.install_plugin(extension)
        profile.set_prefs(self.preferences)
        return
        
        
