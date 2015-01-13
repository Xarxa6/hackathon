#!/bin/bash
# This document is placed via docker/fig in the postgres container and it is executed by the container's entrypoint. It will load the schema.sql file and run all the queries.

echo -e "\n******** CREATING DOCKER DATABASE ********"

queries=`cat /tmp/schema.sql`

gosu postgres postgres --single <<- IOSQL
    CREATE DATABASE xarxa6;
IOSQL

gosu postgres postgres --single xarxa6 <<- IOSQL
    $queries
IOSQL

echo -e "\n\nExecuted queries:\n"
echo $queries

echo -e "\n******** DOCKER DATABASE CREATED ********\n"

echo -e "host all \"api\" 0.0.0.0/0 trust" >> /var/lib/postgresql/data/pg_hba.conf
