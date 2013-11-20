class Hoja(object):

	def __init__(self):
		self.var1 = 8
		self.var2 = 20
		print "Nuevo objeto ha sido instanciado en el constructor"

	def activar(self,cuanto,dias):
		print "Hoja activa",cuanto,"veces a los",dias,"dias"
		self.variable = 1
	def imprimir(self):
		print "variable:",self.variable

h = Hoja()
h.activar(5,10)
h.activar(dias=5,cuanto=2)
h.imprimir()
