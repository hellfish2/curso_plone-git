a = ('uno','dos','tres')
try:
    print a
    print b
except NameError:
    print "Sucedio un error relacionado con el nombre de la variable"

else:
    print a,b

finally:
    print "fin del programa"
