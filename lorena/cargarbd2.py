import xlrd
from pg8000 import DBAPI
conn = DBAPI.connect(host="161.196.204.6", user="postgres", password="postgres",port=5433,database="prueba")
cursor = conn.cursor()
libro = xlrd.open_workbook("Libros.xls")
hoja = libro.sheet_by_name('Hoja1')
filas = hoja.nrows
for i in range(filas-1):
   title=hoja.cell_value(rowx=i+1,colx=0)
   author= hoja.cell_value(rowx=i+1,colx=1)
   tipolibro= hoja.cell_value(rowx=i+1,colx=2)
   paginalibro= hoja.cell_value(rowx=i+1,colx=3)
   if len(str(paginalibro))==0:
      paginalibro=0
   #query = "INSERT INTO LORENA (titulo, autor, tipo, pagina) VALUES ('%s','%s','%s',%s)" % (title,author,tipolibro,paginalibro)
  #query = "INSERT INTO LORENA (titulo, autor, tipo, pagina) VALUES ('" + title + "','" + author + "','" + tipolibro + "','" + paginalibro + "')"
   query = "INSERT INTO LORENA (titulo, autor, tipo, pagina) VALUES ('" + title + "','" + author + "','" + tipolibro + "'," + str(paginalibro) + ")"
  # print query
   #cursor.execute(query)
   conn.commit()

s="SELECT * FROM LORENA"
cursor.execute(s)
for cada_uno in cursor.fetchall():
  print cada_uno



"""for each in range(20):
      cursor.execute(s)
     print cursor.fetchone()"""
#print cursor.fetchone()
cursor.close()
conn.close()

