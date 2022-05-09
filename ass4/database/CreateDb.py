import sqlite3
from sqlite3 import Error

def createconnection(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
        print(sqlite3.version)
        
    except Error as err:
        print(err)
        
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    createconnection(r"database/database.db")