
-- Moses Jura
-- 10/29/2026
-- 4.A Using JOINs

USE northwind;
SELECT database();
SHOW tables;

-- 1. Product name(s) of the most expensive products.
SELECT ProductName, UnitPrice 
FROM Products 
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- 2. Product name(s) and categories of the least expensive products.
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- 3. Order id, shipping name, address of all orders shipped via "Federal Shipping".
-- (You don't need to display the shipper name in the final results).
SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = (SELECT ShipperID FROM Shippers WHERE CompanyName = 'Federal Shipping');

-- 4. Order ids of orders that included "Sasquatch Ale".
SELECT OrderID
FROM `Order Details`
WHERE ProductID = (SELECT ProductID FROM Products WHERE ProductName = 'Sasquatch Ale');

-- 5. Name of the employee that sold order 10266.
SELECT CONCAT(FirstName, ' ', LastName) AS EmployeeName
FROM Employees
WHERE EmployeeID = (SELECT EmployeeID FROM Orders WHERE OrderID = 10266);

-- 6. Name of the customer that bought order 10266.
-- (The Orders table has CustomerID. We use that to find the CompanyName in Customers).
SELECT CompanyName
FROM Customers
WHERE CustomerID = (SELECT CustomerID FROM Orders WHERE OrderID = 10266);