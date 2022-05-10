import sqlite3

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

with open(r"input/queries/CreateWarehouseTables.sql") as sql:
    query = sql.read()
cursor.executescript(query)

with open(r"input/queries/CreateOperationalTables.sql") as sql2:
    query2 = sql2.read()

cursor.executescript(query2)


conn.commit()
conn.close()
