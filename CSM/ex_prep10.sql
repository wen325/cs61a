-- 4
create table X as select 20 as X;

    with ints(n) as (select 1 union select n+1 from ints, X where n < X)
    select a.n, count(*) from ints as a, ints as b 
        where b.n > a.n  AND b.n % a.n = 0 
        group by a.n having count(*) > 2;


-- 5

-- select starts, count(*) from reviews
--     where user = 'Albert'
--     group by starts
--     having stars > 3;


-- 6

CREATE TABLE anagrams as

    WITH word(letter, position) AS (
    SELECT 'c', 1 UNION
    SELECT 'a', 10 UNION
    SELECT 't', 100 UNION
    SELECT 's', 1000
)
    SELECT a.letter || b.letter || c.letter || d.letter
    FROM word AS a, word AS b, word AS c, word AS d
    WHERE a.position + b.position + c.position + d.position = 1111;


-- SELECT * FROM anagrams;
