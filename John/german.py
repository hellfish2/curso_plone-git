
from lorena import Lorena

class German(Lorena):
    def __init__(self):
        print "Ejercicio"
    def area(self,x,y):
        """Esta es la formula simple de calculo de area de un triangulo.
        """
        print "Base",x, "Altura",y
        return x*y/2



if __name__=="__main__":
    a = German()
    result = a.area(2,2)
    print result


