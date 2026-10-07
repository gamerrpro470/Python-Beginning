-- FINAL ASSESSMENT 

-- Part 1: Database and Table

create database RestaurantDB;
use RestaurantDB;
show databases;

-- task 2 and 3:
create table MenuItems (
ItemId INT Primary Key AUTO_INCREMENT,
ItemName VARCHAR(100) NOT NULL,
ItemCode VARCHAR(20) UNIQUE,
Category VARCHAR(40),
Price INT CHECK (Price > 0),
Stock INT,
Status VARCHAR(20) DEFAULT 'Available',
addedDate DATE 
);
show tables;
describe MenuItems;

-- Part 2: insert data
-- task 4

INSERT INTO MenuItems (ItemName, ItemCode, Category, Price, Stock, Status, AddedDate) 
VALUES ('Chicken Biryani', 'R101', 'Rice', 450.00, 30, 'Available', '2024-01-10'),
 ('Beef Pulao', 'R102', 'Rice', 400.00, 25, 'Available', '2024-02-15'),
 ('Chicken Tikka', 'B103', 'BBQ', 650.00, 20, 'Available', '2024-03-01'),
 ('Seekh Kabab', 'B104', 'BBQ', 550.00, 0, 'Out of Stock', '2023-11-20'),
 ('Zinger Burger', 'F105', 'Fast Food', 380.00, 40, 'Available', '2024-04-05'),
 ('Club Sandwich', 'F106', 'Fast Food', 320.00, 35, 'Available', '2024-05-12'),
 ('French Fries', 'F107', 'Fast Food', 250.00, 50, 'Available', '2023-08-18'),
 ('Cold Drink', 'D108', 'Drinks', 80.00, 100, 'Available', '2024-06-25'),
 ('Mint Margarita', 'D109', 'Drinks', 180.00, 0, 'Out of Stock', '2024-07-30'),
 ('Kheer', 'S110', 'Dessert', 150.00, 15, 'Available', '2024-08-14'); 
select * from MenuItems;

-- task 5
INSERT INTO MenuItems (ItemName, ItemCode, Category, Price, Stock, Status, AddedDate) 
VALUES ('Gulab Jamun' , 'S111' , 'Dessert' , 120 , 22 , ' 2024-09-01');
select * from MenuItems;

-- Part 3: SELECT Queries
-- task 6
-- 6.1 
select * from MenuItems;
-- 6.2
select ItemName , Category , Price from MenuItems;
-- 6.3
select * from MenuItems
where Price > 400; 
-- 6.4
select * from MenuItems
where Category in ('RICE' , 'BBQ'); 
-- 6.5
select * from MenuItems
where Price between 300 and 500;
-- 6.6
select * from MenuItems
where ItemName like 'C%';
-- 6.7
select * from MenuItems
where Category not in ('FAST FOOD');
-- 6.8
select * from MenuItems
where Category in ('BBQ') AND Price > 600; 
-- 6.9
select ItemName , Price from MenuItems
order by Price desc;
-- 6.10
select ItemName , Price from MenuItems
order by Price desc
limit 3;

-- Part 4: Update, Delete and Alter 
-- task 7
-- 7.1
update MenuItems
set Price = 700
where ItemName = 'Chicken Tikka'; 
-- 7.2
update MenuItems
set Stock = 20 , Status = 'Availible'
where ItemId = 4;
-- 7.3
update MenuItems
set Price = 200
where ItemName = 'Mint Margarita';
-- 7.4
delete from MenuItems
where ItemName = 'Gulab Jamun';
-- 7.5
alter table MenuItems add Discount int;
-- 7.6
alter table MenuItems modify Category VARCHAR(60);
-- 7.7
alter table MenuItems
drop column Discount;
select * from MenuItems;

-- Part 5: Aggregate Functions and Grouping
-- task 8
-- 8.1
select COUNT(*) as total_items 
from MenuItems;
-- 8.2
select SUM(Stock) as total_stock 
from MenuItems;
-- 8.3
select AVG(Price) as average_price 
from MenuItems;
-- 8.4
select MAX(Price) as most_expensive, 
       MIN(Price) as cheapest 
from MenuItems;
-- 8.5
select Category, COUNT(*) as total_quantity
from MenuItems
group by Category;
-- 8.6
select AVG(Price) as total_price
from MenuItems
group by Category;
-- 8.7
select Category, COUNT(*) as total_quantity
from MenuItems
group by Category
having COUNT(*) > 2;

-- Part 6: Debugging 
-- task 9
-- 9.1
SELECT * FROM MenuItems; 
-- 9.2
SELECT Category, COUNT(*) AS total_quantity FROM MenuItems GROUP BY Category HAVING COUNT(*) > 2;
-- 9.3
INSERT INTO MenuItems (ItemName, Price) VALUES ('Pizza', 900); 





 