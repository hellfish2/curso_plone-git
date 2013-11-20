#!/usr/bin/python
# *-* coding: utf-8 *-*
# vim: set fileencoding= utf-8 :
import xlrd


"""from pg8000 import DBAPI

db = DBAPI.connect(host="161.196.204.6",user="postgres",password="postgres",database="prueba",port=5433)

cursor = db.cursor()"""

#cursor.execute("CREATE TABLE cesarLibrosFinal (id SERIAL, titulo TEXT, author TEXT, tipo TEXT, paginas TEXT)")
#query = """INSERT INTO cesarLibrosFinal (titulo, author, tipo, paginas) VALUES (%s, %s, %s, %s)"""
doc = xlrd.open_workbook('Libros.xls')
sheet = doc.sheet_by_index(0)

for r in range(1, sheet.nrows):
      titulo = sheet.cell(r,0).value
      author = sheet.cell(r,1).value
      tipo = sheet.cell(r,2).value
      paginas = sheet.cell(r,3).value
      values = (titulo, author, tipo, paginas)
      print values 
      #cursor.execute(query, values)

#book_id, = cursor.fetchone()
"""cursor.close()
db.commit()
db.close()"""
