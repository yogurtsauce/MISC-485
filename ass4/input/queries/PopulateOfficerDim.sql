delete from OfficerDim

;with officerquery as (
    select *
    from Officer
)


insert into OfficerDim (Id, Name, Rank)
select *
from officerquery