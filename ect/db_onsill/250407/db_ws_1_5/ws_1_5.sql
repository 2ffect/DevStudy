-- Active: 1743999120545@@127.0.0.1@3306

# 1.
SELECT * FROM users WHERE age >= 30 and balance >= 1000;

# 2.
SELECT * FROM users WHERE balance <= 1000 and age <= 20;

# 3.
SELECT * FROM users WHERE first_name LIKE '현%' and country = '제주특별자치도' 
ORDER BY age DESC LIMIT 1;

# 4.
SELECT * FROM users WHERE last_name LIKE '%박' and age >= 25
ORDER BY age LIMIT 1;

# 5.
SELECT * FROM users WHERE first_name IN ('재은', '영일') ORDER BY balance DESC LIMIT 1;

# 6.
SELECT first_name, last_name, age, phone, country, MAX(balance) AS max_balance FROM users
GROUP BY country ORDER BY max_balance DESC;

# 7.
SELECT first_name, last_name, age, phone, country, balance FROM users WHERE age >= 30 
AND balance > (SELECT AVG(balance) FROM users WHERE age >= 30);