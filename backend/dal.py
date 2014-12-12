import psycopg2
import log
from config import dbConfig
from utils import protocol

HOST = dbConfig['host']
NAME = dbConfig['name']
USER = dbConfig['user']
PASS = dbConfig['pass']

def match_analyses_sql(tags):
    formatted_tags = str(tags).replace("'", '"')
    q="""
        SELECT anly.payload, anly.status
        FROM (
            SELECT at.analysis_id, count(*) AS cnt
            FROM (
                -- create table from analysis table with one tag per row
                SELECT json_array_elements(tags) AS tag, analysis_id FROM analyses
                ) at
            -- create table from input with one tag per row and join
            INNER JOIN (SELECT json_array_elements('{tags}') AS tag
            ) it
            ON ((at.tag->>'measure' = it.tag->>'measure') or (at.tag->>'dimension' = it.tag->>'dimension'))
            GROUP BY at.analysis_id
        ) matched_tags
        -- join back to analysis jobs table to get the payload and status (cannot group by payload as it is JSON)
        INNER JOIN analyses anly ON anly.analysis_id = matched_tags.analysis_id
        ORDER BY matched_tags.cnt DESC
        LIMIT 100;
    """
    query = q.format(tags=formatted_tags)
    return query

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

#HELPERS
def db():
    db = conn.cursor()
    return db

def escapeForSql(value):
    if type(value) == str:
        return "\'" + value.strip() + "\'"
    else:
        return value

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

def update_analysis(uid,obj):

    return protocol.success("Successfully updated analysis with id "+str(uid))

def new_analysis(source_id,dimensions,metric,query):
    uid = None
    return protocol.success("Successfully created analysis with id "+str(uid))

#TODO continue here
def get_sources():
    sql = "SELECT * from data_sources;"
    cursor = db()
    cursor.execute(sql)
    items = cursor.fetchall()
    return protocol.success("Successfully fetched data sources",items)

def create_source(host,port,user,password,type_of):
    sql = "INSERT INTO data_sources VALUES (DEFAULT,"+host+","+port+","+user+","+password+") "
    uid = db().execute(sql)
    return protocol.success("Successfully create new Source with id "+str(uid))

def update_source(uid,params):
    try:
        _sql = ""
        for key in params:
            _sql = _sql + str(key) + " = " + escapeForSql(params[key]) + ","
        sql = "UPDATE data_sources SET " + _sql[:-1] + " WHERE sid = " + str(uid) +";"
        db().execute(sql)
        return protocol.success("Successfully updated source with id " + str(uid))
    except Exception as e:
        return protocol.error(e)

def delete_source(uid):
    try:
        sql = "DELETE from data_sources where sid =" +str(uid)+";"
        db().execute(sql)
        return protocol.success("Succesfully deleted data source with id " +str(uid)
            )
    except Exception as e:
        return protocol.error(e)

def run_query(query_id):
    return protocol.success("Succesfully executed query with id "+str(query_id))



