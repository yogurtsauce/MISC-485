# Assignment 4

## Table Of Contents <!-- omit in toc -->

- [Assignment 4](#assignment-4)
  - [Requirements](#requirements)
  - [Schemas and tables](#schemas-and-tables)
  - [Creating the tables](#creating-the-tables)

## Requirements

**Question 1:**

    E8.2 in Chapter 8. (Note: 1st Edition: there are some typos in Figure 8.43. In Figure 8.46, please remove any space inside a field name). Please do E8.2a (manually populate the tables in Figure 8.42), E8.2b, and E8.2c. No SQLs are needed.

    Note: please add ticket type ID for TicketType dimension.

    Submit your answers in one Word file.

**Question 2:**

    Step 1: Use Access to create the operational database (E8.2) City Police Department and input sample data as shown in Figure 8.39 (1st Edition 8.43) and Figure 8.40 (1st Edition, 8.44).

    Step 2: Use SQL statements to create the data warehouse table structures (without data) based on the star schema as shown in Figure 8.41 (1st Edition: 8.45) and Figure 8.42 (1st Edition 8.46).

    Step 3: Use SQL statements to populate the data warehouse tables.

    Step 4: Use SQL statements to:

    (a) Compare the ticket amount between male and female, showing the genders and their corresponding amounts.

    (b) Compare the ticket amount by different ticket categories, showing the ticket categories, ticket violation, and the corresponding amounts.

    Please submit an Access file.

**Hint:**

    It’s a good practice to prepare needed data by query (or queries, several queries can be used for a complex task).
    You may use Union in SQL query to get all Dates from DrivingTicket and ParkingTicket tables.
    You may use Union in SQL query to get the data from two or more tables.

## Schemas and tables

![image1](https://github.com/yogurtsauce/MISC-485/blob/master/ass4/input/images/image1.jpg)
![image2](https://github.com/yogurtsauce/MISC-485/blob/master/ass4/input/images/image2.jpg)

## Creating the tables

<details>
<summary>View Code</summary>

```
createTable('''
            create table Vendor (
                Id integer not null primary key autoincrement,
                Name varchar not null
            )
    ''')


createTable('''
            create table Category (
                Id integer not null primary key autoincrement,
                Name varchar not null
            )
    ''')


createTable('''
            create table Product (
                Id integer not null primary key autoincrement,
                Price int not null,
                Name varchar not null,
                VendorId integer not null references Vendor(Id),
                CategoryId integer not null references Category(Id)
            )
    ''')


createTable('''
            create table Customer (
                Id integer not null primary key autoincrement,
                Name varchar not null,
                Zip int not null
            )
    ''')


createTable('''
            create table Region (
                Id integer not null primary key autoincrement,
                Name varchar not null
            )
    ''')


createTable('''
            create table Store (
                Id integer not null primary key autoincrement,
                Zip int not null,
                RegionId integer not null references Region(Id)
            )
    ''')


createTable('''
            create table SalesTransaction (
                Id integer not null primary key autoincrement,
                Date date not null,
                StoreId integer not null references Store(Id),
                CustomerId integer not null references Customer(Id)
            )
    ''')


createTable('''
            create table Includes (
                ProductId integer not null references Product(Id),
                TId integer not null references SalesTransaction(Id),
                Quantity int not null,
                primary key (ProductId, TId)
            )
    ''')
```

</details>
