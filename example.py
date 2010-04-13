from mozrunner import FirefoxRunner
from profile import Profile
from ts import Ts


def test_firebug_unittest():
    firefox = FirefoxRunner(binary='firefox/firefox')
    profile = Profile(plugins=["firebug.xpi"])
    profile.set_prefs({"extensions.firebug.allPagesActivation" : True})

    mochitest = Ts()
    mochitest.run(profile=prof, runner=firefox)

def test_addon_perf():
    firefox = FirefoxRunner(binary='firefox/firefox')

    profile = Profile(plugins=["addon.xpi"])
    
    ts = Ts()
    result = ts.run(profile=profile, runner=firefox)
    print result

if __name__ == "__main__":
    test_addon_perf()



