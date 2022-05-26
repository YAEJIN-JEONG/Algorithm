-- https://programmers.co.kr/learn/courses/30/lessons/59410
select ANIMAL_TYPE, ifnull(NAME, 'No name'), SEX_UPON_INTAKE
from ANIMAL_INS
order by ANIMAL_ID
