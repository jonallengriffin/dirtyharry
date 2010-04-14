from talos import Talos
from mozrunner import FirefoxRunner
from profile import Profile

import csv
from dirtyutils import download_url
import traceback

results_file = open('results.csv', "w")
resultsWriter = csv.writer(results_file, delimiter=' ')

raw_file = open('raw_results.csv', "w")
rawWriter = csv.writer(raw_file, delimiter=' ')

firefox = FirefoxRunner(binary='firefox/firefox')

cycles = 3

def run_talos(prof, name):
  t = Talos(profile=prof, firefox=firefox, talos_dir='talos_linux')
  results = t.run_ts(cycles=cycles)

  rawWriter.writerow([name] + results)
  raw_file.flush()

  average = int(round(reduce(lambda x, y: int(x)+int(y), results) / cycles))
  resultsWriter.writerow([name, average])
  results_file.flush()

resultsWriter.writerow(['addon_name', 'ts_average'])
rawWriter.writerow(['addon_name', 'ts1', 'ts2', 'ts3'])

# no addons
prof = Profile()
prof.initialize(runner=firefox)
run_talos(prof, "<empty profile>")

prof = Profile()
prof.initialize(runner=firefox)
run_talos(prof, "<empty profile>")

# top addons
f = open('topaddons.csv', "r")
reader = csv.reader(f, delimiter=',')
topaddons = map(lambda a : a, reader)

for i in range(1, 1000):
  addon_info = topaddons[i]
  url = addon_info[0]
  name = addon_info[1]
  weekly_downloads = addon_info[2]
  
  for i in range(0, 3):
    try:
      download_url(url, dest="addon.xpi")
      prof = Profile(plugins=["addon.xpi"])
      prof.initialize(runner=firefox)
      run_talos(prof, name)
      downloaded = True
      break
    except:
      continue

  if not downloaded:
    resultsWriter.writerow([name, 0])

    



