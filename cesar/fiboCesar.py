def factorial(n):
	"""Esta funcion calcula el factorial de un numro n"""
	print 'n',n
	if n>1:
		return n*factorial(n-1)
	else:
		print 'fin de linea'
		return 1

def fibo(n):
	"""Esta funcion calcula la serie de fibonacci
	Retorna la lista"""
	resultado = []
	num1, num2 = 0, 1
	while num2 < n:
		resultado.append(num2)
		num1, num2 = num2 , num1+num2
	return resultado

#print "el valor de __name en fiboCesar.py es:",__name__
if __name__ == "__main__":
	print fibo(4)
