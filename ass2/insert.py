import sqlite3

connect = sqlite3.connect('hw2.db')
cursor = connect.cursor()

openFile = open(r'insert.txt')

for row in openFile:
    row = str(row)
    cursor.execute(row)

connect.commit()
connect.close()