-- Active: 1743993957279@@127.0.0.1@3306

# 1.
SELECT * FROM users WHERE age < 18 ORDER BY age DESC;

# 2.
SELECT last_name, age FROM users WHERE age < 18 ORDER BY last_name, age DESC;

# 3.
SELECT last_name, age FROM users WHERE age < 18 GROUP BY last_name ORDER BY last_name, age DESC;