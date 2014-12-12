import psycopg2
import log
from config import dbConfig
from utils import protocol
import model

HOST = dbConfig['host'].strip()
NAME = dbConfig['name'].strip()
USER = dbConfig['user'].strip()
PASS = dbConfig['pass'].strip()

def match_analyses_sql(tags):
    formatted_tags = str(tags).replace("'", '"')
    q="""
        SELECT anly.analysis_id, anly.tags, anly.payload, anly.status
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
    formatted_tags = str(tags).replace("'", '"')
    print tags
    print sentence
    q="""
        INSERT INTO analyses
        VALUES (DEFAULT, '{tags}', '{{"query":"{sentence}"}}', 'queued');
    """
    query = q.format(tags=formatted_tags, sentence=sentence)
    return query

#Set up connection
try:
    conn = psycopg2.connect(
        "host='" + HOST + "' \
        dbname='" + NAME + "' \
        user='" + USER + "' \
        sslmode='prefer' \
        password='" + PASS + "'")

    conn.autocommit = True

    log.info("Succesfully connected to DB "+ HOST +"/" + NAME + \
        " with user " + USER)
except:
    log.critical("Unable to connect to the DB")

#HELPERS
def db():
    db = conn.cursor()
    return db

def query(sql):
    log.debug("Executing query in host:{} -> {}".format(HOST,sql))
    return sql

def escapeForSql(value):
    if type(value) == str or type(value) == unicode:
        return "\'" + value.strip() + "\'"
    else:
        log.debug("Not escaping value with type " + str(type(value)))
        return str(value)

def queue_analysis(sentence, tags):
    try:
        db().execute(query(insert_new_analysis_sql(tags,sentence)))
        log.info("Successfully appended new analysis to queue")
        return { 'status' : 'OK' }
    except Exception as e:
        return protocol.error(e)

def query_analyses(tags):
    try:
        if type(tags) is not list:
            raise AssertionError("Tags must be a list!")
        cursor = db()
        cursor.execute(query(match_analyses_sql(tags)))
        msg = "Succesfully extracted analyses"
        i = cursor.fetchall()
        print i
        items = [model.Analysis(proto) for proto in i]
        return protocol.success(msg,items)
    except Exception as e:
        return protocol.error(e)

def update_analysis(uid,params):
    try:
        _sql = ""
        for key in params:
            if key == 'analysis_id':
                continue
            _sql = _sql + str(key) + " = " + escapeForSql(params[key]) + ","
        sql = query("UPDATE analyses SET " + _sql[:-1] + " WHERE analysis_id = " + str(uid) +";")
        cursor = db()
        cursor.execute(sql)
        return protocol.success("Successfully updated analysis with id "+str(uid), cursor.statusmessage)
    except Exception as e:
        return protocol.error(e)


def new_analysis(source_id,dimensions,metric,query):
    uid = None
    return protocol.success("Successfully created analysis with id "+str(uid))

def get_sources():
    try:
        sql = query("SELECT * from data_sources;")
        cursor = db()
        cursor.execute(sql)
        items = [model.DataSource(proto).toDict() for proto in cursor.fetchall()]
        return protocol.success("Successfully fetched data sources",items)
    except Exception as e:
        return protocol.error(e)

def create_source(type_of,host,port,user,password):
    try:
        sql = query("""INSERT INTO data_sources
            VALUES (DEFAULT,'{}', '{}', {}, '{}', '{}')
            RETURNING sid""".format(type_of,host,str(port),user,password))
        cursor = db()
        cursor.execute(sql)
        uid = cursor.fetchone()
        return protocol.success("Successfully created new source with id "+str(uid), cursor.statusmessage)
    except Exception as e:
        return protocol.error(e)

def update_source(uid,params):
    try:
        _sql = ""
        for key in params:
            if key == 'sid':
                continue
            _sql = _sql + str(key) + "=" + escapeForSql(params[key]) + ","
        sql = query("UPDATE data_sources SET " + _sql[:-1] + " WHERE sid = " + str(uid) +";")
        cursor = db()
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return protocol.success("Successfully updated source with id " + str(uid),cursor.statusmessage)
        else:
            return protocol.warning("Could not update data source with id "+str(uid))
    except Exception as e:
        return protocol.error(e)

def delete_source(uid):
    try:
        sql = query("DELETE from data_sources where sid ={id};".format(id=uid))
        cursor = db()
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return protocol.success("Succesfully deleted data source with id " +str(uid),cursor.statusmessage)
        else:
            return protocol.warning("Could not delete data source with id "+str(uid))
    except Exception as e:
        return protocol.error(e)

def run_query(query_id):
    #return protocol.success("Succesfully executed query with id "+str(query_id))
    return protocol.warning("Not implemented!")



