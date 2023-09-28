SELECT movie_id FROM stars
WHERE person_id = (
    SELECT id FROM people
    WHERE name = 'Kevin Bacon' and birth = 1958
);