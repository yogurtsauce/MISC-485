delete from TicketRevenueFactTable;

with payer as (
    select key PayerKey
    from payerdim
),

vehicle as (
    select key VehicleKey
    from vehicledim
),

calendar as (
    select key as CalendarKey
    from calendardim
),

officer as (
    select key OfficerKey
    from officerdim
),

ticket as (
    select key TicketTypeKey, 
    fee as amount
    from tickettypedim
)

insert into TicketRevenueFactTable (Amount,CalendarKey,OfficerKey,PayerKey,VehicleKey,TicketTypeKey)
select 
Amount,
CalendarKey,
OfficerKey,
PayerKey,
VehicleKey,
TicketTypeKey

from 
calendar, 
ticket,
payer, 
vehicle, 
officer

group by tickettypekey