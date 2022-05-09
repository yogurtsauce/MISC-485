import sqlite3

connect = sqlite3.connect('inclass.db')
cursor = connect.cursor()



cursor.execute('''
               create table Customer (
                   CustomerId integer not null primary key autoincrement,
                   CustomerName varchar(50) not null
               )
               ''')


cursor.execute('''
               create table TransactionTable (
                   Tid integer not null primary key autoincrement,
                   CustomerId smallint not null,
                   Tdate date not null,
                   Amount int not null
               )
               ''')


cursor.execute('''
               create table 
               ''')


connect.commit()
connect.close()
