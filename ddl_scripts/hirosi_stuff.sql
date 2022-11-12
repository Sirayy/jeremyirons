create table hirosi(
id INT NOT NULL,
name VARCHAR(30) NOT NULL,
class VARCHAR(30) NOT NULL,
race VARCHAR(30) NOT NULL,
ac INT not null,
hp INT not null,
speed INT not null,
align VARCHAR(30) NOT NULL,
source INT not null,
str INT not null,
dex INT not null,
con INT not null,
intel INT not null,
wis INT not null,
cha INT not null,
PRIMARY KEY(id));
)

DROP table if exists hirosi;

describe hirosi;

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/heroes.csv"
INTO TABLE chrispine.hirosi
COLUMNS TERMINATED BY ';'
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES (id,name,class,race,ac,hp,speed,align,source,str,dex,con,intel,wis,cha);

SELECT *
from hirosi;

CREATE table interakcje(
hero INT not null,
monster INT not null,
result_of_interaction VARCHAR(30) NOT NULL,
FOREIGN KEY (hero) REFERENCES hirosi(id),
FOREIGN KEY (monster) REFERENCES monszterki(id) 
);

select *
FROM interakcje;

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/link_heroes_monsters.csv"
INTO TABLE chrispine.interakcje
COLUMNS TERMINATED BY '|'
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES (hero,monster,result_of_interaction);

SELECT h.name, i.hero, COUNT(result_of_interaction)
FROM interakcje as i
 JOIN hirosi as h
ON h.id = i.hero
WHERE result_of_interaction = 'kill'
GROUP by hero
ORDER BY COUNT(result_of_interaction) DESC;

TRUNCATE TABLE interakcje;

select * 
from interakcje;

create view accordingly AS
select *
from INTERAKCJE 
WHERE result_of_interaction = 'kill';

select *
FROM accordingly;

SELECT h.name, a.hero -- , count(a.result_of_interaction)
FROM accordingly as a
FULL OUTER JOIN hirosi as h
ON h.id = a.hero
GROUP by hero
-- ORDER BY count(a.result_of_interaction) DESC
;

create view ranking_zabojcow AS 
SELECT h.name, a.hero, COUNT(result_of_interaction) AS kill_count
from hirosi AS h
LEFT JOIN accordingly as a
ON h.id = a.hero
GROUP by name
ORDER BY COUNT(result_of_interaction) DESC;

select *
from ranking_zabojcow;
 
create view besties AS
select *
from interakcje
where result_of_interaction = "befriend";

SELECT * 
FROM besties;

SELECT h.name, m.name, count(*)
from besties as b 
INNER JOIN hirosi as h
ON h.id = b.hero
INNER JOIN monszterki as m
ON m.id = b.monster
GROUP BY h.name, m.name;

SELECT m.name, m.str, AVG(h.str) as hiro_s
FROM besties as b
INNER JOIN hirosi as h
ON h.id = b.hero
INNER JOIN monszterki as m
ON m.id = b.monster
WHERE m.name like '%yeti%';

select * 
from monszterki;



