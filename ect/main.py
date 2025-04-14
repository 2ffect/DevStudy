-- 01. Querying data
SELECT 
  LastName
FROM
  employees;

SELECT
  LastName, FirstName
FROM
  employees;

SELECT
  FirstName AS '이름'
FROM
  employees;
  
SELECT
  Name, Milliseconds / 60000 AS '재생시간 (분)'
FROM
  tracks;

SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks;


-- 02. Sorting data
SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;

SELECT Country, City FROM customers
ORDER BY Country DESC, City ;

SELECT Name, Milliseconds / 60000 AS '재생 시간 (분)' FROM tracks
ORDER BY Milliseconds DESC;

-- NULL 정렬 예시
SELECT 
  postalCode
FROM
  customers
ORDER BY
  postalCode;

-- 03. Filtering data
SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City == 'Prague';

SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL AND Country == 'USA';

SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL OR Country == 'USA';

SELECT Name, Bytes FROM tracks
WHERE
  Bytes BETWEEN 10000 AND 500000
ORDER BY
  Bytes;

SELECT LastName, FirstName, Country From customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');

SELECT LastName, FirstName From customers
WHERE
  LastName LIKE '%son';

SELECT LastName, FirstName From customers
WHERE
  FirstName LIKE '___a';

SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC
LIMIT 3, 4;

-- 04. Grouping data
SELECT
  Country, COUNT(*) AS '나라 별 고객 수'
FROM
  customers
GROUP BY
  Country;
