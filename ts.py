from mozrunner import FirefoxRunner
from talostest import TalosTest

class Ts(TalosTest):
    subprocess_args = {'shell' : True}

    args = ["files/ts/startup_test/startup_test.html?begin=`python -c 'import time; print int(time.time() * 1000);'`"]

