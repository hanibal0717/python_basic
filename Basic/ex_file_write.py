# --*-- coding: utf-8 --*--
'''
# 파일 입출력 하기
fp = open('파일명', 모드)로 파일을 열고
fp.close()로 파일을 닫는다.
'''
# 파일에 내용 쓰기
## w 모드는 파일이 존재하지 않으면 새 파일을 생성.
fp = open("io_test.txt", "w")

fp.write("파일 입력 연습 - 김범준\n")
for i in range(1,5):
	content = "%d 번째 라인 \n" %i
	fp.write(content)

# 파일 닫기
fp.close()