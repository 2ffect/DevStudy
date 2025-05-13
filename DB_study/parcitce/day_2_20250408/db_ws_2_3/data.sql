-- Active: 1744080363031@@127.0.0.1@3306

SELECT * FROM hotels

UPDATE hotels SET grade = upper(grade);

SELECT grade FROM hotels

CREATE TABLE reservations (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER NOT NULL,
  room_num TEXT NOT NULL,
  check_in TEXT,
  check_out TEXT,
  Foreign Key (customer_id) REFERENCES customers(id),
  Foreign Key (room_num) REFERENCES hotels(room_num)
);

CREATE TABLE customers (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT
);

INSERT INTO customers (name, email)
VALUES ('홍길동', 'rlfehd@example.com'),
('박지영', 'wldud@example.com'),
('김미영', 'aldud@example.com'),
('이철수', 'cjftn@example.com');

INSERT INTO reservations (customer_id, room_num, check_in, check_out)
VALUES (1, '101', '2024-03-20', '2024-03-25'),
(2, '202', '2024-03-21', '2024-03-24'),
(3, '303', '2024-03-22', '2024-03-26'),
(4, '404', '2024-03-23', '2024-03-27');

SELECT * FROM reservations;
SELECT * FROM customers;