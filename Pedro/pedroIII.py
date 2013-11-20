def factorial(n):
     """Esta funcion retorne el valor final corrrespondiente al factorial del valor n.
"""

    print 'n =', n
    if n > 1:
       return n * factorial(n - 1)
    else:
        print 'end of the line'
        return 1

def fib(n):
    result =  []
    a , b = 0 , 1
    while b < n:
        result.append(b)
        a , b = b , a+b
 
# a = b 
# b = a + b
return result

if __name__=="__main__":
print fib 22
