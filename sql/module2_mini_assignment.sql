CREATE DATABASE organization;
USE organization;
CREATE TABLE staff (
staff_Id int PRIMARY KEY ,
staff_name varchar(50) ,
staff_department varchar(50) ,
staff_salary int ,
staff_email varchar(50) UNIQUE 
);
INSERT INTO staff ( staff_id , staff_name , staff_department , staff_salary , staff_email )
values ( 01 , "Ahmed" , "Finance" , 200000 , "Ahmed.123@gmail.com" );
INSERT INTO staff ( staff_id , staff_name , staff_department , staff_salary , staff_email )
values ( 02 , "Ali" , "Marketing" , 150000 , "Ali.14423@gmail.com" );
INSERT INTO staff ( staff_id , staff_name , staff_department , staff_salary , staff_email )
values ( 03 , "Umer" , "Customer Support" , 90000 , "Umer23@gmail.com" );
INSERT INTO staff ( staff_id , staff_name , staff_department , staff_salary , staff_email )
values ( 04 , "Rayyan" , "Sales" , 180000 , "Rayyan09@gmail.com" );
INSERT INTO staff ( staff_id , staff_name , staff_department , staff_salary , staff_email )
values ( 05 , "Afaan" , "Administrative" , 250000 , "Afaan.9876@gmail.com" );

select * from staff;
select staff_id , staff_name from staff
order by staff_id ASC
limit 3;

update staff
set staff_salary = 200000
where staff_name = "Afaan";

alter table staff add staff_city varchar(50);
select * from staff;

select * from staff 
where staff_salary between 150000 and 250000;

select * from staff
where staff_name like 'A%' ;

select staff_salary , COUNT(*) as totalsalary from staff
group by staff_salary 
having COUNT(*)  > 1 ;










