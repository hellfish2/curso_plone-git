from bastidas import bastidas

class Padre():
    def __init__(self):
        """Prueba padre del constructor
        """
        self.x = 5;
        print("Este es el constructor de la clase padre")
  
    def metodo(self):
        print("Ejecutando metodo de clase padre")

if __name__=="__main__":

    p = Padre()
    p.metodo()
