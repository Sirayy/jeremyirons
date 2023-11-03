select country, count(country)
from WINKA 
group by country
having count(country) > 1
