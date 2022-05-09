import sqlite3

connect = sqlite3.connect('ass3.db')
cursor = connect.cursor()


cursor.execute("""
    create table vendor (
    vendorId char(2) not null,
    vendorName varchar(25) not null,
    primary key (vendorId)
    );
    """)


cursor.execute("""
    CREATE TABLE category (
    categoryid  CHAR(2)  NOT NULL,
    categoryname  VARCHAR(25)  NOT NULL,
    PRIMARY KEY (categoryid) );
    """)

cursor.execute("""
    CREATE TABLE product
    (productid  CHAR(3)  NOT NULL,
    productname  VARCHAR(25)  NOT NULL,
    productprice  NUMERIC(7,2)  NOT NULL,
    vendorid  CHAR(2)  NOT NULL,
    categoryid  CHAR(2)  NOT NULL,
    PRIMARY KEY (productid),
    FOREIGN KEY (vendorid) REFERENCES vendor(vendorid),
    FOREIGN KEY (categoryid) REFERENCES category(categoryid));
    """)

cursor.execute("""
    CREATE TABLE region
    (  regionid  CHAR(1)  NOT NULL,
    regionname  VARCHAR(25)  NOT NULL,
    PRIMARY KEY (regionid) );
    """)

cursor.execute("""
    CREATE TABLE store
    (  storeid  VARCHAR(3)  NOT NULL,
    storezip  CHAR(5)  NOT NULL,
    regionid  CHAR(1)  NOT NULL,
    PRIMARY KEY (storeid),
    FOREIGN KEY (regionid) REFERENCES region(regionid) )
    """)

cursor.execute('''
    CREATE TABLE customer
    (  customerid  CHAR(7)  NOT NULL,
    customername  VARCHAR(15)  NOT NULL,
    customerzip  CHAR(5)  NOT NULL,
    PRIMARY KEY (customerid) );
    ''')

cursor.execute('''
    CREATE TABLE salesTransaction
    (  tid  VARCHAR(8)  NOT NULL,
    customerid  CHAR(7)  NOT NULL,
    storeid  VARCHAR(3)  NOT NULL,
    tdate  DATE  NOT NULL,
    PRIMARY KEY (tid),
    FOREIGN KEY (customerid) REFERENCES customer(customerid),
    FOREIGN KEY (storeid) REFERENCES store(storeid) );
    ''')

cursor.execute('''
    CREATE TABLE includes
    (  productid  CHAR(3)  NOT NULL,
    tid  VARCHAR(8)  NOT NULL,
    quantity  INT  NOT NULL,
    PRIMARY KEY (productid, tid),
    FOREIGN KEY (productid) REFERENCES product(productid),
    FOREIGN KEY (tid) REFERENCES salestransaction(tid) );
    ''')


connect.commit()
connect.close()
