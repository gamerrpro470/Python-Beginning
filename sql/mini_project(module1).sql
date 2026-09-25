-- MINI PROJECT 
CREATE DATABASE student_system;
USE student_system;
CREATE TABLE students(
student_id int,
name varchar(50),
age int,
city varchar(30),
admission_date date
);
INSERT INTO students(student_id , name , age , city , admission_date)
VALUES( 01 , "Muhammad Isaam" , 14 , "Karachi" , '2023-03-15' );
INSERT INTO students(student_id , name , age , city , admission_date)
VALUES( 02 , "Nameer Rustam" , 14 , "Karachi" , '2023-05-17' );
INSERT INTO students(student_id , name , age , city , admission_date)
VALUES( 03 , "Muhammad Arham" , 14 , "Karachi" , '2023-01-11' );
INSERT INTO students(student_id , name , age , city , admission_date)
VALUES( 04 , "Muhammad Ahmed" , 14 , "Karachi" , '2023-11-05' );
INSERT INTO students(student_id , name , age , city , admission_date)
VALUES( 05 , "Muhammad Afaan" , 14 , "Karachi" , '2023-02-01' );
select * from students;

select * from students
WHERE city = "Karachi";



