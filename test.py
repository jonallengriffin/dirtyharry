from mozrunner import FirefoxRunner
from profile import Profile
import time
import subprocess

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

        runner.kp_kwargs = {'stdout' : subprocess.PIPE}

        if(self.arg_injections):
            for i in range(0, len(self.args)):
                self.args[i] = self.args[i] % eval(self.arg_injections[i])
        runner.cmdargs = self.args

        runner.start()

        output, error = runner.process_handler.communicate()

        return self.format_output(output)

    def initialize_profile(self, profile):
        for extension in self.extensions:
            profile.install_plugin(extension)
        profile.set_prefs(self.preferences)
        return

    def format_output(self, output):
        return output
        
        
