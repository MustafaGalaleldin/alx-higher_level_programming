-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_shows LEFT JOIN (SELECT tv_show_genres.show_id FROM tv_show_genres JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_genres.name = 'Comedy') AS COM ON tv_shows.id = COM.show_id WHERE COM.show_id IS NULL ORDER BY tv_shows.title;
