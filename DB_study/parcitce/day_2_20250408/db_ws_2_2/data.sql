-- Active: 1744079922215@@127.0.0.1@3306


ALTER TABLE zoo ADD COLUMN species TEXT NOT NULL DEFAULT ('default value');
SELECT * FROM zoo;

UPDATE zoo SET species = 'Panthera leo' WHERE name = 'Lion';
UPDATE zoo SET species = 'Loxodonta africana' WHERE name = 'Elephant';
UPDATE zoo SET species = 'Giraffa camelopardalis' WHERE name = 'Giraffe';
UPDATE zoo SET species = 'Cebus capucinus' WHERE name = 'Monkey';

UPDATE zoo SET height = height * 2.54;
SELECT * FROM zoo;