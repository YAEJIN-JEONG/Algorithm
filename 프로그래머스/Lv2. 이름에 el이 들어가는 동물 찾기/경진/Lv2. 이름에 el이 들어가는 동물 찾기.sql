-- https://programmers.co.kr/learn/courses/30/lessons/59047
select ANIMAL_ID, NAME
from ANIMAL_INS
where NAME like '%EL%'
    and ANIMAL_TYPE = 'Dog'
order by NAME