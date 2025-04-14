-- Active: 1743994867669@@127.0.0.1@3306

# 1.
SELECT AVG(age) AS average_age FROM users;

# 2.
SELECT country, COUNT(country) AS user_count FROM users GROUP BY country;

# 3.
SELECT * FROM users ORDER BY balance DESC LIMIT 1;

# 4.
SELECT country, AVG(balance) AS avg_balance FROM users GROUP BY country;

# 5.
SELECT MAX(balance) - MIN(balance) AS balance_difference FROM users;

