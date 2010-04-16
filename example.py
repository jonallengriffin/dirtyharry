import time

from mozrunner import FirefoxRunner
from profile import Profile
from talos import Talos
from profile import Profile

def test_addon_perf():
    firefox = FirefoxRunner(binary='firefox/firefox')

    profile = Profile()
    profile.initialize(runner=firefox)

    t = Talos(profile=profile, firefox=firefox, talos_dir='talos_linux')
    results = []
    cycles = 10
    for i in range(0, cycles):
        time.sleep(26)
        results.append(t.run_ts(cycles=1)[0])

    print results
         

if __name__ == "__main__":
    test_addon_perf()



