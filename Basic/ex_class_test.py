# --*-- coding: utf-8 --*--
'''
동물클래스
속성: 이름
메소드: 먹다, 소리내다. 잠잔다. 일어난다

동물을 상속받은 새
메소드: 날다

동물을 상속받은 원숭이
메소드: 나무에 오르다
'''

class Animal:
	def __init__(self, name):
		self.name = name
	def eat(self):
		print(self.name, "이 먹이를 먹는다")
	def sound(self):
		print(self.name, "이 소리를 낸다.")
	def sleep(self):
		print(self.name, "이 잠잔다.")
	def wakeup(self):
		print(self.name, "이 일어난다.")

class Bird(Animal):
	def __init__(self, name):
		super().__init__(name)
	def fly(self):
		print(self.name, "이 날아간다")

class Monkey(Animal):
	def __init__(self, name):
		super().__init__(name)
	def climb(self):
		print(self.name, "이 나무에 기어오른다")

bird = Bird("종달새")
bird.fly()
bird.sound()

monkey = Monkey("개코원숭이")
monkey.climb()
monkey.eat()