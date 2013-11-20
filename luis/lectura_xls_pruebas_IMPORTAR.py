#!/usr/bin/env python
# *-*coding=utf-8 *-*

from xlrd import open_workbook,cellname
from pg8000 import DBAPI
from unicodedata import normalize
from workbook import Workbook

wb = Workbook()
wb.country_code = 61

conn = DBAPI.connect(host="161.196.204.6", user="postgres", password="postgres", port=5433, database="prueba")

book = open_workbook('Libros.xls')
sheet = book.sheet_by_index(0)

filas = sheet.nrows
columnas = sheet.ncols


cursor = conn.cursor()
for row_index in range(1, filas):
    valor1=sheet.cell(row_index,0).value
    valor2=sheet.cell(row_index,1).value
    valor3=sheet.cell(row_index,2).value
    valor4=sheet.cell(row_index,3).value
    #print "INSERT INTO luis_pruebas (titulo,autor,tipo,paginas) VALUES ('%s','%s','%s','%s');" % (valor1, valor2, valor3, valor4)
    #cursor.execute("TRUNCATE luis_pruebas;")
    #conn.commit()
    cursor.execute("INSERT INTO luis_pruebas (titulo,autor,tipo,paginas) VALUES ('%s','%s','%s','%s');" % (valor1,valor2,valor3,valor4))
    conn.commit()


cursor.execute("select id,titulo,autor,tipo,paginas from luis_pruebas")
rows = cursor.fetchall()
for result in rows:
    print result[0]," - ", result[1]," - ", result[2]," - ", result[3]

cursor.close()
conn.close()
