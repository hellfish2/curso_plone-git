def factorial(n):
    """Funcion para el uso de factorial y sus valores
    """
    print'n=',n
    if n > 1:
		return n * factorial(n - 1)
    else:
        print 'end of the line'
        return 1
def fib(n):
    """Funcion que recrea la sucesion de fibonacci
    """
    result = []
    a,b = 0,1
    while b < n:
		result.append(b)
		a,b = b , a + b
    return result

print "Soy carlos.py y el valor de mi __name__ es:",__name__

if __name__ =='__main__':
	print fib(22)
