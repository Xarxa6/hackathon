CREATE DATABASE xarxa6;
CREATE USER api with PASSWORD '1234';
CREATE TABLE analyses (analysis_id SERIAL,tags json,payload json,status text);
CREATE TABLE data_sources (sid serial,type text,host text,port integer,username text,password text);
GRANT ALL ON analyses TO api;
GRANT ALL ON data_sources TO api;
GRANT USAGE, SELECT ON SEQUENCE analyses_analysis_id_seq TO api;
