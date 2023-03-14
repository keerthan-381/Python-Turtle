import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgpic("Instagram.gif")

t.penup()
t.backward(200)
t.left(90)
t.forward(200)
t.right(90)
t.pendown()

t.pencolor('white')
t.pensize(25)

for i in range(4):
    t.forward(400)
    t.circle(-50,90)

t.penup()
t.goto(0,40)
t.pendown()
t.circle(-100)

t.penup()
t.goto(135.0,116.0)
t.pendown()
t.begin_fill()
t.fillcolor('white')
t.circle(-20)
t.end_fill()

t.penup()
t.goto(391.0,-314.0)
t.pendown()
t.pencolor('white')
t.write("#NSK",font=("Bradley Hand ITC",30,"bold"))

