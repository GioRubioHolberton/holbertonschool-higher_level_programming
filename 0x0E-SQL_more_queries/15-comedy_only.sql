-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE tv_show_genres.show_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id;
