a =("uno","dos","tres")
b =a
try:
	#a.append("cuatro")
	#index(2)
	print a
	print b

except Exception as e:
	print e

else:
	print a,b
finally:
	print "fin del programa"
