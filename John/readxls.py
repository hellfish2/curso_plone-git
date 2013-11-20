from xlrd import open_workbook

def readWorksheet(sheetIO):
# Read row by row
 for rownum in range(sheetIO.nrows):
  rowValues = sheetIO.row_values(rownum)
  rollNo = rowValues[0]
  name = rowValues[1]
print rollNo, name

if __name__ == '__main__':
 bookTestData = open_workbook("/home/usuario/Libros.xls")
 sheetIO = bookTestData.sheet_by_name('Sheet1')
 readWorksheet(sheetIO)
