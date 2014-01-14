#!/usr/bin/env python
#*.* coding=utf-8 *.*

from pg8000 import DBAPI

#Abrimos la conexion a la base de datos
try:
  conn = DBAPI.connect(host="161.196.204.6", user="postgres", password="postgres", port=5433, database="prueba")
except:
  print "NO me puedo conectar"
# Creamos el cursor
cursor = conn.cursor()
cursor.execute("SELECT * FROM tabla_Rafael_Final")
for x in cursor.fetchall():
  li =[]
  for y in x:
     li.append(y)
  print li[1],',', li[2],',', li[3],',', li[4]
conn.commit()
