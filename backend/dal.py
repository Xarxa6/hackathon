import psycopg2
import log
from config import dbConfig
from utils.errors import errorify

HOST = dbConfig['host']
NAME = dbConfig['name']
USER = dbConfig['user']
PASS = dbConfig['pass']

match_analyses_sql = lambda tags: """select * from test;"""

#Set up connection
try:
    conn = psycopg2.connect(
        "host='" + HOST + "' \
        dbname='" + NAME + "' \
        user='" + USER + "' \
        password='" + PASS + "'")

    log.info("Succesfully connected to DB "+ HOST +"/" + NAME + \
        " with user " + USER)
except:
    log.critical("Unable to connect to the DB")

#cursor builder
def db():
    db = conn.cursor()
    return db

def query_analyses(tags):
    try:
        if type(tags) is not list:
            raise AssertionError("Tags must be a list!")
        cursor = db()
        cursor.execute(match_analyses_sql(tags))
        log.debug(cursor.fetchall())
        #mock - TODO
        return [
            { "id" : "1",
            "tags": ["stuff", "more"],
            "payload_type": "SQL",
            "payload" : "SELECT * FROM STUFF WHERE thing IS NOT NULL" },
            { "id" : "2",
            "tags": ["things", "exciting"],
            "payload_type": "URL",
            "payload" : "http://unstable.build" }
        ]
    except Exception as e:
        log.error(e)
        return errorify(e)




