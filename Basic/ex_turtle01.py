import turtle

t = turtle.Turtle()

t.width(2)
t.speed(0)

length = 10
colors = ['red','green','blue','orange','pink']

while length<500 :
    length += 1
    t.pencolor(colors[length%len(colors)])
    t.forward(length)
    t.left(89)
