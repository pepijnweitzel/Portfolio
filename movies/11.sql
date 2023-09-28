SELECT movie_id FROM ratings
WHERE movie_id in (
    SELECT movie_id FROM stars
    WHERE person_id = (
        SELECT id FROM people
        WHERE name = 'Chadwick Boseman'
    )
)
ORDER BY rating DESC
LIMIT 5;