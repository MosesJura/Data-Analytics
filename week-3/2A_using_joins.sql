-- Moses Jura
-- 10/27/2026
-- 2.A Using JOINs

USE northwind;
SELECT database();
SHOW tables;

-- 1. Product id, name, unit price, category name. Order by category, then product.
SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName 
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- 2. Product id, name, unit price, supplier name. Cost > $75. Order by product name.

SELECT p.ProductID, p.ProductName,p.UnitPrice,s.CompanyName 'Supplier Name'
 FROM products p
 JOIN Suppliers s ON p.SupplierID  = s.SupplierID
 WHERE p.UnitPrice > 75 
 ORDER BY p.ProductName;
 
 -- 3. Product id, name, unit price, category name, supplier name. Order by product name.
 SELECT p.ProductID, p.ProductName, p.UnitPrice, 
	    c.CategoryName, s.CompanyName 'Supplier Name'
FROM Products p
JOIN Categories c ON p.CategoryID = c.CategoryID
JOIN Suppliers s ON p.SupplierID  = s.SupplierID
ORDER BY p.ProductName;
 
 -- 4. Order id, ship name, ship address, shipper name (alias 'Shipper'). 
 -- Shipped to Germany. Order by shipper then name.
 SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName Shipper 
 FROM orders o
 JOIN shippers s ON s.ShipperID = o.ShipVia
 WHERE o.ShipCountry = 'Germany'
 ORDER BY s.CompanyName, o.ShipName;
 
 -- 5. Same as #4, but omit OrderID and group by ShipName with a count of orders.
SELECT o.ShipName, s.CompanyName AS Shipper, COUNT(o.OrderID) AS OrderCount
FROM Orders o
JOIN Shippers s ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY o.ShipName, s.CompanyName
ORDER BY s.CompanyName, o.ShipName;

-- 6. Order id, order date, ship name, ship address of orders that included Sasquatch Ale.
-- (Requires joining Orders, Order Details, and Products. Note the backticks for the table name with a space).
SELECT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM Orders o
JOIN `Order Details` od ON o.OrderID = od.OrderID
JOIN Products p ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';
 



