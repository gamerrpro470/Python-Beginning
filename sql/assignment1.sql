create database libraryDB;
use libraryDB;
create table books (
bookid int,
title varchar(100) not null,
author varchar(60),
category varchar(40),
price int check(price > 0),
availiblecopies int check(availiblecopies >= 0 )
);
alter table books 
add primary key (bookid);

create table members (
memberid int primary key,
fullname varchar(100) not null,
email varchar(100) unique,
city varchar(50),
joindate date
);

create table borrowrecords (
borrowid int primary key,
memberid int,
bookid int,
borrowdate date,
returndate date null,
status varchar(20) default 'borrowed',
foreign key (memberid) references members (memberid),
foreign key (bookid) references books (bookid)
);

insert into books (bookid , title , author , category , price , availiblecopies)
values(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 4155, 10),
      (2, 'To Kill a Mockingbird', 'Harper Lee', 'Classic Literature', 3601, 5),
      (3, '1984', 'George Orwell', 'Dystopian', 3047, 8),
      (4, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 4432, 12),
      (5, 'A Brief History of Time', 'Stephen Hawking', 'Science', 5263, 4),
      (6, 'The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 3047, 7),
      (7, 'Sapiens', 'Yuval Noah Harari', 'History', 6094, 6),
      (8, 'Educated', 'Tara Westover', 'Biography', 4709, 9);
      
insert into members (memberid , fullname , email , city , joindate) 
values(1, 'Ahmed Ali', 'ahmed.ali@email.com', 'Karachi', '2026-01-15'),
      (2, 'Fatima Khan', 'fatima.k@email.com', 'Lahore', '2026-02-20'),
      (3, 'Muhammad Umar', 'umar.m@email.com', 'Islamabad', '2026-03-05'),
      (4, 'Ayesha Siddiqui', 'ayesha.s@email.com', 'Faisalabad', '2026-04-12'),
      (5, 'Zainab Bibi', 'zainab.b@email.com', 'Peshawar', '2026-05-19'),
	  (6, 'Bilal Ahmed', 'bilal.a@email.com', 'Quetta', '2026-06-22');
			
insert into borrowrecords (borrowid , memberid , bookid , borrowdate , returndate , status)
values(1, 1, 4, '2026-09-01', '2026-09-15', 'Returned'),
      (2, 2, 1, '2026-09-05', '2026-09-19', 'Returned'),
      (3, 3, 7, '2026-09-10', '2026-09-24', 'Returned'),
      (4, 4, 3, '2026-09-12', '2026-09-26', 'Returned'),
      (5, 5, 8, '2026-09-15', NULL, 'Borrowed'),
      (6, 6, 2, '2026-09-18', NULL, 'Borrowed'),
      (7, 1, 5, '2026-09-20', NULL, 'Borrowed'),
	  (8, 2, 3, '2026-09-22', NULL, 'Borrowed'),
      (9, 3, 6, '2026-09-25', NULL, 'Borrowed'),
      (10, 4, 1, '2026-09-28', NULL, 'Borrowed');
      
select * from books;

select * from books 
where price > 4000;

select * from books
where category = 'Fiction';

select * from members
where city = 'Karachi';

select * from books
order by price desc;

select * from books
order by price desc
limit 3;

select * from books
where availiblecopies between 2 and 5;

select * from members
where fullname like 'A%';

update books 
set availiblecopies = 7
where bookid = 1;

update books 
set availiblecopies = 4
where bookid = 8;

update members
set city = 'Islamabad'
where memberid = 1;

delete from borrowrecords
where borrowid = 8;

alter table books add publishedyear int;
select * from books;

alter table books modify category varchar(60);
select * from books; 

alter table books
drop column publishedyear;
select * from books;

select COUNT(*) as total_books 
from books;

select AVG(price) as average_price 
from books;

select 
    MAX(price) as most_expensive, 
    MIN(price) as cheapest 
from books;

select category, COUNT(*) as total_books
from books
group by category;

select city, COUNT(*) as total_members
from members
group by city;

select category, COUNT(*) as total_books
from books
group by category
having COUNT(*) > 1;

SELECT memberid, COUNT(*) AS total_borrows
from borrowrecords
group by memberid;

select * from books 
where category in ('Fiction', 'Science');

select * from books
where price between 3000 and 4000;

select * from members
where city not in ('Karachi', 'Hyderabad');

select * from books 
where title like '%Educated%';

insert into members (fullname, email) 
values ('Ahmed Farooq', 'ahmed.ali@email.com');

insert into books (price)
values (-10);

insert into borrowrecords (bookid)
values (18);

















	

    


      



