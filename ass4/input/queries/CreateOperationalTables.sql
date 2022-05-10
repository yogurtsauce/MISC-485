create table Driver (
    DriversLicenseNumber varchar not null primary key,
    [Name] varchar not null,
    Gender varchar not null,
    BirthYear int not null
);

create table Vehicle (
    LicensePlateNumber varchar not null primary key,
    Make varchar not null,
    Model varchar not null,
    Year int not null
);

create table Officer (
    Id varchar not null primary key,
    [Name] varchar not null,
    Rank varchar not null
);

create table ParkingTicketType (
    Id varchar not null primary key,
    Violation varchar not null,
    Fee int not null
);

create table DrivingTicketType (
    Id varchar not null primary key,
    Violation varchar not null,
    Fee int not null
);

create table ParkingTicket (
    Id varchar not null primary key,
    Date date not null,
    OfficerId varchar not null references Officer(Id),
    VehicleLicensePlateNumber varchar not null references Vehicle(DriversLicenseNumber),
    ParkingTicketTypeId varchar not null references ParkingTicketType(Id)
);

create table DrivingTicket (
    Id varchar not null primary key,
    Date date not null,
    OfficerId varchar not null references Officer(Id),
    DriversLicenseNumber varchar not null references Driver(DriversLicenseNumber),
    VehicleLicensePlateNumber varchar not null references Vehicle(LicensePlateNumber),
    DrivingTicketTypeId varchar not null references DrivingTicketType(Id)
);