-- https://programmers.co.kr/learn/courses/30/lessons/59046
select ANIMAL_ID, NAME, SEX_UPON_INTAKE
from ANIMAL_INS
where NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')