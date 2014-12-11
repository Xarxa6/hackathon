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
    return dbConfig, logConfig

try:
    dbConfig, logConfig = loadConfig(config_file)
except:
    print "[WARNING] Could not load application.json. Importing defaults..."
    print traceback.print_exc()
    try:
        dbConfig, logConfig = loadConfig(defaults)
    except:
        print "[CRITICAL] COULD NOT LOAD ANY CONFIG!"
        print traceback.print_exc()
