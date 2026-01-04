In this project I have created a submission form to enter student marks with details through a local host portal by using HTML CSS and python flask library for routing.
After that I have done feature engineering on that my sql table data.

Queries to run before inintialing "python main.py" command :-

CREATE DATABASE studentDetails;

USE studentDetails;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    course VARCHAR(100),
    semester VARCHAR(20),
    marks INT,
    result VARCHAR(10)
);

Dummy entries for the same:-

INSERT INTO students (name, course, semester, marks, result)
WITH RECURSIVE seq AS (
    SELECT 1 AS i
    UNION ALL
    SELECT i + 1 FROM seq WHERE i < 500
)
SELECT 
    CONCAT('Student_', i) AS name,
    -- Randomly assign one of 4 courses
    ELT(FLOOR(1 + (RAND() * 4)), 'Computer Science', 'Mathematics', 'Physics', 'Biology') AS course,
    -- Randomly assign one of 3 semesters
    ELT(FLOOR(1 + (RAND() * 3)), 'Fall 2024', 'Spring 2025', 'Fall 2025') AS semester,
    -- Random marks between 30 and 100
    FLOOR(30 + (RAND() * 71)) AS marks,
    -- Derived result: If marks >= 40 then 'Pass' else 'Fail'
    CASE 
        WHEN (FLOOR(30 + (RAND() * 71))) >= 40 THEN 'Pass' 
        ELSE 'Fail' 
    END AS result
FROM seq;

INSERT INTO students (name, course, semester, marks, result) VALUES
-- 1. Impossible High Scores (Data Entry Errors)
('Outlier_High_1', 'Computer Science', 'Fall 2024', 250, 'Pass'),
('Outlier_High_2', 'Mathematics', 'Spring 2025', 500, 'Pass'),
('Outlier_High_3', 'Physics', 'Fall 2025', 999, 'Pass'),

-- 2. Negative Scores (Data Entry Errors)
('Outlier_Neg_1', 'Biology', 'Fall 2024', -50, 'Fail'),
('Outlier_Neg_2', 'Mathematics', 'Spring 2025', -5, 'Fail'),

-- 3. Extreme Low Scores (Near Zero)
('Outlier_Low_1', 'Computer Science', 'Fall 2024', 1, 'Fail'),
('Outlier_Low_2', 'Physics', 'Spring 2025', 0, 'Fail'),

-- 4. Statistical Outliers (Just barely outside normal range but suspicious)
('Outlier_Stat_1', 'Biology', 'Fall 2025', 15, 'Fail'),
('Outlier_Stat_2', 'Mathematics', 'Fall 2024', 110, 'Pass'),
('Outlier_Stat_3', 'Computer Science', 'Spring 2025', 12, 'Fail');
