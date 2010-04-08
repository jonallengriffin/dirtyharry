from talos import Talos
from mozrunner import FirefoxRunner
from profile import Profile

import csv
from dirtyutils import download_url

resultsWriter = csv.writer(open('results.csv', "w"), delimiter=' ')

firefox = FirefoxRunner(binary='firefox/firefox')

def run_talos(prof, name):
  t = Talos(profile=prof, firefox=firefox)
  results = t.run_ts(cycles=1)
  resultsWriter.writerow([name] + results)

# no addons
prof = Profile()
prof.initialize(runner=firefox)
run_talos(prof, "(no addons)")

prof = Profile()
prof.initialize(runner=firefox)
run_talos(prof, "(no addons)")

# top addons
f = open('topaddons.csv', "r")
reader = csv.reader(f, delimiter=',')
topaddons = map(lambda a : a, reader)

for i in range(1, 4):
  addon_info = topaddons[i]
  url = addon_info[0]
  name = addon_info[1]
  weekly_downloads = addon_info[2]
  try:
    download_url(url, dest="addon.xpi")
    prof = Profile(plugins=["addon.xpi"])
    prof.initialize(runner=firefox)
    run_talos(prof, name)
  except:
    continue # could be a bad zip file, move along

    



