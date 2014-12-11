import logging

# logging.basicConfig(format='[%(levelname)s] %(message)s', filename='xarxa6-api.log', level=logging.DEBUG)

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

def critical(msg):
    logging.critical(msg)

#TODO FINISH IMPLEMENTING BASIC LOG MODULE
