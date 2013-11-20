
# Ejemplo de lectura de hoja Excel
import xlrd
import pg

usuario='postgres'
clave='postgres'
base='prueba'
ip='161.196.204.6'
puerto=5433

conexion=pg.connect(host=ip,dbname=base,port=puerto,user=usuario,passwd=clave)

book = xlrd.open_workbook("Libros.xls")
hoja = book.sheet_by_name('Hoja1')
filas = hoja.nrows
print "Las filas son :",filas

for i in range(filas-1):
    titulo=hoja.cell_value(rowx=i+1,colx=0)
    autor=hoja.cell_value(rowx=i+1,colx=1)
    tipo=hoja.cell_value(rowx=i+1,colx=2)
    paginas=hoja.cell_value(rowx=i+1,colx=3)

    print i

    insertar="""INSERT INTO john VALUES ('%s', '%s', '%s', '%s')""" % (titulo,autor,tipo,1)
    #insertar = "INSERT INTO john VALUES ('%s','%s','%s',%d)" % (titulo,autor,tipo,1)
    print insertar
    conexion.query(insertar.encode('utf-8'))
#respuesta=conexion.query("INSERT INTO john (titulo,autor,tipo,paginas) VALUES('a','b','c',1)")

#respuesta=conexion.query(insertar)

conexion.close()

#print respuesta
