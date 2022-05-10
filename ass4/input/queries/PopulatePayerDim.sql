delete from PayerDim

;with payerquery as (
    select * 
    from Driver
)

insert into PayerDim(DLN, [Name], Gender, BirthYear)
select *
from payerquery