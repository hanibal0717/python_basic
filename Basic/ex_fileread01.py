# --*-- coding: utf-8 --*--
#### mytype.py

import sys

try:
	fileName = sys.argv[1]
	print("fileName =>", fileName)
	fp=open(fileName, "r")
	data = fp.read()
	print(data)
except:
	print("파라미터 에러!")
