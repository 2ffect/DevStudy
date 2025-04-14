-- Active: 1744070020666@@127.0.0.1@3306
-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);


-- 1. Insert data into table
INSERT INTO articles (title, content, createdAt) 
VALUES 
('title4', 'content4', DATE()),
('title5', 'content5', DATE()),
('title6', 'content6', DATE());

-- 2. Update data in table
UPDATE articles SET title = 'update Title' WHERE id = 1;
UPDATE articles SET title = 'update Title', content = 'update Content' WHERE id = 2;

-- 3. Delete data from table
DELETE FROM articles WHERE id = 1;

DELETE FROM articles WHERE id IN (SELECT id FROM articles ORDER BY createdAt LIMIT 2);