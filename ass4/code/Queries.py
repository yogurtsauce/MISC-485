import sqlite3

conn = sqlite3.connect('database/database.db')

cursor = conn.cursor()


def query(filename): #with row names
    filepath = (f"input/queries/{filename}.sql")
    outputdir = (f"output/queries/{filename}.txt")

    with open(filepath, "r")as sql:
        query = sql.read()
        results = cursor.execute(query).fetchall()
        colnames = cursor.description
        appendtooutput = open(outputdir, "a")

        NameOfColumns = []
        for name in colnames:
            NameOfColumns.append(name[0])
        appendtooutput.write(str(NameOfColumns)+'\n')

        records = []
        for row in results:
            records.append(row)

        for things in records:
            appendtooutput.write(str(things)+'\n')


def query2(filename): #no row names
    filepath = (f"input/queries/{filename}.sql")
    outputdir = (f"output/queries/{filename}.txt")

    with open(filepath, "r")as sql:
        query = sql.read()
        results = cursor.executescript(query).fetchall()
        appendtooutput = open(outputdir, "a")

        records = []
        for row in results:
            records.append(row)

        for things in records:
            appendtooutput.write(str(things)+'\n')


query('TableNames')
query2('PopulateOfficerDim')
query2('PopulateVehicleDim')
query2('PopulateTicketTypeDim')
query2('PopulateCalendarDim')
query2('PopulatePayerDim')
query2('PopulateFact')