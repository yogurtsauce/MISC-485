import sqlite3

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()

def query(input):
    results = cursor.execute(input).fetchall()
    colnames = cursor.description
    
    NameOfColumns = []
    for name in colnames:
        NameOfColumns.append(name[0])
    print(NameOfColumns)
    
    for row in results:
        print(row)
    


# query('''
#       select name
#       from sqlite_master
#       where type = "table"
#       ''')
query('''
      select * from Customer
               ''')




cursor.close()
