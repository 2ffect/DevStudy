-- Active: 1744076829973@@127.0.0.1@3306
# 1. 
SELECT * FROM artists;

# 2.
SELECT COUNT(ArtistID) FROM artists;

# 3.
SELECT Name From artists WHERE Name = 'AC/DC';

# 4.
SELECT Name FROM artists;

# 5.
SELECT * FROM artists WHERE Name IN ('Gilberto Gil', 'Ed Motta');

# 6.
SELECT * FROM artists ORDER BY Name DESC;

# 7.
SELECT * FROM artists WHERE Name LIKE 'Vinícius%' LIMIT 2;

# 8.
SELECT ArtistId FROM artists WHERE ArtistId BETWEEN 50 AND 70;