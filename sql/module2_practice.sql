CREATE DATABASE company;
USE company;
CREATE TABLE employee(
employee_id int,
employee_name varchar(50),
employee_salary int 
);
INSERT INTO employee ( employee_id , employee_name , employee_salary )
values ( 01 , "Ahmed" , 90000);
INSERT INTO employee ( employee_id , employee_name , employee_salary )
values ( 02 , "Ali" , 98000);
INSERT INTO employee ( employee_id , employee_name , employee_salary )
values ( 03 , "Daud" , 87000);
INSERT INTO employee ( employee_id , employee_name , employee_salary )
values ( 04 , "Shariq" , 70000);
INSERT INTO employee ( employee_id , employee_name , employee_salary )
values ( 05 , "Abdullah" , 74000);

select * from employee;
USE company; 
UPDATE employee
SET employee_salary = 100000
WHERE employee_name = "Ahmed";
select * from employee;

DELETE from employee
WHERE employee_name = "Abdullah";
select * from employee;
ALTER TABLE employee ADD employee_status varchar(50);
select * from employee;

UPDATE employee
SET employee_status = "active" 
WHERE employee_name = "Ali";
UPDATE employee
SET employee_status = "inactive" 
WHERE employee_name = "Shariq";
UPDATE employee
SET employee_status = "active" 
WHERE employee_name = "Daud";
UPDATE employee
SET employee_status = "active" 
WHERE employee_name = "Ahmed";
select * from employee;











