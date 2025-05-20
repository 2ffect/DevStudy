-- Active: 1743992052757@@127.0.0.1@3306

# 1.
SELECT * FROM tracks;

# 2.
SELECT Name, Milliseconds, UnitPrice From tracks;

# 3.
SELECT * FROM tracks WHERE GenreId == 1;

# 4.
SELECT * FROM tracks ORDER BY Name;

# 5.
SELECT * FROM tracks LIMIT 10;