delete from VehicleDim;

with vehiclequery as (
    select LicensePlateNumber, Make, Model, Year, DriversLicenseNumber, Name, Gender, BirthYear
    from Driver as d
    join DrivingTicket as dt on dt.driverslicensenumber = d.driverslicensenumber
    join Vehicle as v on v.LicensePlateNumber = dt.VehicleLicensePlateNumber
)

insert into VehicleDim
select *
from vehiclequery