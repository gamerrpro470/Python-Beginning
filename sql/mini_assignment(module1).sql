-- MINI ASSIGNMENT
CREATE DATABASE Library_db;
use Library_db;
CREATE TABLE Books(
book_id int,
title varchar(50),
author varchar(50),
price int
);
INSERT INTO Books ( book_id , title , author , price )
VALUES( 01 , "The Old Man and the Sea" , "Ernest Hemingway" , 2300 );
INSERT INTO Books ( book_id , title , author , price )
VALUES( 02 , "Crime and Punishment" , "Fyodor Dostoevsky" , 1000 );
INSERT INTO Books ( book_id , title , author , price )
VALUES( 03 , "Cool Machine" , "Colson Whitehead" , 3200 );
INSERT INTO Books ( book_id , title , author , price )
VALUES( 04 , "The Keeper" , "Tana French" , 1300 );
INSERT INTO Books ( book_id , title , author , price )
VALUES( 05 , "Atmosphere" , "Taylor Jenkins Reid" , 2100 );

select * from Books;

select * from Books
WHERE price = 1000;