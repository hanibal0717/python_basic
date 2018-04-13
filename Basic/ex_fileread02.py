# --*-- coding: utf-8 --*--
# 파일 읽기
# fp=open('파일명','r') <-- 파일을 읽기 모드로 열기
# data = fp.read() <- 파일의 내용을 읽기

#파일을 읽기 모드로 연다
fp=open("io_test.txt","r")

#파일의 데이터를 읽어온다.
#fp.read() >>> 전체 내용 읽기
#data = fp.read()
#print(data)

#fp.readline() >>> 한줄만 읽어 오기
#data = fp.readline()
#print(data)
'''
while True:
	data=fp.readline()
	if not data:
		break
	print(data, end="")
'''

#리스트로 읽어 온다.
dataList = fp.readlines()
for line in dataList:
	print(line, end="")

#파일을 닫아준다.
fp.close()
