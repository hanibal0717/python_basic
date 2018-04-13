# --*-- coding: utf-8 --*--
#사용자 입력 -> 화면 출력

fp=open("io_test2.txt","w")
while 1:
	in_data = input()
	if not in_data:
		break
	#print(in_data)
	fp.write(in_data + "\n")

fp.close()