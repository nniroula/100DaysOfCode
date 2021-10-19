--Give the total GDP of Africa
SELECT SUM(gdp) FROM world
WHERE continent = 'Africa';

-- Get poplulation of 3 countries
SELECT SUM(population) FROM world
WHERE 'Estonia' IN (name) OR 'Latvia' IN (name) OR 'Lithuania' IN (name);