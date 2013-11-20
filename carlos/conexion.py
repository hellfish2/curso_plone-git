#!/usr/bin/env python
# -*- coding: utf-8 -*-
sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')
import psycopg2
from openpyxl import load_workbook

wb2 = load_workbook(filename ='Libros.xls')
print wb2.get_sheet_names()
# conexion a una base de datos existente
#conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres port=5432")
#cur = conn.cursor()
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
#conn.commit()


cur.execute("SELECT * FROM test;")
for record in cur:
	print record
conn.commit()
cur.fetchone()

cur.close()
conn.close()
