--  lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre,
COUNT(tv_show_genres.genre_id) AS 'Number of shows linked to this genre' 
FROM tv_genres 
JOIN tv_show_genres 
ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY tv_show_genres.genre_id 
ORDER BY `Number of shows linked to this genre` DESC, genre ASC;
