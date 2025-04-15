-- Active: 1743993436788@@127.0.0.1@3306

# 1.
SELECT genre, COUNT(genre) AS count, AVG(duration) AS average_duration FROM songs GROUP BY genre;

