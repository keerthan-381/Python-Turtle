import turtle
t=turtle.Turtle()

t.forward(150)
t.left(90)
t.penup()
t.circle(150,50)
t.pendown()
t.circle(150,310)
t.penup()
t.circle(150,50)
t.left(90)
t.pendown()

t.begin_fill()
t.pensize(3)
t.fillcolor('red')
t.pencolor('red')
t.forward(40)
t.right(90)
t.circle(110,120)
t.right(90)
t.forward(40)
t.right(90)
t.circle(-150,120)
t.end_fill()

t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.circle(110,120)
t.pendown()

t.begin_fill()
t.pensize(3)
t.fillcolor('yellow')
t.pencolor('yellow')
t.circle(110,30)
t.right(90)
t.forward(40)
t.right(90)
t.circle(-150,30)
t.end_fill()

t.penup()
t.right(90)
t.forward(43)
t.right(90)
t.circle(110,30)
t.pendown()

t.begin_fill()
t.fillcolor('green')
t.pencolor('green')
t.pensize(3)
t.circle(110,110)
t.right(90)
t.forward(40)
t.right(90)
t.circle(-150,110)
t.end_fill()

t.penup()
t.right(90)
t.forward(40)
t.right(90)
t.circle(110,110)
t.pendown()

t.begin_fill()
t.fillcolor('blue')
t.pencolor('blue')
t.pensize(3)
t.circle(110,33)
t.left(107)
t.forward(110)
t.right(90)
t.forward(33)
t.right(90)
t.forward(155)
t.right(90)
t.circle(-150,50)
t.end_fill()


t.penup()
t.goto(184.0,-197.0)
t.pendown()
t.pencolor('black')
t.write('#NSK',font=("Bradley Hand ITC",30,"bold"))
        
































        


