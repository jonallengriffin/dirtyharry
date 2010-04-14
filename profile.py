from mozrunner import FirefoxProfile
from mozrunner import FirefoxRunner

import simplejson
import os.path
import time

class Profile(FirefoxProfile):
    def set_prefs(self, preferences):
        # use prefs.js so talos prefs will be set in time

        prefs_file = os.path.join(self.profile, 'prefs.js')
        # Ensure that the file exists first otherwise create an empty file
        if os.path.isfile(prefs_file):
            f = open(prefs_file, 'a+')
        else:
            f = open(prefs_file, 'w')

        f.write('\n#MozRunner Prefs Start\n')

        pref_lines = ['user_pref(%s, %s);' %
                      (simplejson.dumps(k), simplejson.dumps(v) ) for k, v in
                       preferences.items()]
        for line in pref_lines:
            f.write(line+'\n')
        f.write('#MozRunner Prefs End\n')
        f.flush()
        f.close()

    def initialize(self, runner=FirefoxRunner()):
        runner.profile = self
        runner.start()
        time.sleep(5)
        runner.stop()
        #time.sleep(5)
        




