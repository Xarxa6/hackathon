import traceback
import sys

if __name__ == "__main__":
    try:
        import config
        import log
        import dal
        import api
        log.info("Xarxa6 API is booting ...")
        if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEV':
            api.app.run(host = config.bootConfig['host'], port = config.bootConfig['port'], debug=True,use_evalex=False)
        else:
            api.app.run(host = config.bootConfig['host'], port = config.bootConfig['port'])
    except:
        print "Xarxa6 API has NOT started!"
        traceback.print_exc()
