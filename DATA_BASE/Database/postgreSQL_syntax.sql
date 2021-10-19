--Give the total GDP of Africa
SELECT SUM(gdp) FROM world
WHERE continent = 'Africa';

-- Get poplulation of 3 countries
SELECT SUM(population) FROM world
WHERE 'Estonia' IN (name) OR 'Latvia' IN (name) OR 'Lithuania' IN (name);


-- GROUP BY and HAVING. The HAVING clause is tested after the GROUP BY. You can test the aggregated values with 
-- a HAVING clause. Show the total population of those continents with a total population of at least half a billion.
SELECT continent, SUM(population)
    FROM world
    GROUP BY continent
    HAVING SUM(population)>500000000