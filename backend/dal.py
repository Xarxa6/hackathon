import psycopg2
import log
from config import dbConfig
from utils import protocol

HOST = dbConfig['host']
NAME = dbConfig['name']
USER = dbConfig['user']
PASS = dbConfig['pass']

def match_analyses_sql(tags):
    return """select * from available_analysis;"""

def insert_new_analysis_sql(tags, sentence):
    return """insert * from available_analysis;"""

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


def queue_analysis(tags, sentence):
    try:
        db().execute(insert_new_analysis_sql(tags,sentence))
        log.info("Successfully appended new analysis to queue")
        return { 'status' : 'OK' }
    except Exception as e:
        return protocol.error(e)

def query_analyses(tags):
    try:
        if type(tags) is not list:
            raise AssertionError("Tags must be a list!")
        cursor = db()
        cursor.execute(match_analyses_sql(tags))
        msg = "Succesfylly extracted analyses"
        return protocol.success(msg,cursor.fetchall())
    except Exception as e:
        return protocol.error(e)

def update_analysis(uid):
    return protocol.success("Successfully updated analysis with id "+str(uid))

def new_analysis(source_id,dimensions,metric,query):
    uid = None
    return protocol.success("Successfully created analysis with id "+str(uid))

def get_sources():
    return protocol.success("Successfully fetched data sources")

def create_source(host,port,user,password,type_of):
    uid = None
    return protocol.success("Successfully create new Source with id "+str(uid))

def update_source(uid,fields):
    return protocol.success("Successfully updated source with id " + str(uid))

def delete_source(uid):
    return protocol.success("Succesfully deleted data source with id " +str(uid))

def run_query(query_id):
    return protocol.success("Succesfully executed query with id "+str(query_id))



