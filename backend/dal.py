import psycopg2
import traceback
import sys
import log
import logging

#TODO IMPLEMENT BASIC CONNECTION OBJECT

try:
    conn = psycopg2.connect("dbname='xarxa6' \
        user='xarxa6' \
        host='localhost'")
except:
    msg = "I am unable to connect to the DB"
    log.critical(msg)
    #traceback.print_exc(file=sys.stdout)
