--Který výrobce prodal nejvíce kusů?
SELECT TOP 1 
    Manufacturer,
    SUM(Units) AS TotalUnits
FROM
    Manufacturer m
    JOIN Product p ON m.ManufacturerID = p.ManufacturerID
    JOIN Sales s ON p.ProductID = s.ProductID
GROUP BY
    Manufacturer
ORDER BY
    TotalUnits DESC

-- Ve kterém státě je nejvíce měst?
SELECT
    COUNT(DISTINCT City) as count_city,
    State
FROM
    Country
GROUP BY
    State
ORDER BY
    count_city DESC

--Který výrobce vydělal nejvíce na velkých prodejích (nad 10 ks)?    
SELECT 
    Manufacturer,
    SUM(Revenue) AS TotalRevenue
FROM
    Manufacturer m
    JOIN Product p ON m.ManufacturerID = p.ManufacturerID
    JOIN Sales s ON p.ProductID = s.ProductID
WHERE 
    s.Units > 10
GROUP BY
    Manufacturer
ORDER BY
    TotalRevenue DESC   

-- Za které výrobky jsme v roce 2014 utržili alespoň 10 milionů?
SELECT 
    Product,
    SUM(Revenue) AS TotalRevenue
FROM
    Product p
    JOIN Sales s ON p.ProductID = s.ProductID
WHERE
    YEAR(Date) = 2014
GROUP BY
    Product
HAVING 
    SUM(Revenue) > 10000000
ORDER BY
    TotalRevenue DESC

--Na kterých ZIP kódech se nic neprodalo?
SELECT 
    *
FROM
    Country c
    LEFT JOIN Sales s ON c.Zip = s.Zip
WHERE
    s.Zip is NULL
