-- inserting into the analyse table a request for analysis (when the user doesn't find the analysis they wanted)

INSERT INTO analyses VALUES (DEFAULT, '[{"request": "i would like to see the uptime last month, thanks!"}]', '{"query":"not specified"}', 'queued');


