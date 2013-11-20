from pyExcelerator.Workbook import *
from pyExcelerator.Style import *

style = XFStyle()

wb = Workbook()
ws0 = wb.add_sheet('0')

for fila in range(1,9):
  for columna in range (1,9):
       ws0.write(fila, columna, fila*columna)

wb.save('hojaexcel.xls')
