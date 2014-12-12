-- query to return analysis payload and analysis status
-- when at least one of the measure or dimension tags matches an existing analysis
-- in the below the input JSON is '[{"measure": "users"},{"dimension": "week"},{"dimension": "os"}]'

SELECT anly.payload, anly.status
FROM (
	SELECT at.analysis_id, count(*) AS cnt
	FROM (
		-- create table from analysis table with one tag per row
		SELECT json_array_elements(tags) AS tag, analysis_id FROM analyses
	) at
		-- create table from input with one tag per row and join
	INNER JOIN (SELECT json_array_elements('[{"measure": "users"},{"dimension": "week"},{"dimension": "os"}]') AS tag
	) it
	ON ((at.tag->>'measure' = it.tag->>'measure') or (at.tag->>'dimension' = it.tag->>'dimension'))
	GROUP BY at.analysis_id
) matched_tags
-- join back to analysis jobs table to get the payload and status (cannot group by payload as it is JSON)
INNER JOIN analyses anly ON anly.analysis_id = matched_tags.analysis_id
ORDER BY matched_tags.cnt DESC
LIMIT 100;
