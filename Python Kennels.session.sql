SELECT * FROM Animal
SELECT * FROM Location

-- Find Animals by Location
SELECT
    a.id,
    a.name as animalName,
    a.breed,
    a.status,
    c.name as customerName,
    l.name as locationName
  FROM Animal as a 
  INNER JOIN Location as l ON a.location_id = l.id
  INNER JOIN Customer as c
  ON a.customer_id = c.id
  WHERE l.name = 'Nashville North'

-- this also work below with just join without inner there
SELECT
    a.id,
    a.name as animalName,
    a.breed,
    a.status,
    c.name as customerName,
    l.name as locationName
  FROM Animal as a 
  JOIN Location as l ON a.location_id = l.id
  JOIN Customer as c
  ON a.customer_id = c.id
  WHERE l.name = 'Nashville North'


-- Find Employees by location
SELECT
    a.id,
    a.name as EmployeeName,
    l.name as locationName
  FROM Employee as a join Location as l
  ON a.location_id = l.id
  WHERE l.name = 'Nashville North'

-- Find Animals by Status I have the % that when you type whatever letters then include Treatment in between will bring it .. kind search keyword
SELECT
    a.id,
    a.name as animalName,
    a.breed,
    a.status,
    l.name as locationName
  FROM Animal as a join Location as l
  ON a.location_id = l.id
  WHERE a.status like '%Treatment%'
