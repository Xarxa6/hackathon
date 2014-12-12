-- create analyse table statement
CREATE TABLE analyses (
	analysis_id SERIAL,
	tags json,
	payload json,
	status text
);

-- create data_sources table statement
create table data_sources (
  sid serial,
  type text,
  host text,
  port integer,
  username text,
  password text
);
