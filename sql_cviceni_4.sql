--Která města mají v názvu „aa“?
SELECT DISTINCT
    City
FROM
    Country
WHERE
    City LIKE '%aa%'

-- Kolik jsme vydělali ve 45. týdnu roku 2014?
SELECT DISTINCT
    SUM(Revenue)
FROM
    Sales
WHERE
    DATEPART(WEEK, Date) = 45 AND 
    YEAR(Date) = 2014

-- Ve kterém regionu je nejvíce států?
SELECT TOP 1 WITH TIES
	Region,
	COUNT(DISTINCT State) AS States
FROM
	Country
GROUP BY
	Region
ORDER BY
	States DESC

-- vypiste prodeje s nejnizsi trzbou
SELECT TOP 1 WITH TIES
    Revenue
FROM
	Sales
WHERE
    Revenue IS NOT NULL
ORDER BY
	Revenue ASC

-- Který produkt (ProductID) má nejvyšší průměrný počet kusů v rámci jednoho prodeje, 
-- pokud uvažujeme jen faktury s částkou vyšší než 10000?

SELECT TOP 1 WITH TIES
    ProductID,
    AVG(Units) AS AvgUnits
FROM
    Sales
WHERE
    Revenue > 1000
GROUP BY
    ProductID
ORDER BY
    AvgUnits DESC


--Ve kterých letech jsme na Floridě vydělali přes 10 000 000?    
SELECT
    YEAR(Date),
    SUM(Revenue) AS TotalRevenue
FROM
    Sales s
    JOIN Country c ON c.Zip = s.Zip
WHERE
    c.State = N'FL'
GROUP BY
    YEAR(Date)
HAVING
    SUM(Revenue)> 10000000


-- Které výrobky se nikdy neprodávaly?
SELECT
    *
FROM
    Sales s
    RIGHT JOIN Product p ON p.ProductID = s.ProductID
WHERE
    s.ProductID IS NULL
 
-- nebo
SELECT
	Product
FROM
	Product p
	LEFT JOIN Sales s ON s.ProductID = p.ProductID
WHERE
	s.ProductID IS NULL

--Kolik výrobků řady UM se prodalo v roce 2013?

SELECT
	SUM(Units)
FROM
	Sales s
    JOIN Product p ON p.ProductID = s.ProductID
WHERE
	Product LIKE N'% UM-%' AND
    YEAR(Date) = 2013

