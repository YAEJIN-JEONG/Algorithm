-- https://programmers.co.kr/learn/courses/30/lessons/59409
select ANIMAL_ID,
        NAME,
        case when regexp_like(SEX_UPON_INTAKE, 'Neutered|Spayed') then 'O' else 'X' end "중성화"
from ANIMAL_INS
