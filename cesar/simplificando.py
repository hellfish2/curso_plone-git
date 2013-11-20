lista1 = [1,2,3,4,5,"esto es un string"]

lista2 = [cada_valor*cada_valor for cada_valor in lista1 if type(cada_valor)==int]
print lista2
print '\n'.join(str(valor) for valor in lista2)
