-- https://programmers.co.kr/learn/courses/30/lessons/59412
select hour(DATETIME), count(DATETIME)
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by hour(DATETIME)
order by hour(DATETIME)
