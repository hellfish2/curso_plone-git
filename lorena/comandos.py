cursor.execute("CREATE TABLE LORENA (titulo TEXT, autor TEXT, tipo TEXT, pagina integer)")

cursor.execute("select * from LORENA")

cursor.execute("INSERT INTO  LORENA VALUES ("20000 leguas de viaje submarino","Julio Verne","Novela",512)")


cursor.execute("CREATE TEMPORARY TABLE lorena (id SERIAL, title TEXT)")



