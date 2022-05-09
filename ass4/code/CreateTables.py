import sqlite3

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

with open(r"input/queries/CreateOperationalTables.sql") as sql:
    query = sql.read()

cursor.executescript(query)


conn.commit()
conn.close()
