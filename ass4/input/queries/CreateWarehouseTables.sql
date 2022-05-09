create table PayerDim (
    [Key] integer not null primary key autoincrement,
    DLN varchar not null,
    [Name] varchar not null,
    Gender varchar not null,
    BirthYear int not null
);

create table VehicleDim (
    [Key] integer not null primary key autoincrement,
    LPN varchar not null,
    Make varchar not null,
    Model varchar not null,
    [Year] int not null,
    OwnerDLN varchar not null,
    OwnerName varchar not null,
    OwnerGender varchar not null,
    OwnerBirthYear int not null
);

create table CalendarDim (
    [Key] integer not null primary key autoincrement,
    Fulldate date not null,
    DayOfWeek varchar not null,
    DayOfMonth int not null,
    [Month] int not null,
    Quarter int not null,
    [Year] int not null,
);

create table OfficerDim (
    [Key] integer not null primary key autoincrement,
    Id varchar not null,
    [Name] varchar not null,
    Rank varchar not null
);

create table TicketTypeDim (
    [Key] integer not null primary key autoincrement,
    Category varchar not null,
    Violation varchar not null,
    Fee int not null
)

create table TicketRevenueFactTable (
    Id integer not null primary key autoincrement,
    Amount int not null,
    CalendarKey integer not null references CalendarDim([Key]),
    OfficerKey integer not null references OfficerDim([Key]),
    PayerKey integer not null references PayerDim([Key]),
    VehicleKey integer not null references VehicleDim([Key])
);

