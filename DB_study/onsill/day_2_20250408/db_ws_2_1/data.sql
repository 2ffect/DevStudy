-- Active: 1744079510164@@127.0.0.1@3306
CREATE TABLE zoo (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  eat TEXT,
  weight INT,
  height INT,
  age INT
);

DROP TABLE zoo

INSERT INTO zoo (name, eat, weight, height, age)
VALUES ('Lion', 'Meat', 200, 120, 5),
('Elephant', 'Plants', 5000, 300, 15),
('Giraffe', 'Leaves', 1500, 550, 10),
('Monkey', 'Fruits', 50, 60, 8);

SELECT * FROM zoo;