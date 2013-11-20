#!/bin/bash python
# *-* coding=utf-8 *-*

import odslib

doc= odslib.ODS()

for row in range(1,9):
  for col in range (1,9):
      doc.content.getCell(col,row).floatValue(col*row).setBorder()

doc.save("ejemplocalc.ods")
