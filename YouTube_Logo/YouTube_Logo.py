import turtle
t=turtle.Turtle()

t.penup()
t.backward(150)
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

t.begin_fill()
t.fillcolor('red')
t.pencolor('red')
t.pensize(3)
for i in range(2):
    t.forward(300)
    t.circle(-40,90)
    t.forward(150)
    t.circle(-40,90)
t.end_fill()

t.penup()
t.goto(-25.0,75.0)
t.right(90)
t.pendown()

t.begin_fill()
t.pencolor('snow')
t.fillcolor('snow')
t.pensize(3)
for i in range(3):
    t.forward(80)
    t.left(120)
t.end_fill()

t.penup()
t.goto(219.0,-208.0)
t.pendown()
t.pencolor('black')
t.write('#NSK',font=("Bradley Hand ITC",30,"bold"))



