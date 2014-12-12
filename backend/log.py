import logging
from config import logConfig
import traceback

FORMAT = '[%(levelname)s][%(asctime)s] %(message)s'
OUTPUT = logConfig['file']
LEVEL = logConfig['level']

if OUTPUT == '':
    logging.basicConfig(format=FORMAT, level=LEVEL.upper())
else:
    logging.basicConfig(format=FORMAT, level=LEVEL.upper(), filename = OUTPUT)


def critical(msg):
    logging.critical(msg)
    traceback.print_exc()

def error(msg):
    logging.error(msg)
    traceback.print_exc()

def info(msg):
    logging.info(msg)

def debug(msg):
    logging.debug(msg)

def warn(msg):
    logging.warning(msg)

def warning(msg):
    logging.warning(msg)
