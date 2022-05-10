import sqlite3

conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

ListOfTables = [
    'CalendarDim',
    'PayerDim',
    'VehicleDim',
    'OfficerDim',
    'TicketTypeDim',
    'TicketRevenueFactTable',
    'Driver',
    'Vehicle',
    'Officer',
    'ParkingTicketType',
    'DrivingTicketType',
    'ParkingTicket',
    'DrivingTicket'
]

for table in ListOfTables:
    cursor.execute(f"drop table if exists {table}")

with open(r"input/queries/CreateWarehouseTables.sql") as sql:
    query = sql.read()
cursor.executescript(query)

with open(r"input/queries/CreateOperationalTables.sql") as sql:
    query = sql.read()

cursor.executescript(query)


conn.commit()
conn.close()
