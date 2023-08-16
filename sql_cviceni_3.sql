--kolik je v tabulce netflix hororu
SELECT
    COUNT(*)
FROM
    netflix
WHERE
    listed_in LIKE N'%Horror%'

--Jaky je nejstarsi film
SELECT TOP 1 WITH TIES
	*
FROM
	netflix
ORDER BY
	release_year ASC

--Ze kterého roku je v tabulce netflix nejvíce filmů?
SELECT TOP 1 WITH TIES
	release_year,
	COUNT(DISTINCT show_id) AS Cnt
FROM
	netflix
WHERE
    type = N'Movie'
GROUP BY
	release_year
ORDER BY
	Cnt DESC


--Vypište 100 nejdelších snímků (mimo seriály)
SELECT TOP 100
	runtimeMinutes/60, *
FROM
	imdb_titles
WHERE
    titleType NOT LIKE N'%Serie%'
ORDER BY
	runtimeMinutes DESC    

--Jaký je nejlépe hodnocený sci-fi film?
SELECT TOP 20
	*
FROM
	imdb_titles it
	JOIN imdb_ratings ir ON it.tconst = ir.tconst
WHERE
	titleType = N'movie' AND
	genres LIKE N'%Sci-fi%'
ORDER BY
	ir.averageRating DESC

-- Kolik je v imdb datech nehodnocených filmů?

SELECT
	COUNT(DISTINCT it.tconst)
FROM
	imdb_titles it
	LEFT JOIN imdb_ratings ir ON it.tconst = ir.tconst
WHERE
	ir.tconst IS NULL

--Ve kterých letech vzniklo přes 5000 h filmů?   

SELECT
	startYear,
	SUM(runtimeMinutes)
FROM
	imdb_titles
WHERE
	titleType = N'movie'
GROUP BY
	startYear
HAVING
	SUM(runtimeMinutes) > 5000*60



