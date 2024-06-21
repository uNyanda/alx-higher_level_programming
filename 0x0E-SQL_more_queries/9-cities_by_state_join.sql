-- This script lists all cities contained in the database hbtn_0d_usa.
-- only allowed to use one SELECT.

-- First: select the data to be displayed from the 'cities' and 'states' tables.
SELECT cities.id, cities.name, states.name

-- The main table we're working with.
FROM cities

-- Join with 'states' where 'state_id' in 'cities' matches 'id' in 'states'.
INNER JOIN states ON cities.state_id = states.id

-- Sort the results by 'cities.id' in ascending order (small to big).
ORDER BY cities.id ASC;
