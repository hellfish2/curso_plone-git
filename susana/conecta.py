#!/usr/bin/python
#*.* coding = utf-8 *.*

#Host Details
host = "161.196.204.6"
port = 5433

#You will need to change these to your specific connection details.
user = "postgres"
dbname = "prueba"
passwd = "postgres"

import pgdb

def pgdbExample():
    """See: http://www.python.org/peps/pep-0249.html"""

    # DB-API needs a data source name in this format.
    dsn = host + ':' + dbname

    # By default a transaction is implicitly started when the connection is
    # created in DB-API. Unfortunately it is not possible to stop this in the
    # pgdb module, other DB-API implementations do allow different behaviour.
    connection = pgdb.connect(dsn=dsn, user=user, password=passwd)

    # A cursor object (not necessarily a PostgreSQL cursor - depends on the
    # module implementation) is required for all database operations.
    cursor = connection.cursor()

    # Create an example table.
    cursor.execute("CREATE TABLE test(code SERIAL PRIMARY KEY, data TEXT);")

    # Put something in the table. The "code" attribute is populated but
    # the implicit trigger on the SERIAL type. When inserting many rows into
    # a table the executemany() method is a better option.
    cursor.execute("INSERT INTO test (data) VALUES ('Hello World!');")

    # Commit what we've done so far. This implicitly starts a new transaction
    # within the connection object.
    connection.commit()

    # Fetch all entries in our example table.
    cursor.execute("SELECT * FROM test;")

    print "There were " + str(cursor.rowcount) + " rows in the table:\n"

    # Pull the data into python data structures. Note that this is not the
    # best way to deal with very large sets of data, the fetchone() or
    # fetchmany() method would be better. This gives the python module the
    # option of using PostgreSQL cursors or similar efficiency tricks.
    tuples = cursor.fetchall()

    # Print out table data.
    for (code, data) in tuples:
        print "Code: " + str(code) + ", Data: " + str(data)

    # Clean up.
    cursor.execute("DROP TABLE test;")
    connection.commit()

    # Close database connection.
    cursor.close()
    connection.close()


import pg

def pgExample():
    """See: http://www.postgresql.org/docs/7.3/static/pygresql.html"""

# Open a connection to the database using the pg module"s DB class.
    db = pg.DB(dbname=dbname, host=host, user=user, passwd=passwd)
    print "Conectado"

 # Start a transaction.
    db.query("BEGIN;")

    # Create and example table.
    db.query("CREATE TABLE test(code SERIAL PRIMARY KEY, data TEXT);")

    # The DB class in the pg module has a nice method that allows us to
    # pass it a dictionary and have it insert it into the database.
    db.insert('test', {'data': 'Hello World!'})

    # Commit the transaction.
    db.query('END;')

    # Start another transaction.
    db.query("BEGIN;")

    # Fetch all entries from out example table.
    result = db.query("SELECT * FROM test;")

    print "There were " + str(result.ntuples()) + " rows in the table:\n"
    # Pull the data into python data structures.
    tuples = result.getresult()

    # Print out table data.
    for (code, data) in tuples:
        print "Code: " + str(code) + ", Data: " + str(data)

    # Clean up.
    db.query("DROP TABLE test;")
    db.query('END;')

    db.close()


#try:
#   conecta = pg.connect(dbname="prueba",user="postgres",passwd="posgres")
#except:
#   print "Error"
