import yaml
import csv
import copy
import os
import subprocess
import sys

import talos_config
from dirtyutils import path
from mozrunner import FirefoxRunner as Firefox
from profile import Profile

class Talos(object):
    def __init__(self, talos_dir='talos', firefox=Firefox(), profile=Profile()):
        self.talos_dir = talos_dir
        self.firefox = firefox
        self.profile = profile
        preferences = talos_config.base_config['preferences']
        self.profile.set_prefs(preferences)

        self.base_config = copy.copy(talos_config.base_config)
        self.output_dir = os.path.join(talos_dir, 'output')
        self.base_config.update({'process' : firefox.names[0],
           'browser_path' : firefox.binary,
           'browser_log' : os.path.join(talos_dir, 'boutput.txt'),
           'init_url' : os.path.join(talos_dir, 'getInfo.html'),
           'csv_dir' : self.output_dir})

        # import the talos script
        sys.path.append(self.talos_dir)
        global StandaloneTalos
        StandaloneTalos = __import__('run_tests')
    
    def run_ts(self, cycles=1):
        ts_config = copy.copy(talos_config.ts_config)
        ts_config.update({'cycles' : cycles,
           'profile_path' : self.profile.profile,
           'url' : os.path.join(self.talos_dir, 'startup_test/startup_test.html?begin=')})
        config = copy.deepcopy(self.base_config)
        config['tests'].append(ts_config)

        config_path = os.path.join(self.talos_dir, 'ts.config')
        self.write_config(config, config_path)

        StandaloneTalos.test_file(config_path)

        output_path = os.path.join(self.output_dir, 'ts.csv')
        results = self.read_output(output_path)
        
        # clear log file in case the next run fails
        f = open(output_path, "w")
        f.write("")
        f.close()

        return results

    def write_config(self, config, path):
        f = open(path, "w")
        yaml.dump(config, f, canonical=False, default_flow_style=False)
        f.close()

    def read_output(self, path):
        f = open(path, "r")
        reader = csv.DictReader(f, delimiter=',')
        return map(lambda a : a['val'], reader)
       
