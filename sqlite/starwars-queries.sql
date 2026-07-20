/* PLaneten zählen */

SELECT COUNT(*) FROM planet;


/* Skywalker-Familie finden */

select a.name as character, b.name as planet
from people a
inner join planet b on a.planet_id=b.id
where a.name like '%Skywalker%';
