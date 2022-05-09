create table Vendor (
    Id varchar not null primary key,
    Name varchar not null
);

create table Category (
    Id varchar not null primary key,
    Name varchar not null
);

create table Product (
    Id varchar not null primary key,
    Price int not null,
    Name varchar not null,
    VendorId varchar not null references Vendor(Id),
    CategoryId varchar not null references Category(Id)
);

create table Customer (
    Id varchar not null primary key,
    Name varchar not null,
    Zip int not null
);

create table Region (
    Id varchar not null primary key,
    Name varchar not null
);

create table Store (
    Id varchar not null primary key,
    Zip int not null,
    RegionId varchar not null references Region(Id)
);

create table SalesTransaction (
    Id varchar not null primary key,
    Date date not null,
    StoreId varchar not null references Store(Id),
    CustomerId varchar not null references Customer(Id)
);

create table Includes (
    ProductId varchar not null references Product(Id),
    TId varchar not null references SalesTransaction(Id),
    Quantity int not null,
    primary key (ProductId, TId)
);