-- https://programmers.co.kr/learn/courses/30/lessons/59042
select outs.ANIMAL_ID, outs.NAME
from ANIMAL_OUTS outs
    left join ANIMAL_INS ins
    on outs.ANIMAL_ID = ins.ANIMAL_ID
where ins.ANIMAL_ID is null
order by outs.ANIMAL_ID
