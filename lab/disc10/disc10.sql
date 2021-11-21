CREATE TABLE records AS
    SELECT "Ben Bitdiddle" AS name, "Computer" AS division, "Wizard" AS title, 60000 AS salary, "Oliver Warbucks" AS supervisor UNION
    SELECT "Alyssa P Hacker", "Computer", "Programmer", 40000, "Ben Bitdiddle" UNION
    SELECT "Cy D Fect", "Computer", "Programmer", 35000, "Ben Bitdiddle" UNION
    SELECT "Lem E Tweakit", "Computer", "Technician", 25000, "Ben Bitdiddle" UNION
    SELECT "Louis Reasoner", "Computer", "Programmer Trainee", 30000, "Alyssa P Hacker" UNION
    SELECT "Oliver Warbucks", "Administration", "Big Wheel", 150000, "Oliver Warbucks" UNION
    SELECT "Eben Scrooge", "Accounting", "Chief Accountant", 75000, "Oliver Warbucks" UNION
    SELECT "Robert Cratchet", "Accounting", "Scrivener", 18000, "Eben Scrooge" ;

-- 2.1
CREATE TABLE Oliver_supervisor AS
    SELECT name FROM records WHERE supervisor = "Oliver Warbucks";

-- 2.2
CREATE TABLE self_supervising AS
    SELECT * FROM records WHERE name = supervisor;

-- 2.3
CREATE TABLE salary_great AS
    SELECT name FROM records WHERE salary > 50000 ORDER BY name ASC;


CREATE TABLE meetings AS
    SELECT "Accounting" AS division, "Monday" AS day, "9am" AS time UNION
    SELECT "Computer", "Wednesday", "4pm" UNION
    SELECT "Administration", "Monday", "11am" UNION
    SELECT "Administration", "Thursday", "1pm";

-- 3.1
CREATE TABLE earntwice AS
    SELECT a.name, a.salary, a.supervisor, b.salary FROM records AS a, records AS b
    WHERE b.salary > 2*a.salary AND a.supervisor = b.name;

-- 3.2
CREATE TABLE differentdivision AS
    SELECT a.name FROM records AS a, records AS b
    WHERE a.supervisor = b.name AND a.division != b.division;

-- 3.3
CREATE TABLE meeting_Oliver AS
    SELECT a.day, a.time FROM meetings AS a, records AS b
    WHERE b.supervisor = "Oliver Warbucks" AND a.division = b.division;

-- 3.4
CREATE TABLE middlemanager AS
    SELECT DISTINCT a.name FROM records AS a, records AS b, records AS c
    WHERE a.supervisor = b.name AND c.supervisor = a.name 
        AND b.name != c.name AND a.name != b.name;

-- 3.6
CREATE TABLE samedaymeeting AS
    SELECT DISTINCT a.name FROM records AS a, records AS b, meetings AS c
    WHERE a.supervisor = b.name AND a.division = c.division AND b.division = c.division AND c.day = c.day;

-- 4.1
CREATE TABLE dogs(name, age, phrase DEFAULT "woof");
    INSERT INTO dogs(name, age) VALUES ("Fido", 1), ("Sparky", 2);
    INSERT INTO dogs VALUES ("Lassie", 2, "I'll save you!"), ("Floofy", 3, "Much doge");

-- SELECT * FROM dogs;


-- 5
CREATE TABLE courses AS
    SELECT "John DeNero" AS professor, "CS 61A" AS course, "Fa17" AS semester UNION
    SELECT "Paul Hilfinger", "CS 61A", 'Fa17' UNION
    SELECT "Paul Hilfinger", "CS 61A", 'Sp17' UNION
    SELECT "John DeNero", "Data 8", "Sp17" UNION
    SELECT "Josh Hug", "CS 61B", "Sp17" UNION
    SELECT "Satish Rao", "CS 70", "Sp17" UNION
    SELECT "Nicholas Weaver", "CS 61C", "Sp17" UNION
    SELECT "Gerald Friedland", "CS 61C", "Sp17" UNION
    SELECT "John DeNero", "CS 61A", "Fa16" UNION
    SELECT "Paul Hilfinger", "CS 61B", "Fa16";

CREATE TABLE num_taught AS
    SELECT "Gerald Friedland" AS professor, "CS 61C" AS course, 1 AS times UNION
    SELECT "John DeNero", "CS 61A", 2 UNION
    SELECT "John DeNero", "Data 8", 1 UNION
    SELECT "Josh Hug", "CS 61B", 1 UNION
    SELECT "Nicholas Weaver", "CS 61C", 1 UNION
    SELECT "Paul Hilfinger", "CS 61A", 2 UNION
    SELECT "Paul Hilfinger", "CS 61B", 1 UNION
    SELECT "Satish Rao", "CS 70", 1;

-- 5.1
CREATE TABLE Paul_1 AS
    SELECT course FROM num_taught WHERE professor = "Paul Hilfinger" AND times = 1;

-- 5.2
CREATE TABLE more AS
    SELECT a.professor, a.course, a.semester FROM courses AS a, courses AS b
    WHERE a.professor = b.professor AND a.course = b.course AND a.semester != b.semester;

-- 5.3 how to avoid pairs? using unique ID?
CREATE TABLE twoprof AS
    SELECT a.professor, b.professor, a.course FROM num_taught AS a, num_taught AS b
    WHERE a.course = b.course AND a.times = b.times AND a.professor != b.professor AND a.professor < b.professor;