.read lab12.sql

-- Q5
CREATE TABLE greatstudents AS
  SELECT a.date, a.color, a.pet, a.number, b.number
    FROM students AS a, fa17students AS b
    WHERE a.date = b.date AND a.color = b.color AND a.pet = b.pet;

-- Q6
CREATE TABLE sevens AS
  SELECT a.seven 
    FROM students AS a, checkboxes AS b
    WHERE a.number = 7 AND b.'7' = 'True' AND a.time = b.time;

-- Q7
CREATE TABLE fa17favnum AS
  SELECT number, COUNT(*) FROM fa17students GROUP BY number ORDER BY -COUNT(*) LIMIT 1;


CREATE TABLE fa17favpets AS
  SELECT pet, COUNT(*) FROM fa17students GROUP BY pet ORDER BY -COUNT(*) LIMIT 10;


CREATE TABLE sp18favpets AS
  SELECT pet, COUNT(*) FROM students GROUP BY pet ORDER BY -COUNT(*) LIMIT 10;


CREATE TABLE sp18dog AS
  SELECT pet, COUNT(*) FROM students WHERE pet = 'dog';


CREATE TABLE sp18alldogs AS
  SELECT pet, COUNT(*) FROM students WHERE pet LIKE '%dog%';


CREATE TABLE obedienceimages AS
  SELECT seven, denero, COUNT(*) as count
    FROM students WHERE seven = '7' GROUP BY denero;

-- Q8
CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) AS count FROM students GROUP BY smallest ORDER BY smallest;
