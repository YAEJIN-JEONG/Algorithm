select ANIMAL_TYPE, count(ANIMAL_TYPE)
from ANIMAL_INS
group by ANIMAL_TYPE
order by ANIMAL_TYPE asc
