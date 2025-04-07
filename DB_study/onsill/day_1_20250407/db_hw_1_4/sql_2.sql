-- Active: 1743992485299@@127.0.0.1@3306

# 1.
SELECT * FROM tracks WHERE Name LIKE '%love%';

# 2.
SELECT * FROM tracks WHERE GenreId == 1 AND Milliseconds >= 300000 ORDER BY UnitPrice DESC;

# 3.
SELECT GenreID, COUNT(GenreID) AS TotalTracks FROM tracks GROUP BY GenreId;

# 4.
SELECT GenreID, SUM(UnitPrice) AS TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice >= 100;

