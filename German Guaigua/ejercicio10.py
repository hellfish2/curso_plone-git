#!/usr/bin/python
# *-* coding=utf-8 *-*
import xlrd
from pg8000 import DBAPI

db = DBAPI.connect(host="161.196.204.6",user="postgres",password="postgres",database="prueba",port=5433)
cursor = db.cursor()
cursor.execute("CREATE TABLE germanfinal (id SERIAL, titulo TEXT, autor TEXT, tipo TEXT, paginas TEXT)")
db.commit()
wb = xlrd.open_workbook('Libros.xls',encoding_override='utf-8')

wb.sheet_names()

sh = wb.sheet_by_index(0)
sh = wb.sheet_by_name('Hoja1')

for rownum in range(sh.nrows):
     titulo = sh.row_values(rownum)[0]
     autor = sh.row_values(rownum)[1]
     tipo = sh.row_values(rownum)[2]
     paginas = sh.row_values(rownum)[3]
     print titulo, autor, tipo, paginas
     
     if rownum>0:
        cursor.execute("""INSERT INTO germanfinal (titulo, autor, tipo, paginas) VALUES (%s, %s, %s, %s)""", (titulo, autor, tipo, paginas))
        db.commit()
    
row = 0
col = 0
ctype = 1  
value = 'asdf'
xf = 0   
sh.put_cell(row, col, ctype, value, xf)
#prueba git


