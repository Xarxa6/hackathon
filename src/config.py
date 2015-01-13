import json
import os, sys, traceback

script_dir = os.path.dirname(__file__)
config_file = os.path.join(script_dir, './config/application.json')
defaults = os.path.join(script_dir, './config/reference.json')

def loadConfig(f):
    print "[INFO] Loading configuration from " + f + "..."
    with open(f, 'r') as opened:
        configuration = json.load(opened)
        dbConfig = configuration['analytics-db']
        logConfig = configuration['log']
        bootConfig = configuration['server']
        return dbConfig, logConfig, bootConfig

# If dev is passed to init.py, this script loads the db linked via docker/fig in  /etc/hosts
if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEV':
        print "Booting API using /etc/hosts file..."

        logConfig = {
            "level" : "DEBUG",
            "file" : ""
        }

        bootConfig = {
            "host" : "0.0.0.0",
            "port" : 5000
        }

        with open('/etc/hosts','r') as hosts:
            found = False
            for line in hosts:
                if 'db' in line:
                    found = True
                    ip, hostname = line.strip('\n').split('\t')
                    dbConfig = {
                        "host" : ip,
                        "name" : "xarxa6",
                        "user" : "api",
                        "pass" : "1234" }
            if found is False:
                print "Hosts file:"
                for line in hosts:
                    print line
                raise EnvironmentError('Could not load linked db via /etc/hosts')

else:
    try:
        dbConfig, logConfig, bootConfig = loadConfig(config_file)
    except:
        print "[WARNING] Could not load application.json. Importing defaults..."
        try:
            dbConfig, logConfig, bootConfig = loadConfig(defaults)
        except:
            print "[ERROR] COULD NOT LOAD ANY CONFIG!"
            print traceback.print_exc()
