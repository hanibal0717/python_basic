# --*-- coding:utf-8 --*--
import turtle

t = turtle.Turtle()
t.width(3)
t.pencolor("red");

while True:
    # 방향과 각도와 거리를 입력해서 실행하도록 하세요.
    di = input("왼쪽:L, 오른쪽:R, 직진:S, 종료:Q >>>")
    if di == 'Q' or di == 'q':
        break
    print("방향 ==> ", di)

    angle = int(input("각도 입력 >>>"))
    length = int(input("거리 입력 >>>"))

    if di == "L" or di == "l":
        print("왼쪽으로 이동~")
        t.left(angle)
        t.forward(length)
    elif di == "R" or di == "r":
        print("오른쪽으로 이동~")
        t.right(angle)
        t.forward(length)
    elif di == "S" or di == "s":
        print("고고씽~ 직진~~")
        t.forward(length)
    else:
        print("관련 명령이 없다.")

print('수고하셨습니다.')