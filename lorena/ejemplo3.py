#from openpyxl import Workbook
import openpyxl


libro = openpyxl.Workbook()
hoja = libro.get_active_sheet()
for fila in range(1,9):
  for columna in range (1,9):
   celda = hoja.cell(row=fila, column=columna) 
   celda.value =fila*columna

libro.save("nombre_archivo.xlsx")

