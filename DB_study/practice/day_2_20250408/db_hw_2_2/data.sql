-- Active: 1744073426138@@127.0.0.1@3306
SELECT * FROM orders;
SELECT * FROM customers;

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_date DATE,
  total_amount REAL
);

INSERT INTO orders (order_date, total_amount)
VALUES
('2023-07-15', 50.99),
('2023-07-16', 75.5),
('2023-07-17', 30.25);

CREATE TABLE customers (
  customer_id  INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT,
  phone TEXT
);

INSERT INTO customers (name, email, phone)
VALUES
('허균', 'gjrbs@gjrbs.com', '010-9999-9999'),
('김영희', 'dudgml@gjrbs.com', '010-9999-8888'),
('이철수수', 'cjftn@gjrbs.com', '010-9999-7777');

DELETE FROM orders
WHERE order_id = 3; 

UPDATE customers
SET name = '홍길동'
WHERE customer_id = 1;

SELECT * FROM orders;
SELECT * FROM customers;
