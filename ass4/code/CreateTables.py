import sqlite3

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()

def createTable(statement):
    cursor.execute(statement)