import sqlite3

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

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

with open(r"input/queries/CreateTables.sql") as sql:
    query = sql.read()

cursor.executescript(query)


conn.commit()
conn.close()
