#/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import xlrd

DSN = "host=161.196.204.6 dbname=prueba user=postgres password=postgres port=5433"

def leer_datos():
    con = psycopg2.connect(DSN) # se crea la conexión
    cur = con.cursor() # se crea un cursor

##########################

# Open the workbook and define the worksheet
book = xlrd.open_workbook("Libros.xls")
sheet = book.sheet_by_name("Hoja1")


# Get the cursor, which is used to traverse the database, line by line
database = psycopg2.connect (DSN)

# 
query = """INSERT INTO malave_final (Titulo, Autor, Tipo, Paginas) VALUES (%s, %s, %s, %s)"""

# 
for r in range(1, sheet.nrows):
      Titulo      = sheet.cell(r,).value
      Autor = sheet.cell(r,1).value
      Tipo          = sheet.cell(r,2).value
      Paginas     = sheet.cell(r,3).value

      # Assign values from each row
      values = (Titulo, Autor, Tipo, Paginas)

      # Execute sql Query
      cur.execute(query, values)

# Close the cursor
cur.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done! Bye, for now."
print ""
print "I "

########################

"""
def leer_datos():
    con = psycopg2.connect(DSN) # se crea la conexión
    cur = con.cursor() # se crea un cursor
    query = "INSERT INTO malave_final(Titulo,Autor,Tipo,Paginas) VALUES ('Titulo','autor','tipo',200);"
    cur.execute(query)
    con.commit()

    query = "SELECT * FROM malave_final;"
    cur.execute(query)
    for id in cur.fetchall():
        print (id)
    cur.close()
    con.close()
if __name__== "__main__":
   leer_datos();
"""
