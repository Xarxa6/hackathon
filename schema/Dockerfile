# DB Dockerfile
FROM postgres:9.4

EXPOSE 5432

RUN apt-get update -y
RUN apt-get -y install sudo

# Insert the configuration script and the schema file in the container
ADD ./psql_init.sh /docker-entrypoint-initdb.d/
ADD ./schema.sql /tmp/
