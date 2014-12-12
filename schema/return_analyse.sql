-- query to return analysis payload and analysis status
-- when at least one of the measure or dimension tags matches an existing analysis
-- in the below the input JSON is '[{"measure": "users"},{"dimension": "week"},{"dimension": "os"}]'

SELECT anly.payload, anly.status
FROM (
	SELECT at.analysis_id, count(*) AS cnt
	FROM (
		SELECT json_array_elements(tags) AS tag, analysis_id FROM analyses
	) at
	INNER JOIN (SELECT json_array_elements('[{"measure": "users"},{"dimension": "week"},{"dimension": "os"}]') AS tag
	) it
	ON ((at.tag->>'measure' = it.tag->>'measure') or (at.tag->>'dimension' = it.tag->>'dimension'))
	GROUP BY at.analysis_id
) matched_tags
INNER JOIN analyses anly ON anly.analysis_id = matched_tags.analysis_id
ORDER BY matched_tags.cnt DESC
LIMIT 100;
