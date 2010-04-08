import platform
import os

class Firefox(object):
   def __init__(self, app_dir='firefox'):
       if platform.system() == "Linux":
           self.process_name = 'firefox-bin'
           self.executable_path = os.path.join(app_dir, 'firefox')
       elif platform.system() in ("Windows", "Microsoft"):
           self.process_name = 'firefox.exe'
           self.executable_path = os.path.join(app_dir, 'firefox.exe')
       elif platform.system() == "Darwin":
           self.process_name = 'firefox-bin'
           self.executable_path = os.path.join(app_dir, 'Firefox.app/Contents/MacOS/firefox-bin')
