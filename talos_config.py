base_config = {
               'extensions' : {},
               'title' : "test",
               'extra_args' : "",
               'browser_wait' : 5,
               "env" : {'NO_EM_RESTART' : 1},
               'branch': 'testbranch',
               'buildid': 'testbuildid',
               'dirs': {},
               'preferences' : {  'browser.EULA.override' : True,
                    'security.fileuri.strict_origin_policy' : False,
                    'browser.shell.checkDefaultBrowser' : False,
                    'browser.warnOnQuit' : False,
                    'browser.link.open_newwindow' : 2,
                    'dom.allow_scripts_to_close_windows' : True,
                    'dom.disable_open_during_load': False,
                    'dom.max_script_run_time' : 0,
                    'dom.max_chrome_script_run_time' : 0,
                    'browser.dom.window.dump.enabled': True,
                    'network.proxy.type' : 1,
                    'network.proxy.http' : 'localhost',
                    'network.proxy.http_port' : 80,
                    'dom.disable_window_flip' : True,
                    'dom.disable_window_move_resize' : True,
                    'security.enable_java' : False,
                    'extensions.checkCompatibility' : False,
                    'extensions.update.notifyUser': False},
                 'tests' : []
              }

ts_config =  {"name" : "ts",
              "url" : "talos/startup_test/startup_test.html?begin=",
              "url_mod" : "str(int(time.time()*1000))",
              "resolution" : 1,
              "timeout": 150,
              "win_counters" : [],
              "unix_counters" : [],
              "mac_counters" : [],
              "shutdown" : True
             }


