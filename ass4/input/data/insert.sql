delete from Officer;

insert into Officer
values ('1', 'Joe', 'Sergeant');

insert into Officer
values ('2', 'Mike', 'Patrolman');

insert into Officer
values ('3', 'Bob', 'Patrolman');

delete from DrivingTicket;

insert into DrivingTicket
values ('DT1111', '2020-01-01', '1', '111', 'IL2222', 'D1');

insert into DrivingTicket
values ('DT2222', '2020-01-02', '2', '222', 'IL2222', 'D1');

insert into DrivingTicket
values ('DT3333', '2020-01-02', '3', '111', 'IL1111', 'D2');

delete from ParkingTicket;

insert into ParkingTicket
values ('PT1111', '2020-01-01', '1', 'IL1111', 'P1');

insert into ParkingTicket
values ('PT2222', '2020-01-01', '2', 'IL2222', 'P2');

insert into ParkingTicket
values ('PT3333', '2020-01-02', '3', 'IL3333', 'P2');

delete from ParkingTicketType;

insert into ParkingTicketType
values ('P1', 'Meter Expired', 100);

insert into ParkingTicketType
values ('P2', 'Hydrant', 150);

delete from DrivingTicketType;

insert into DrivingTicketType
values ('D1', 'Red Light', 200);

insert into DrivingTicketType
values ('D2', 'Seat Belt', 100);

delete from Vehicle;

insert into Vehicle
values ('IL1111', 'Honda', 'CRV', 2017);

insert into Vehicle
values ('IL2222', 'Honda', 'Civic', 2020);

insert into Vehicle
values ('IL3333', 'Honda', 'Civic', 2018);

delete from Driver;

insert into Driver
values ('111', 'Bill', 'Male', 1998);

insert into Driver
values ('222', 'Suzy', 'Female', 1987);

insert into Driver
values ('333', 'David', 'Male', 1976)