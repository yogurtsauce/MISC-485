delete from TicketTypeDim;

with ticketqueries as (
    select 

    case when id='a' then 'driving'
    else 'driving' end as Category,

    violation,
    fee 

    from drivingtickettype

    union
    
    select 
    
    case when id='a' then 'parking'
    else 'parking' end as Category,
    
    violation,
    fee
    
    from parkingtickettype
)

insert into TicketTypeDim (Category, Violation, Fee)
select *
from ticketqueries