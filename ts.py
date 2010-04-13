from mozrunner import FirefoxRunner
from talostest import TalosTest

class Ts(TalosTest):
    dry_run_profile = True

    args = ['files/ts/startup_test/startup_test.html?begin=%s']

    arg_injections = ['str(int(time.time()*1000))']

