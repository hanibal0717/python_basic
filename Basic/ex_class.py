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


# 클래스 선언시 클래스 내의 함수는 인자로 self가 필수다.
# 멤버 변수 선언이 따로 없다.
# self.멤버변수 <== 클래스의 멤버 변수가 된다.
# self 는 해당 클래스로 생성된 인스턴스 자신의 참조변수
# 자바나 C++의 this와 비슷한 개념
class People:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def showInfo(self):
        print(self.name, self.phone)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class Student(People):
    def __init__(self, name, phone, hakbun):
        super().__init__(name, phone);  # 부모의 __init__()을 호출
        self.hakbun = hakbun

    def showInfo(self):
        super().showInfo()
        print(self.hakbun)


# p = People("HONG","010-1234-5678")
# print(p.name)
# print(p.phone)
# p.showInfo()

s = Student("KIM", "010-1111", "1234")
s.showInfo()