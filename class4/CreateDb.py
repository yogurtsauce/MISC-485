import sqlite3
from sqlite3 import Error


def CreateDatabase(name):
    connect = None
    try:
        connect = sqlite3.connect(name)
    except Error as err:
        print(err)
    finally:
        if connect:
            connect.close()


CreateDatabase(r'inclass.db')
