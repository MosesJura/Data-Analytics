-- Moses Jura
-- 10/26/2026
-- 1.B Querying a database

USE northwind;
SELECT database();
SHOW tables;

-- 1. query to list the product id, product name, and unit price of every product
SELECT * FROM products;
SELECT productid, productname, unitprice
FROM products; 

-- 2. products where the unit price is $7.50 or less
SELECT productid, productname, unitprice
FROM products
WHERE unitprice <= 7.50 ; 

-- 3. Products with no units on hand, but 1 or more units on backorder.
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder 
FROM Products 
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;

-- 4. Examine products table. How identify category? Where find list of categories? 
-- List all Seafood items.
-- (The Products table uses CategoryID. The Categories table has the names).
-- (To find Seafood ID: SELECT * FROM Categories WHERE CategoryName = 'Seafood'; It is ID 8)
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM Products
WHERE CategoryID = (
    SELECT CategoryID 
    FROM Categories 
    WHERE CategoryName = 'Seafood');

-- 5. How know supplier? Find ID for "Tokyo Traders", then find all products.
-- (To find Supplier ID: SELECT SupplierID FROM Suppliers WHERE CompanyName = 'Tokyo Traders'; It is ID 4)
SELECT * FROM suppliers
WHERE companyname = 'Tokyo Traders';
SELECT ProductID, ProductName
FROM Products
WHERE SupplierID = (
    SELECT SupplierID FROM suppliers
WHERE companyname = 'Tokyo Traders');

-- 6. How many employees work at northwind? What employees have "manager" in title?
SELECT *
FROM Employees;

SELECT COUNT(employeeID) TotalEmployees
FROM Employees;

SELECT FirstName, LastName, Title 
FROM Employees 
WHERE Title LIKE '%manager%';

