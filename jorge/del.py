import pg
c = pg.connect("prueba","161.196.204.6", 5433, None, None, "postgres", "postgres") 

r = c.query('DELETE FROM tbl_jorge WHERE true;')




