SELECT * FROM Customers;
SELECT * FROM Customers ORDER BY CompanyName DESC LIMIT 15;

--! AGGREGATE FUNCTIONS
--? Select the most expensive product
SELECT MAX(UnitPrice) FROM Products;
-- ALIASING
SELECT MAX(UnitPrice) AS most_expensive_product FROM Products;

-- ?Select the least expensive product
SELECT MIN(UnitPrice) FROM Products;
-- ALIASING
SELECT MIN(UnitPrice) AS least_expensive_product FROM Products;

--? Select the average price
SELECT AVG(UnitPrice) FROM Products;
-- ALIASING
SELECT AVG(UnitPrice) AS average_price FROM Products;

--? Select the total numbers products
SELECT COUNT(*) FROM Products;
-- Aliasing
SELECT COUNT(*) AS total_products FROM Products;

--! PAGINATION
--? Select all products
SELECT * FROM Products LIMIT 0, 5;
-- Get 5 products, ordered by cheapest to highest
SELECT * FROM Products ORDER BY UnitPrice ASC LIMIT 0, 5;

--! LIKE
--? Select all products
SELECT * FROM Customers where ContactName LIKE "mar%";
SELECT * FROM Customers where ContactName LIKE "%s";
SELECT * FROM Customers where ContactName LIKE "%wa%";

--! JOINS
SELECT * FROM Customers;
SELECT * from Orders;
-- Select all orders with all the costumers
SELECT * FROM Orders JOIN Customers ON Orders.CustomerID = Customers.CustomerID where Customers.CustomerID = "VINET" LIMIT 0,2;



--! Select from multiple columns
-- Tweet elon + message with the word elon +



SELECT ProductID, ProductName, UnitPrice FROM Products ORDER BY UnitPrice ASC;
