#!/usr/bin/env python

import pg

usuario='postgres'
clave='postgres'
base='prueba'
ip='161.196.204.6'
puerto=5433

conexion=pg.connect(host=ip,dbname=base,port=puerto,user=usuario,passwd=clave)
consulta='select * from john'
#consuta='CREATE TABLE john (titulo varchar(50),autor varchar(50), tipo varchar(50), paginas integer)'
#respuesta=conexion.query("CREATE TABLE john (titulo varchar(50),autor varchar(50), tipo varchar(50), paginas integer)")
respuesta=conexion.query(consulta)
conexion.close()

print respuesta
