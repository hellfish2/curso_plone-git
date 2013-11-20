#! /usr/bin/env python
# *-* coding=utf-8 *-*
from rafael import Rafael

class Jorge(Rafael):
    def __init__(self,cedula=0,nombre="n/a",usuario="n/a",clave="n/a"):
        """
        clase Jorge con variables cedula y nombre

        return none
        """
        self.cedula = cedula
        self.nombre = nombre
        Rafael.__init__(self,usuario,clave)      

    def setCedula(self,cedula=-1):       
        self.cedula = str(cedula)

    def setNombre(self,nombre="undefined"):
        self.nombre = nombre

    def quienEs(self):
        print "Es:",self.nombre,",y su cedula es:",self.cedula

if __name__ =="__main__":
    j = Jorge()
    j.quienEs()
    j.setCedula(13918410)
    j.setNombre("Jorge Merchan")
    j.quienEs()
    print ""
    j.imprimir()
    j3 = Jorge(5678,"Rafael Barretta","rbarre06","Inicio01")
    j3.quienEs()
    print ""
    j3.imprimir()
    j2 = Jorge(1234,"Susana Villamizar")
    j2.quienEs()
    print ""
