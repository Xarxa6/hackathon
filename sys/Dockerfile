# DB Dockerfile
FROM postgres:9.4

EXPOSE 5432

RUN apt-get update -y
RUN apt-get -y install sudo

# TODO Add schema file and run SQL from there
ADD ./psql_init.sh /docker-entrypoint-initdb.d/
