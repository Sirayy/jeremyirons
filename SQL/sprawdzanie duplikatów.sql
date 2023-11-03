select seriesnumber, count(*)
from tblEpisode ep
group by seriesnumber
having count(*) > 1
order by count(*) desc

