-- Day 1: Verified Reference Queries for LLM Debugging

-- Database 1: Chinook VIP Spending Analysis
USE Chinook;
GO

SELECT TOP 5
    c.CustomerId,
    c.FirstName + ' ' + c.LastName AS FullName,
    c.Country,
    ROUND(SUM(i.Total), 2) AS LifetimeSpend
FROM Customer c
INNER JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName, c.Country
ORDER BY LifetimeSpend DESC;
GO

-- Database 2: Northwind Inventory Stock Check
USE Northwind;
GO

SELECT TOP 5
    p.ProductName,
    c.CategoryName,
    p.UnitPrice,
    p.UnitsInStock
FROM Products p
INNER JOIN Categories c ON p.CategoryID = c.CategoryID
WHERE p.UnitsInStock > 0
ORDER BY p.UnitsInStock DESC;
GO
