-- Active: 1744083674246@@127.0.0.1@3306

CREATE TABLE transactions (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER NOT NULL,
  amount TEXT,
  transaction_date DATE,
  Foreign Key (user_id) REFERENCES users(id)
);

INSERT INTO transactions (user_id, amount, transaction_date)
VALUES (1, '500', '2024-03-15'),
(2, '700', '2024-03-16'),
(1, '200', '2024-03-17'),
(3, '1000', '2024-03-18');

SELECT * FROM users;

SELECT users.first_name, users.last_name, transactions.amount, transactions.transaction_date
FROM users INNER JOIN transactions
ON transactions.user_id = users.id;

SELECT users.first_name, users.last_name, transactions.amount, transactions.transaction_date
FROM users INNER JOIN transactions
ON transactions.user_id = users.id
WHERE transaction_date > '2024-03-16';

SELECT users.first_name, users.last_name, SUM(transactions.amount) AS total_amount FROM users
INNER JOIN transactions ON transactions.user_id = users.id GROUP BY users.id;

