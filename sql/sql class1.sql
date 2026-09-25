CREATE DATABASE Library;
USE	Library;
CREATE TABLE Books(
Id int,
Title varchar(50),
Price int
);
show tables;
select * from Books;
INSERT INTO Books (Id , Title , Price)
VALUES (01 ,"THE CHOCOLATE FACTORY" ,1000 );

INSERT INTO Books (Id , Title , Price)
VALUES (02 ,"THE ATOMIC HABITS" ,1700 );

INSERT INTO Books (Id , Title , Price)
VALUES (03 ,"FRIENDS" ,2100 );

select * from Books;
select Title from Books;

