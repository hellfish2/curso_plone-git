import odslib

doc=odslib.ODS()

for row in range(1,900):
    for col in range (1,90):
        doc.content.getCell(col, row).floatValue(col * row).setBorder()

doc.save("calc-example01.ods")
