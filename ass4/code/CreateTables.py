import sqlite3

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()


def createTable(statement):
    cursor.execute(statement)


cursor.execute('''
      select name
      from sqlite_master
      where type = "table"
      ''')

ListOfTables = [
    'Vendor',
    'Category',
    'Product',
    'Includes',
    'SalesTransaction',
    'Customer',
    'Store',
    'Region'
]


for table in ListOfTables:
    cursor.execute(f"drop table if exists {table}")

# createTable('''
#             create table Vendor (
#                 Id varchar not null primary key,
#                 Name varchar not null
#             )
#     ''')


# createTable('''
#             create table Category (
#                 Id varchar not null primary key,
#                 Name varchar not null
#             )
#     ''')


# createTable('''
#             create table Product (
#                 Id varchar not null primary key,
#                 Price int not null,
#                 Name varchar not null,
#                 VendorId varchar not null references Vendor(Id),
#                 CategoryId varchar not null references Category(Id)
#             )
#     ''')


# createTable('''
#             create table Customer (
#                 Id varchar not null primary key,
#                 Name varchar not null,
#                 Zip int not null
#             )
#     ''')


# createTable('''
#             create table Region (
#                 Id varchar not null primary key,
#                 Name varchar not null
#             )
#     ''')


# createTable('''
#             create table Store (
#                 Id varchar not null primary key,
#                 Zip int not null,
#                 RegionId varchar not null references Region(Id)
#             )
#     ''')


# createTable('''
#             create table SalesTransaction (
#                 Id varchar not null primary key,
#                 Date date not null,
#                 StoreId varchar not null references Store(Id),
#                 CustomerId varchar not null references Customer(Id)
#             )
#     ''')


# createTable('''
#             create table Includes (
#                 ProductId varchar not null references Product(Id),
#                 TId varchar not null references SalesTransaction(Id),
#                 Quantity int not null,
#                 primary key (ProductId, TId)
#             )
#     ''')


conn.commit()
conn.close()
