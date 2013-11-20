#! /usr/bin/env python
# *-* coding=utf-8 *-*
import pg
from xlrd import open_workbook

c = pg.connect("prueba","161.196.204.6", 5433, None, None, "postgres", "postgres")  

book = open_workbook('Libros.xls',on_demand=True,encoding_override="utf-8")
sheet = book.sheet_by_name("Hoja1")
num_rows = sheet.nrows - 1
num_cols = sheet.ncols - 1

print num_rows
print num_cols

curr_row = 0
while curr_row < num_rows:
    curr_row += 1
    curr_col = -1
    
    titulo = sheet.cell_value(curr_row, 0)

    autor = sheet.cell_value(curr_row, 1)

    tipo = sheet.cell_value(curr_row, 2)

    paginas = sheet.cell_value(curr_row, 3)
    if paginas!= "" :
        paginas = int(float(paginas))
    else:
        paginas = 0
 
    query = """INSERT INTO tbl_jorge (titulo,autor,tipo,paginas) VALUES ('%s','%s','%s',%d)""" % (titulo,autor,tipo,paginas)
    query= query.encode("utf-8")

    res = c.query(query)

c.close()
