USE northwind;
/*

What is the name of the table that holds the items Northwind sells?
categories, customercustomerdemo, customerdemographics, customers, employees, employeeterritones,
 orderdetails, orders, products, region, shippers, suppliers, territories


What is the name of the table that holds the types/categories of the items
Northwind sells?
/*
-- Who is the Northwind employee whose name makes it look like she’s a bird? " Peacock Margaret "

SELECT * FROM employees  -- to retrieve all columns from the employees table.
-- Peacock Margaret 
-----------------------------------------------------------------------------------------------------
SELECT * FROM products;  -- retrieve all columns from the products table

-- 77 rows record found , you can set a limit to 10 rows using tool bar

SELECT * FROM products LIMIT 10; -- -- This returns only the first 10 rows of the result set.
------------------------------------------------------------------------------------------------------------

SELECT * FROM categories   -- to retrieve all columns from the categories table
WHERE categoryName = 'seafood';  -- when i use where to filter and get seafood

=======================================================================================================

SELECT  OrderID, OrderDate, ShipName, ShipCountry FROM orders
 --to retrieve the top 50 records from orders









