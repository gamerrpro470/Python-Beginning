-- debugging
-- debug1
-- SELECT * FORM Students; 
-- sol
-- SELECT * FROM Students;

-- debug2
-- CREATE TABLE Students (
--  id INT PRIMARY KEY 
--  name VARCHAR(50) 
--  ); 
-- sol
-- CREATE TABLE Students (
--  id INT PRIMARY KEY,
--  name VARCHAR(50) 
--  ); 

-- debug3
-- INSERT INTO Students (name, age) VALUES (Ali, 20); 
-- sol
-- INSERT INTO Students (name, age) VALUES ("Ali", 20);

-- debug4
-- SELECT * FROM Students WHERE name = Sara; 
-- sol
-- SELECT * FROM Students WHERE name = "Sara";

-- debug5
-- CREATE TABLE 1students (id INT); 
-- sol
-- CREATE TABLE students (id INT);
   