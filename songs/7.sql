SELECT AVG(engergy) FROM songs
WHERE artist_id = (
    SELECT id FROM artists
    WHERE name = 'Drake'
);