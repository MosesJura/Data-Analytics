-- Moses Jura
-- 10/29/2026
-- 3.A Using JOINs

USE northwind;
SELECT database();
SHOW tables;

-- 1. Find the price of the cheapest item. Then find the name of that product.
SELECT MIN(UnitPrice) AS CheapestPrice FROM Products;
SELECT ProductName, UnitPrice FROM Products WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- 2. Average price of all items. (Bonus: Round to nearest cent).
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice FROM Products;

-- 3. Price of most expensive item. Then name and supplier of that product.
SELECT MAX(UnitPrice) AS MaxPrice FROM Products;
SELECT p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM Products p
JOIN Suppliers s ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- 4. Total monthly payroll (sum of all employees' salaries).
SELECT SUM(Salary) AS TotalMonthlyPayroll FROM Employees;

-- 5. Highest and lowest salary amounts.
SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary FROM Employees;

-- 6. Name and supplier ID of each supplier and the number of items they supply.
SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductID) AS ItemCount
FROM Suppliers s
LEFT JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName;

-- 7. List of all category names and average price for items in each.
SELECT c.CategoryName, ROUND(AVG(p.UnitPrice), 2) AS AveragePrice
FROM Categories c
JOIN Products p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8. For suppliers providing at least 5 items: name and number of items.
SELECT s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM Suppliers s
JOIN Products p ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9. Products in inventory: ID, name, inventory value (UnitPrice * UnitsInStock). 
-- Sort descending by value, then product name. Leave off out-of-stock items.
SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;