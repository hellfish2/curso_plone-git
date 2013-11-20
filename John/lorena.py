from hugo import Hugo

class Lorena(Hugo):
   
  def raiz_cuadrada(self,numero):
    self.resultado=numero**0.5
    print "raiz cuadrada de: ",numero,"es",self.resultado

if __name__=="__main__":
  h=Lorena()
  h.raiz_cuadrada(4)
  h.dia_semana(5)
  

  
  
