#!/bin/bash

echo "host all \"api\" 0.0.0.0/0 md5" >> /var/lib/postgresql/data/pg_hba.conf

echo "******** CREATING DOCKER DATABASE ********"

gosu postgres postgres --single <<- EOSQL
    CREATE DATABASE xarxa6;
    CREATE USER api with PASSWORD '1234';
    CREATE TABLE analyses (analysis_id SERIAL,tags json,payload json,status text);
    CREATE TABLE data_sources (sid serial,type text,host text,port integer,username text,password text);
    GRANT ALL ON analyses TO api;
    GRANT ALL ON data_sources TO api;
    GRANT USAGE, SELECT ON SEQUENCE analyses_analysis_id_seq TO api;
EOSQL
echo ""
echo "******** DOCKER DATABASE CREATED ********"
