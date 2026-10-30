-- Moses Jura
-- 10/27/2026
-- 1.C More Querying a database

USE northwind;
SELECT database();
SHOW tables;
-- 1. query to list the product id, product name, and unit price of every product.
-- This time, display them in ascending order by price 
SELECT ProductID, ProductName, UnitPrice 
FROM Products 
ORDER BY UnitPrice ASC;

-- 2. products that we carry where we have at least 100 units on hand? 
-- Order them in descending order by price.

SELECT productID, ProductName, UnitsInStock, UnitPrice
FROM PRODUCTS
WHERE UnitsInStock >= 100 
ORDER BY UnitPrice DESC;

-- 3. Same as #2, but if prices are the same, list in ascending order by product name.
SELECT productID, ProductName, UnitsInStock, UnitPrice
FROM PRODUCTS
WHERE UnitsInStock >= 100 AND UnitsInStock = UnitsInStock 
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4. Total number of distinct customers who placed orders. Alias as CustomerCount.
SELECT COUNT(DISTINCT CustomerID) CustomerCount 
FROM orders;

-- 5. Distinct customers by country. Alias CustomerCount. Order largest to smallest. 
SELECT COUNT(DISTINCT CustomerID) CustomerCount, ShipCountry
FROM orders
GROUP BY ShipCountry
ORDER BY COUNT(DISTINCT CustomerID) DESC;

-- 6. Products with less than 25 on hand, but 1 or more on order. Order by quantity on order (high to low), then name.

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder FROM products
WHERE UnitsInStock < 25 AND UnitsOnOrder >= 1
ORDER BY QuantityPerUnit DESC, ProductName ASC ;

-- 7. Job titles in employees, with a count of how many hold each.
SELECT COUNT(EmployeeID) TotalEmployee, Title 
FROM employees
GROUP BY Title;

-- 8. Employees with monthly salary between 2000 and 2500. Order by job title.
SELECT EmployeeID, FirstName, LastName, Title,Salary
FROM employees
WHERE Salary between 2000 and 2500
ORDER BY Title;











