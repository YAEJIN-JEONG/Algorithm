-- https://programmers.co.kr/learn/courses/30/lessons/59041
select NAME, count(NAME)
from ANIMAL_INS
where NAME is not null
group by NAME having count(NAME) >= 2
order by NAME asc