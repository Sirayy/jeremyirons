
  _  _ _ _  _   
 / \| | | || |  
( o ) V V || |_ 
 \_/ \_n_/ |___|
                

-- it's a good idea to make sure you're in the right database
USE Movies
GO
CREATE PROC spSimple
AS
-- pointless procedure to list all actors from a database
SELECT * FROM tblActor

-- 3 ways to run procedure to list out actors
EXEC spListActors
GO
EXECUTE spListActors
GO
spListActors
GO

------------------------------------------------------------------------

-- show all films lasting more than a given number of minutes
SELECT
FilmName,
FilmRunTimeMinutes
FROM
tblFilm
WHERE
FilmRunTimeMinutes>120

-- show films lasting more than 3 hours
EXEC spFilmsByMinLength 180
-- show films lasting more than 3.5 hours
EXEC spFilmsByMinLength 210

------------------------------------------------------------------------

-- variables
CREATE PROC spListFilmsWithParameters (

@MinDate date,
@MaxDate date,
@ContainsText varchar(MAX)
)

AS
-- show films made between given dates, and whose titles contain given text
SELECT
FilmName,
FilmReleaseDate
FROM
tblFilm
WHERE
FilmReleaseDate between @MinDate and @MaxDate and
FilmName like '%' + @ContainsText + '%'

-- try out this stored procedure

EXEC spListFilmsWithParameters
'01/01/2001', '12/31/2010', 'Shrek'

-- OR pass parameters by name

EXEC spListFilmsWithParameters
@ContainsText='Shrek',
@MinDate='01/01/2001',
@MaxDate='12/31/2010'

------------------------------------------------------------------------


--I want to write a stored procedure which allows me to show the number of actors and directors born in a given range of years.  I could run this with parameters:
-- show number of directors and actors
-- born in each year

spShowYears 1970, 1980

CREATE PROC spShowYears(
@StartYear int,
@EndYear int
)

AS
-- create a table of years

DECLARE @tblYears TABLE (
YearId int IDENTITY(1,1) PRIMARY KEY,
YearNumber int,
NumberDirectors int,
NumberActors int
)

-- populate it with n years

DECLARE @year int
SET @year = @StartYear
WHILE @year <= @EndYear
BEGIN

-- insert into table this year

INSERT INTO @tblYears (
YearNumber,
NumberDirectors,
NumberActors
) VALUES (
@year,
0,
0
)

SET @year = @year + 1

END

-- set how many directors born in each year

UPDATE
@tblYears
SET
NumberDirectors = (
SELECT COUNT(*) FROM tblDirector
WHERE Year(DirectorDob) = YearNumber
)

-- set how many actors born in each year

UPDATE
@tblYears
SET
NumberActors = (
SELECT COUNT(*) FROM tblActor
WHERE Year(ActorDob) = YearNumber
)

-- return results

SELECT
*
FROM
@tblYears

--------------------------------------------------------

---The spListFilmsWithParameters procedure listed above has one flaw: you have to specify a value for every single parameter.  It would be good t be able to miss out a parameter and have it take a sensible value.  For example, it would be nice to run:
-- pass parameters by name

EXEC spListFilmsWithParameters
@ContainsText='Shrek',
@MinDate='01/01/2001'

---and have this return all Shrek films made since the start of the millennium, with no maximum date.  To do this, you need to give one or more parameters default values:

CREATE PROC spListFilmsWithParameters (
@MinDate date=null,
@MaxDate date=null,
@ContainsText varchar(MAX)=''
)
AS

-- show films made between given dates, and whose
-- titles contain given text (but let user omit parameters)

SELECT
FilmName,
FilmReleaseDate
FROM
tblFilm
WHERE
(FilmReleaseDate >= @MinDate or @MinDate is null) and
(FilmReleaseDate <= @MaxDate or @MaxDate is null) and
(FilmName like '%' + @ContainsText + '%')
--- Here's how this works.   Suppose you call the procedure, but don't specify the maximum date:
-- omit the MaxDate parameter
EXEC spListFilmsWithParameters
@MinDate='01/01/2001',
@ContainsText='Shrek'
---Then the conditon:
-- second of three conditions
@MaxDate is null
-----is always true (the parameter always equals null), so the second condition above will effectively be ignored.

--###################################################################


 __   _  ___  _   __   _   _   _  ___ 
|  \ / \|_ _|/ \ / _| / \ | \_/ || o \
| o ) o || || o ( (_ | o || \_/ ||  _/
|__/|_n_||_||_n_|\__||_n_||_| |_||_|  
                                      


-- Create the stored procedure
CREATE PROCEDURE dbo.cuspSumRideHrsSingleDay
    -- Declare the input parameter
	@DateParm date,
    -- Declare the output parameter
	@RideHrsOut numeric OUTPUT
AS
-- Don't send the row count 
SET NOCOUNT ON
BEGIN
-- Assign the query result to @RideHrsOut
SELECT
	@RideHrsOut = SUM(DATEDIFF(second, StartDate, EndDate))/3600
FROM CapitalBikeShare
-- Cast StartDate as date and compare with @DateParm
WHERE CAST(StartDate AS date) = @DateParm
RETURN
END