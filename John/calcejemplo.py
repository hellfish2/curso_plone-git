import odslib

doc = odslib.ODS()

for row in range(1, 9):
	for col in range(1, 9):
		doc.content.getCall(col, row).floatValue(col * row).setBorder()

doc.save("calc-example1.ods")
