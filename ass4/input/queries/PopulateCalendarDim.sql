delete from CalendarDim;

with fulldate as (
            select distinct date 
            from drivingticket

            union

            select distinct date
            from parkingticket
      ),

datequery as (
select
-------------------------------------- case for days of week
case cast (strftime('%w', date) as integer)
when 0 then 'Sunday'
when 1 then 'Monday'
when 2 then 'Tuesday'
when 3 then 'Wednesday'
when 4 then 'Thursday'
when 5 then 'Friday'
else 'Saturday' end as DayOfWeek,
strftime('%d', date) as DayOfMonth,
strftime('%m', date) as Month,
------------------------------------- case for quarters
case cast (strftime('m',date) as integer)
when 1 | 2 | 3 then 'Q1'
when 4 | 5 | 6 then 'Q2'
when 7 | 8 | 9 then 'Q3'
when 10 | 11 | 12 then 'Q4'
else 'q4' end as Quarter,
--------------------------------------

strftime('%Y', date) as Year

from fulldate)

insert into CalendarDim (fulldate, dayofweek, dayofmonth, month, quarter, year)
select *
from fulldate, datequery