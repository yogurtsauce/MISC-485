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



conn.commit()
conn.close()
