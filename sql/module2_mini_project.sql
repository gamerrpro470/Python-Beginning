-- mini project

CREATE DATABASE inventory_management;
USE inventory_management;
create table suppliers(
supplier_id int PRIMARY KEY,
name varchar(50),
city varchar(50)
);

CREATE TABLE products (
product_id int PRIMARY KEY,
name varchar(50),
price int,
stock int,
supplier_id int,
FOREIGN KEY (supplier_id) REFERENCES suppliers (supplier_id)
);

INSERT INTO suppliers (supplier_id , name , city)
VALUES (01 ,"Ahmed" , "karachi" );
INSERT INTO suppliers (supplier_id , name , city)
VALUES (02 ,"Ali" , "punjab" );
INSERT INTO suppliers (supplier_id , name , city)
VALUES (03 ,"Arham" , "sindh" );
INSERT INTO suppliers (supplier_id , name , city)
VALUES (04 ,"Daud" , "sialkot" );
INSERT INTO suppliers (supplier_id , name , city)
VALUES (05 ,"Usman" , "faisalabad" );
select * from suppliers;

INSERT INTO products ( product_id , name , price , stock , supplier_id )
VALUES (01 , "laptop" , 70000 , 70 , 01);
INSERT INTO products ( product_id , name , price , stock , supplier_id )
VALUES (02 , "gaming pc" , 200000 , 60 , 02);
INSERT INTO products ( product_id , name , price , stock , supplier_id )
VALUES (03 , "moniter" , 18000 , 75 , 03);
INSERT INTO products ( product_id , name , price , stock , supplier_id )
VALUES (04 , "mouse" , 1500 , 40 , 04);
INSERT INTO products ( product_id , name , price , stock , supplier_id )
VALUES (05 , "keyboard" , 4000 , 80 , 05);
select * from products;

update products 
set stock = 30  -- or stock - 10
where name = "gaming pc";
select * from products;
delete from products 
where product_id = 04;
select * from products;

select supplier_id , COUNT(*) as totalproducts from products
group by supplier_id
having COUNT(*)  > 0 ;

select name , price from products
order by price DESC
limit 3;








