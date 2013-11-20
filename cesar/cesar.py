#!/usr/bin/env python
##EDITADO POR CARLOS MALAVE
from luis import Luis

class Cesar(Luis):
	"""Clase que implementa el metodo evaluarLista con una lista predefinida"""
	def __init__(self):
		self.lista1 = [1,2,3,4,5,"esto es un string"]
		

	def evaluarLista(self):
		"""Procedimiento que valida que la lista sea entera y eleva al cuadrado cada uno de sus valores retorna los valores de la lista separados por enter"""
		lista2 = [cada_valor*cada_valor for cada_valor in self.lista1 if type(cada_valor)==int]
		print '\n'.join(str(valor) for valor in lista2)

if __name__== "__main__":
	c = Cesar()
	c.evaluarLista()
