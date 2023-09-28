SELECT movies.title, ratings.rating FROM movies
JOIN ratings ON movies.id = ratings.movie_id
ORDER BY ratings.rating DESC, movies.title;