#! /usr/bin/env python
# *-* coding=utf-8 *-*
import pg

c = pg.connect("prueba","161.196.204.6", 5433, None, None, "postgres", "postgres")  
r = c.query("DROP TABLE IF EXISTS tbl_jorge;CREATE TABLE tbl_jorge (id serial, titulo text, autor text, tipo text, paginas integer)") 

print r
