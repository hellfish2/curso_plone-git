class Hoja(object):
    def __init__(self):
        self.variable1 = 8
        self.variable2 = 32
        print "Nuevo objeto ha sido instanciado, funcion __init__ ejecutada"
    def respirar(self,tantas=10,dias=2):
        print "Hoja respirando",tantas,"veces cada",dias,"dias"
        self.__variable=10

    def imprimir_variable(self):
        print "variable:",self.__variable   

h=Hoja()
h.respirar(dias=3)
h.__variable=8
h.imprimir_variable()

print "Funcionando"

h.respirar(8,1)

#__ variable privada esta en segundo plano
