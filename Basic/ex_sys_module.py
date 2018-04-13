# --*-- coding: utf-8 --*--
# import를 이용한 모듈 이용방법
# sys 모듈을 이용

import sys

args = sys.argv[0:]
for arg in args:
	print(arg)