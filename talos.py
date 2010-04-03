import yaml
import csv

class Talos(object):
    def __init__(self, talos_dir='talos', profile=None):
        self.talos_dir = talos_dir
        self.profile = profile
        # self.profile.setPreference({"browser.dumpenabled": 'true'})

    base_config = {'preferences' : '{}',
                   'extensions' : '{}',
                   'csv_dir' : "'output'",
                   'title' : 'test',
                   'extra_args' : "''",
                   'browser_wait' : '5',
                   'browser_log' : 'browser_output.txt'
                   'env' : 'NO_EM_RESTART : 1'}

    def write_config(self, config_name='test.config', config={}):
        f = open(config_name, "w")
        yaml.dump(dataMap, f)
        f.close()
        return
    
    def run_ts(self, cycles=10):
        # create config file
          # profile_path : self.profile.path
          # tests : { " - name" : "ts",
                     # "url" : "startup_test/startup_test.html?begin="}
          # init_url: getInfo.html

        # open process talos_dir + "run_tests.py --
        # open output/ts.csv
        # return [t1, t2, ..., t10]
        return
 
    def run_ts_cold(self):
        return

    def run_tp(self):
        return
        
