# --*-- coding: utf-8 --*--
# python_day02_ex07_myApp.py
# 주소록 프로그램
'''
1.input 2.ouput 3.search 4.modify 5.delete 6.save 7.end
choice: 1
-------------------------------------------------------
### 입력기능 ###
성명: 홍길동
전화번호: 010-1234-5678
-------------------------------------------------------
1.input 2.ouput 3.search 4.modify 5.delete 6.save 7.end
choice: 2
-------------------------------------------------------
     성명     |     전화번호
    홍길동    | 010-1234-5678
-------------------------------------------------------
1.input 2.ouput 3.search 4.modify 5.delete 6.save 7.end
choice:
'''
class People:
	def __init__(self, idx, name, phone):
		self.idx = idx
		self.name = name
		self.phone = phone

	def showData(self):
		print("-"*50)
		print("{:^4}|{:^20}|{:^24}".format(self.idx, self.name, self.phone) )

addrBook = []
top = 5

def choiceMenu(menu):
	for i, item in enumerate(menu):
		print("{}.{}".format(i+1,item), end=" ")
	print()
	no = int(input("choice>>> ") )
	return no

def makePeople():
	name = input("성명>>> ")
	phone = input("연락처>>> ")
	return People(top, name, phone)

def input_data():
	print("### input_data ###")
	#변수의 지역성(전역화 시키기 위해서는 global키워드 사용)
	#global을 남발하면 프로그램에 혼선을 야기한다.
	#return문을 활용한다.
	global top
	top += 1
	addrBook.append( makePeople() )
	print("새로운 주소 추가 완료!")

def output_data():
	print("### output ###")
	for people in addrBook:
		people.showData()

def search_data():
	print("### search ###")

def modify_data():
	print("### modify ###")

def delete_data():
	print("### delete ###")

def save_data():
	print("### save ###")

factory = [input_data,output_data,search_data,modify_data,delete_data,save_data]

def play():
	while True:
		menu = ("input","ouput","search","modify","delete","save","end")
		no = choiceMenu(menu)
		if no == 7:
			print("프로그램 종료!")
			break
		if no in range(1,8):
			factory[no-1]()
		else:
			print("해당 사항 없다")
		print("-"*50)

def main():
	addrBook.append(People(1,"KIM","1111-1111"))
	addrBook.append(People(2,"LEE","2222-2222"))
	addrBook.append(People(3,"PARK","3333-3333"))
	addrBook.append(People(4,"CHOI","4444-4444"))
	addrBook.append(People(5,"HONG","5555-5555"))

	print("{:=^50}".format("전화번호부"))
	play()

if __name__=="__main__":
	main()
