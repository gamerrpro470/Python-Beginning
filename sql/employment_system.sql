-- Part 1: Database and Table
-- Task 1
CREATE DATABASE EmployeeDB;
USE EmployeeDB;
SHOW DATABASES;

-- Task 2
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY AUTO_INCREMENT,
    FullName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    Department VARCHAR(40),
    City VARCHAR(50),
    Salary DECIMAL(10,2) CHECK (Salary > 0),
    Status VARCHAR(20) DEFAULT 'Active',
    JoinDate DATE
);

-- Task 3
SHOW TABLES;
DESCRIBE Employees;

-- Part 2: Insert Data
-- Task 4
INSERT INTO Employees (FullName, Email, Department, City, Salary, Status, JoinDate) VALUES
('Ali Raza', 'ali.raza@company.com', 'IT', 'Karachi', 85000.00, 'Active', '2024-01-10'),
('Sara Khan', 'sara.khan@company.com', 'HR', 'Lahore', 60000.00, 'Active', '2024-02-15'),
('Ahmed Hussain', 'ahmed.hussain@company.com', 'Sales', 'Karachi', 55000.00, 'Active', '2024-03-01'),
('Fatima Noor', 'fatima.noor@company.com', 'Finance', 'Islamabad', 95000.00, 'Active', '2023-11-20'),
('Bilal Sheikh', 'bilal.sheikh@company.com', 'IT', 'Hyderabad', 70000.00, 'On Leave', '2024-04-05'),
('Ayesha Malik', 'ayesha.malik@company.com', 'Sales', 'Lahore', 48000.00, 'Active', '2024-05-12'),
('Usman Tariq', 'usman.tariq@company.com', 'IT', 'Karachi', 120000.00, 'Active', '2023-08-18'),
('Hina Aslam', 'hina.aslam@company.com', 'HR', 'Karachi', 52000.00, 'On Leave', '2024-06-25'),
('Zain Abbas', 'zain.abbas@company.com', 'Finance', 'Lahore', 78000.00, 'Active', '2024-07-30'),
('Maryam Siddiqui', 'maryam.siddiqui@company.com', 'Sales', 'Islamabad', 65000.00, 'Active', '2024-08-14');

-- Task 5
INSERT INTO Employees (FullName, Email, Department, City, Salary, JoinDate) 
VALUES ('Asad Mehmood', 'asad.mehmood@company.com', 'IT', 'Karachi', 75000.00, '2024-09-01');

SELECT * FROM Employees WHERE FullName = 'Asad Mehmood';

-- Part 3: SELECT Queries
-- Task 6.1
SELECT * FROM Employees;

-- Task 6.2
SELECT FullName, Department, Salary FROM Employees;

-- Task 6.3
SELECT * FROM Employees WHERE Salary > 60000;

-- Task 6.4
SELECT * FROM Employees WHERE City IN ('Karachi', 'Lahore');

-- Task 6.5
SELECT * FROM Employees WHERE Salary BETWEEN 50000 AND 80000;

-- Task 6.6
SELECT * FROM Employees WHERE FullName LIKE 'A%';

-- Task 6.7
SELECT * FROM Employees WHERE NOT City = 'Karachi';

-- Task 6.8
SELECT * FROM Employees WHERE Department = 'IT' AND Salary > 70000;

-- Task 6.9
SELECT * FROM Employees ORDER BY Salary DESC;

-- Task 6.10
SELECT * FROM Employees ORDER BY Salary DESC LIMIT 3;

-- Part 4: Update, Delete and Alter
-- Task 7.1
SELECT * FROM Employees WHERE FullName = 'Fatima Noor';
UPDATE Employees SET Salary = 100000.00 WHERE FullName = 'Fatima Noor';

-- Task 7.2
SELECT * FROM Employees WHERE EmpID = 5;
UPDATE Employees SET Status = 'Active' WHERE EmpID = 5;

-- Task 7.3
SELECT * FROM Employees WHERE FullName = 'Hina Aslam';
UPDATE Employees SET City = 'Lahore' WHERE FullName = 'Hina Aslam';

-- Task 7.4
SELECT * FROM Employees WHERE FullName = 'Asad Mehmood';
DELETE FROM Employees WHERE FullName = 'Asad Mehmood';

-- Task 7.5
ALTER TABLE Employees ADD Bonus DECIMAL(8,2);

-- Task 7.6
ALTER TABLE Employees MODIFY Department VARCHAR(60);

-- Task 7.7
ALTER TABLE Employees DROP COLUMN Bonus;

-- Part 5: Constraints Test
-- Task 8.1
INSERT INTO Employees (FullName, Email, Department, City, Salary, JoinDate) 
VALUES ('Test User 1', 'ali.raza@company.com', 'IT', 'Karachi', 50000.00, '2024-10-01');

-- Task 8.2
INSERT INTO Employees (FullName, Email, Department, City, Salary, JoinDate) 
VALUES ('Test User 2', 'test2@company.com', 'IT', 'Karachi', 0.00, '2024-10-01');

-- Task 8.3
INSERT INTO Employees (FullName, Email, Department, City, Salary, JoinDate) 
VALUES (NULL, 'test3@company.com', 'IT', 'Karachi', 45000.00, '2024-10-01');

-- Part 6: Aggregate Functions and Grouping
-- Task 9.1
SELECT COUNT(*) AS TotalEmployees FROM Employees;

-- Task 9.2
SELECT SUM(Salary) AS TotalSalaryInvestment FROM Employees;

-- Task 9.3
SELECT AVG(Salary) AS AverageSalary FROM Employees;

-- Task 9.4
SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary FROM Employees;

-- Task 9.5
SELECT Department, COUNT(*) AS EmployeeCount FROM Employees GROUP BY Department;

-- Task 9.6
SELECT City, AVG(Salary) AS AverageSalaryByCity FROM Employees GROUP BY City;

-- Task 9.7
SELECT Department, COUNT(*) AS EmployeeCount FROM Employees GROUP BY Department HAVING COUNT(*) > 2;
