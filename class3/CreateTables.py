import sqlite3

connect = sqlite3.connect('inclass.db')
cursor = connect.cursor()

cursor.execute('''
               
               ''')


connect.commit()
connect.close()