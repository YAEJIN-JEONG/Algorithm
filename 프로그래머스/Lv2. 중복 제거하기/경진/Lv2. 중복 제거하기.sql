-- https://programmers.co.kr/learn/courses/30/lessons/59408
select count(*)
from (select distinct NAME from ANIMAL_INS) as TB_NAME
where TB_NAME.NAME is not null
