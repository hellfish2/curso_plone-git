#!/usr/bin/env python
# *-*coding=utf-8 *-*

from pg8000 import DBAPI

conn = DBAPI.connect(host="161.196.204.6", user="postgres", password="postgres", port=5433, database="prueba")

cursor = conn.cursor()
cursor.execute("CREATE TABLE luis_pruebas (id SERIAL, titulo TEXT, autor TEXT, tipo TEXT, paginas TEXT)")
conn.commit()

cursor.close()
conn.close()
