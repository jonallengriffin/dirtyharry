import time
import subprocess
from copy import copy

from mozrunner import FirefoxRunner
from profile import Profile

class TestRunner(object):
    preferences = {}

    extensions = {}

    env = {}

    args = []

    subprocess_args = {}

    def __init__(self):
        return

    def run(self, profile=Profile(), runner=FirefoxRunner()):
        self.initialize_profile(profile)

        runner.profile = profile

        proc_args = {'stdout' : subprocess.PIPE}
        proc_args.update(self.subprocess_args)
        runner.kp_kwargs = proc_args

        runner.cmdargs = copy(self.args)

        runner.start()

        output, error = runner.process_handler.communicate()

        return self.format_output(output)

    def initialize_profile(self, profile):
        for extension in self.extensions:
            profile.install_addon(extension)
        profile.set_prefs(self.preferences)
        return

    def format_output(self, output):
        return output
        
        
