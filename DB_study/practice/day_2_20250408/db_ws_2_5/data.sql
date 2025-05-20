-- Active: 1744086296966@@127.0.0.1@3306

SELECT departments.name, employees.name AS oldest_employee, MAX(employees.age) AS max_age, AVG(employees.age) AS avg_age
FROM departments INNER JOIN employees ON departments.id = employees.departmentId GROUP BY departments.name;

SELECT departments.name, employees.name AS highest_paid_employee, MAX(employees.salary) AS max_salary
FROM departments INNER JOIN employees ON departments.id = employees.departmentId GROUP BY departments.name;

SELECT departments.name, CASE WHEN employees.age < 30 THEN 'UNDER 30' WHEN employees.age BETWEEN 30 AND 40 THEN 'BETWEEN 30 ~ 40'
ELSE 'OVER 40' END AS age_group, COUNT(*) AS num_employees
FROM departments INNER JOIN employees ON departments.id = employees.departmentId GROUP BY departments.name;

SELECT departments.name,  (SUM(employees.salary) - MAX(employees.salary)) / (COUNT(*) - 1) AS avg_salary_excluding_hightest
FROM departments INNER JOIN employees ON departments.id = employees.departmentId GROUP BY departments.name;

