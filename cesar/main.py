#!/usr/bin/env python

#from fiboCesar import fibo as f
#print "el valor de __name en main.py es:",__name__
#print f(4)

for var in range(0,10):
	print var
for var2 in xrange(0,10000):
	print var2
listaAsistentes = ["Luis", "Pedro", "Cesar"]
listaA = listaAsistentes

for asistentes in listaAsistentes:
	print "Los asistentes fueron:", asistentes

for numero,asistente in enumerate(listaA):
	print numero+1, asistente


