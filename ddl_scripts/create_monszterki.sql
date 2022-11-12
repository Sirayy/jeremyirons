create table monszterki(
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(30) not null,
url VARCHAR(200) not null,
cr VARCHAR(30) NOT NULL,
type VARCHAR(30) NOT NULL,
size VARCHAR(30) NOT NULL,
ac INT NOT NULL,
hp INT NOT NULL,
speed VARCHAR(30) NOT NULL,
align VARCHAR(30) NOT NULL,
legendary VARCHAR(30) NOT NULL,
source VARCHAR(200) NOT NULL,
str INT NOT NULL,
dex INT NOT NULL,
con INT NOT NULL,
intel INT NOT NULL,
wis INT NOT NULL,
cha INT NOT NULL,
PRIMARY KEY(id));

DESCRIBE monszterki;

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/dnd_monsters.csv"
INTO TABLE chrispine.monszterki
COLUMNS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES (name,url,cr,type,size,ac,hp,speed,align,legendary,source,str,dex,con,intel,wis,cha);
