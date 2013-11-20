import pg
c = pg.connect("prueba","161.196.204.6", 5433, None, None, "postgres", "postgres") 

r = c.query('SELECT * FROM tbl_jorge;')

result = r.dictresult()

for it in result:
    k = it.keys()
    for i in k:
       print "%s: %s" % (i.capitalize(), it[i] )

    print "--------------------"

print "Total %s filas." % (len(result))

c.close()



