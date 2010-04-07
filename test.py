from talos import Talos
from firefox import Firefox

app = Firefox(app_dir='firefox')

t = Talos(profile='/home/heather/.mozilla/firefox/7ilibqeq.persona', firefox=app)

times = t.run_ts(cycles=3)

for time in times:
  print time
    



