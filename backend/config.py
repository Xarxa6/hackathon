import json
import traceback

config_file = './config/application.json'
defaults = './config/reference.json'

def loadConfig(f):
    print "[INFO] Loading configuration from " + f + "..."
    with open(f, 'r') as opened:
        configuration = json.load(opened)
        dbConfig = configuration['analytics-db']
        logConfig = configuration['log']
        bootConfig = configuration['server']
        return dbConfig, logConfig, bootConfig

try:
    dbConfig, logConfig, bootConfig = loadConfig(config_file)
except:
    print "[WARNING] Could not load application.json. Importing defaults..."
    print traceback.print_exc()
    try:
        dbConfig, logConfig, bootConfig = loadConfig(defaults)
    except:
        print "[ERROR] COULD NOT LOAD ANY CONFIG!"
        print traceback.print_exc()

        dbConfig = {
            "host" : "localhost",
            "name" : "xarxa6",
            "user" : "api",
            "pass" : ""
        }

        logConfig = {
            "level" : "DEBUG",
            "file" : ""
        }

        bootConfig = {
            "host" : "127.0.0.1",
            "port" : 5000
        }
