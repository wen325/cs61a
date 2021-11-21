CREATE TABLE cats(name, weight DEFAULT 1, notes DEFAULT "meow");


INSERT INTO cats(name) VALUES ("Tom"), ("Whiskers");
INSERT INTO cats VALUES
    ("Mittens", 2, "Actually likes shoes"),
    ("Rascal", 4, "Prefers to associate with dogs"),
    ("Magic", 2, "Expert at card games");

UPDATE cats SET notes = "A cat" WHERE notes = "meow";
-- SELECT name FROM cats WHERE notes = "A cat";

CREATE TABLE food AS
    SELECT 1 AS cat_weight, 0.5 AS amount UNION
    SELECT 2 , 2.5 UNION
    SELECT 3 , 4.0 UNION
    SELECT 4 , 4.5;

CREATE TABLE cat_foods AS
    SELECT a.weight AS weight, b.amount AS amount 
    FROM cats AS a, food AS b
    WHERE a.weight = b.cat_weight;

-- SELECT sum(amount) FROM cat_foods

CREATE TABLE total AS
    SELECT sum(b.amount)
    FROM cats AS a, food AS b
    WHERE a.weight = b.cat_weight;
