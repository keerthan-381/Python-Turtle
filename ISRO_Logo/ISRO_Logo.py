import turtle
t=turtle.Turtle()


t.pensize(3)
t.penup()
t.goto(-127.0,101.0)
t.pendown()
t.begin_fill()
t.pencolor('orange')
t.fillcolor('orange')
t.pensize(3)
t.left(60)
t.forward(300)
t.right(145)
t.forward(700)
t.right(175)
t.forward(550)
t.left(122.5)
t.forward(162)
t.end_fill()

t.penup()
t.goto(-314.0,300.0)
t.left(120)
t.pendown()


def rectangle():
    t.begin_fill()
    t.pencolor('blue')
    t.fillcolor('blue')
    t.pensize(3)
    for i in range(2):
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()

rectangle()
t.penup()
t.forward(130)
t.pendown()
rectangle()
t.penup()
t.forward(270)
t.pendown()
rectangle()
t.penup()
t.forward(130)
t.pendown()
rectangle()

t.penup()
t.goto(-350,-100.0)
t.pendown()
t.pencolor('orange')
t.write('इसरो ',font=("Monotype Corsiva",100,"bold"))

t.penup()
t.goto(100,-175)
t.pendown()
t.pencolor('blue')
t.write('isro ',font=("Dubai Medium",150,"bold"))

t.penup()
t.goto(101.0,32.0)
t.left(17.5)
t.pendown()
t.pensize(8)
t.forward(300)

t.penup()
t.goto(417.0,-254.0)
t.pendown()
t.write('#NSK',font=("Bradley Hand ITC",30,"bold"))

    


