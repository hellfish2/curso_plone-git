#!/usr/bin/env python
#*.* coding=utf-8 *.*

from pg8000 import DBAPI
import xlrd


# LECTURA DEL ARCHIVO PARA VACIAR LOS DATOS
workbook = xlrd.open_workbook('Libros.xls', on_demand=True, encoding_override='utf-8')
worksheet = workbook.sheet_by_index(0)
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = 0


#Abrimos la conexion a la base de datos
try:
  conn = DBAPI.connect(host="161.196.204.6", user="postgres", password="postgres", port=5433, database="prueba")
except:
  print "NO me puedo conectar"

# Creamos el cursor
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS tabla_Rafael_Final")
cursor.execute("CREATE TABLE tabla_Rafael_Final (id SERIAL primary key, titulo varchar(50), autor varchar(50), tipo varchar(50), paginas int)")
conn.commit()

while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    curr_cell = -1
    li = []
    while curr_cell < num_cells:
	curr_cell += 1
	cell_type = worksheet.cell_type(curr_row, curr_cell)
	cell_value = worksheet.cell_value(curr_row, curr_cell)

        if isinstance(cell_value,float):
           cell_value2 = int(cell_value)
        else:
           cell_value2 = cell_value

        li.append(cell_value2)
    
    # Normalizacion para las paginas vacias
    if len(str(li[3]))<=0:
       li[3] = 0

    print "linea: ",li[0],',', li[1],',',li[2],',',li[3]
    cursor.execute('INSERT INTO tabla_Rafael_Final (titulo, autor, tipo, paginas) VALUES (%s, %s, %s, %s) RETURNING id',(li[0],li[1],li[2],int(li[3])))

conn.commit()

cursor.close()
conn.close()
