import turtle
t=turtle.Turtle()

t.penup()
t.goto(-500.0,185.0)
t.pendown()

t.pencolor('red')
t.pensize(20)
t.forward(180)
t.penup()
t.forward(60)
t.pendown()
t.forward(120)

t.backward(60)
t.right(90)
t.penup()
t.backward(60)
t.pendown()
t.forward(120)
t.penup()
t.forward(60)
t.pendown()
t.forward(180)
t.right(90)
t.forward(300)
t.right(90)
t.forward(300)


t.penup()
t.goto(-430.0,-117.0)
t.pendown()
t.write("1",font=("",200,"bold"))

t.penup()
t.goto(-66.0,175.0)
t.pendown()
t.right(90)

t.begin_fill()
t.fillcolor('red')
t.pencolor('red')
for i in range(2):
    t.forward(700)
    t.right(90)
    t.forward(285)
    t.right(90)
t.end_fill()


t.pencolor('white')
t.penup()
t.goto(-50.0,-45.0)
t.pendown()
t.write("ONE PLUS",font=("",100,"bold"))

t.penup()
t.pencolor('red')
t.goto(415.0,-264.0)
t.pendown()
t.write("#NSK",font=("Bradley Hand ITC",30,"bold"))














