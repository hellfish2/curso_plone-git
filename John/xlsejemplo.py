
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('prueba.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

for row in range(1, 9):
	for col in range(1, 9):

		worksheet.write(row, col, row * col)

workbook.close()
