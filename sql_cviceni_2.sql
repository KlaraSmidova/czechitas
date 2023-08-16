--Kterým písmenem začíná nejvíce měst?

SELECT
    LEFT(City, 1),
    COUNT(DISTINCT City) AS cities
FROM
    Country
GROUP BY
    LEFT(City, 1)
ORDER BY
    cities DESC

--Kolik se prodalo výrobků řady UM-01?
SELECT
    SUM(s.Units)
FROM
    Sales s
    JOIN Product p ON s.ProductID = p.ProductID
WHERE
    p.Product LIKE N'% UM-01%'


--Kolik jsme vydělali v jednotlivých regionech?

SELECT
    Region,
    SUM(s.Revenue) AS total_revenue
FROM
    Sales s
    JOIN Country c ON s.Zip = c.Zip
GROUP BY
    Region
ORDER BY
    total_revenue DESC

-- Který výrobce prodává v nejméně státech?
SELECT
    Manufacturer,
    COUNT(DISTINCT State) AS state_pocet
FROM
    Sales s
    JOIN Country c ON s.Zip = c.Zip
    JOIN Product p ON s.ProductID = p.ProductID
    JOIN Manufacturer m ON p.ManufacturerID = m.ManufacturerID
GROUP BY
    Manufacturer
ORDER BY
    state_pocet ASC

-- Ktere vyrobky se neprodavaji
SELECT
    *
FROM
    Product p LEFT JOIN Sales s ON p.ProductID = s.ProductID
WHERE
    s.ProductID IS NULL

-- rozdil mezi pravou a levou stranou a navazanim tabulek

SELECT
    *
FROM
    Sales s RIGHT JOIN Product p ON p.ProductID = s.ProductID
WHERE
    s.ProductID IS NULL -- musim ponechat stejny zaznam pro tabulku, aby se mi ukazalo, kde jsou chybejici hodnoty

--Kteří výrobci nemají výrobky a které výrobky nemají výrobce?  
SELECT
    *
FROM
    Product p FULL Join Manufacturer m ON m.ManufacturerID = p.ManufacturerID
WHERE
    p.ManufacturerID IS NULL OR m.ManufacturerID IS NULL

-- Na kterych zip kodech jsme nic neprodali, spojim tabulky sales a zip, abych videla kde budou null
SELECT
    *
FROM
    Country c 
    Left Join Sales s ON c.Zip = s.Zip
WHERE
    s.Zip IS NULL

--Vypište pro všechny státy město s nejvyšším ZIP kódem?
SELECT
    *
FROM
    Country c1 
    Left Join Country c2 ON c1.State = c2.State AND c1.Zip < c2.Zip
WHERE
    c2.Zip IS NULL
ORDER BY
    c1.Zip

-- Ktere vyrobky se neprodavali pred rokem 2014
SELECT
    *
FROM
    Product p 
    Left Join Sales s ON s.ProductID = p.ProductID AND s.Date < '2014-01-01'
WHERE
   s.ProductID IS NULL

SELECT
    *
FROM
    Product p
Join 

-- Ve kterém regionu jsme videlali nejvic
SELECT
    c. Region,
    SUM(Revenue) AS TotalRevenue
FROM
    Sales s 
    JOIN Country c ON s.Zip = c.Zip
GROUP BY
    c. Region
ORDER BY
   TotalRevenue DESC

-- Který výrobce videlal nejvíce celkem
SELECT
    m.Manufacturer,
    SUM(Revenue) AS TotalRevenue
FROM
    Sales s 
    JOIN Product p ON s.ProductID = p.ProductID
    JOIN Manufacturer m ON m.ManufacturerID = p.ManufacturerID
GROUP BY
    m.Manufacturer
ORDER BY
   TotalRevenue DESC

-- Kteří výrobci vidělali nejvíc v jednotlivých státech
SELECT
    m.Manufacturer,
    c.State,
    SUM(Revenue) AS TotalRevenue
FROM
    Sales s 
    JOIN Product p ON s.ProductID = p.ProductID
    JOIN Manufacturer m ON m.ManufacturerID = p.ManufacturerID
    JOIN Country c ON c.Zip = s.Zip
GROUP BY
    m.Manufacturer,
    c.state
ORDER BY
    c.State,
    TotalRevenue DESC

--Kolik bylo v jednotlivých státech měst, kde jsme v lednu 2014 nic neprodali?
SELECT
    c.State,
    COUNT(DISTINCT c.Zip) AS ZipCodes
FROM
    Country c 
    LEFT JOIN Sales s ON s.Zip = c.Zip AND MONTH(s.Date) = 1 AND YEAR(s.Date) = 2014
WHERE
    s.Zip IS NULL
GROUP BY
    c.State
ORDER BY
    ZipCodes


-- tvorba view, nelze provest, protoze nejsem vlastnik databaze, 
-- nemam k tomu práva, nelze zahrnout ORDER BY
CREATE VIEW StateManufacturerView AS
(
SELECT
    m.Manufacturer,
    c.State,
    SUM(Revenue) AS TotalRevenue
FROM
    Sales s 
    JOIN Product p ON s.ProductID = p.ProductID
    JOIN Manufacturer m ON m.ManufacturerID = p.ManufacturerID
    JOIN Country c ON c.Zip = s.Zip
GROUP BY
    m.Manufacturer,
    c.state
)

-- zkouska
SELECT
    State,
    SUM(TotalRevenue) AS TotalTotalRevenue
FROM
    StateManufacturerView
GROUP BY
    State
ORDER BY
    TotalTotalRevenue DESC

-- Ve kterych statech vydelali vyrobci nejvic subselect
SELECT
    *
FROM
    StateManufacturerView smv1
WHERE
    NOT EXISTS (
        SELECT
            *
        FROM
            StateManufacturerView smv2
        WHERE
        smv2.Manufacturer = smv1.Manufacturer AND smv1.TotalRevenue < smv2.TotalRevenue
    )

-- dalsi zpusob
SELECT
    *
FROM
    StateManufacturerView smv1
    LEFT JOIN StateManufacturerView smv2 ON smv1.Manufacturer = smv2.Manufacturer AND 
    smv1.TotalRevenue < smv2.TotalRevenue
WHERE   smv2.Manufacturer IS NULL

-- pouziti CTE, nasledujici dotaz musim spustit i s zavedenou metodou CTE, sam o sobe nefunguje
;WITH ByRegion AS
(
SELECT
	c.Region,
	SUM(s.Revenue) AS TotalRevenue
FROM
	Sales s
	JOIN Country c ON s.Zip = c.Zip
GROUP BY
	c.Region
)

SELECT
    *
FROM
    ByRegion


-- Jaký je podíl výrobců na prodejích v jednotlivých státech?
;WITH StateRevenue AS
(
SELECT
	State,
	SUM(TotalRevenue) AS TotalStateRevenue
FROM
	StateManufacturerView
GROUP BY
	State
)
SELECT
    *,
    100.0 * TotalRevenue / TotalStateRevenue AS RevenueShare
FROM
    StateManufacturerView smv
    JOIN StateRevenue sr ON smv.State = sr.State
ORDER BY
    smv.State ASC,
    smv.TotalRevenue DESC
