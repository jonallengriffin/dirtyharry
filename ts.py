from mozrunner import FirefoxRunner
from test import Test

class Ts(Test):
    preferences = { 'browser.EULA.override' : True,
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
                    'extensions.update.notifyUser': False,
                    "capability.principal.codebase.p0.granted" : "UniversalPreferencesWrite UniversalXPConnect UniversalPreferencesRead",
                    "capability.principal.codebase.p0.id" : "file://",
                    "capability.principal.codebase.p0.subjectName": "",
                    "capability.principal.codebase.p1.granted" : "UniversalPreferencesWrite UniversalXPConnect UniversalPreferencesRead",
                    "capability.principal.codebase.p1.id" : "http://localhost",
                    "capability.principal.codebase.p1.subjectName" : "",
                    "signed.applets.codebase_principal_support" : True}

    dry_run_profile = True

    args = ['files/ts/startup_test/startup_test.html?begin=%s']

    arg_injections = ['str(int(time.time()*1000))']

