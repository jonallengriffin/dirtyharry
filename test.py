from talos import Talos
from firefox import Firefox
from profile import Profile

import csv
from dirtyutils import download_url

# get list of addons
f = open('topaddons.csv', "r")
reader = csv.reader(f, delimiter=',')
topaddons = map(lambda a : a, reader)

resultsWriter = csv.writer(open('results.csv', "w"), delimiter=' ')

def run_talos(prof, name):
  app = Firefox(app_dir='firefox')
  t = Talos(profile=prof, firefox=app)
  results = t.run_ts(cycles=1)
  resultsWriter.writerow([name] + results)

# no addons
prof = Profile()
run_talos(prof, "(no addons)")

# top addons
for i in range(1, 5):
  addon_info = topaddons[i]
  url = addon_info[0]
  name = addon_info[1]
  weekly_downloads = addon_info[2]
  
  download_url(url, dest="addon.xpi")
  prof = Profile(plugins=["addon.xpi"])
  run_talos(prof, name)


    



