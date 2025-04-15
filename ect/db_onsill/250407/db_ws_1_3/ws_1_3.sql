-- Active: 1743994598735@@127.0.0.1@3306

# 1.
SELECT * FROM users WHERE first_name LIKE '하%';

# 2.
SELECT * FROM users WHERE phone LIKE '%555';

# 3.
SELECT * FROM users WHERE country LIKE '경상%';

# 4.
SELECT * FROM users WHERE country LIKE '경_남%' OR country LIKE '충_남%';