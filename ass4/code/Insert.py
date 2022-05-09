import sqlite3

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

openFile = open(r'input/data/insert.txt')

for row in openFile:
    row = str(row)
    cursor.execute(row)

conn.commit()
conn.close()