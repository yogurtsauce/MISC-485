import sqlite3

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()


def query(filename):
    filepath = (f"input/queries/{filename}.sql")
    with open(filepath, "r")as sql:
        query = sql.read()
        results = cursor.execute(query).fetchall()
        colnames = cursor.description

        NameOfColumns = []
        for name in colnames:
            NameOfColumns.append(name[0])
        print(NameOfColumns)

        for row in results:
            print(row)


query('customer')
