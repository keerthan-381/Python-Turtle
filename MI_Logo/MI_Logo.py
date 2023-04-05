import turtle
t=turtle.Turtle()

t.penup()
t.backward(50)
t.left(90)
t.forward(350)
t.right(90)
t.pendown()


t.begin_fill()
t.fillcolor('orange')
t.pencolor('orange')
t.pensize(3)
for i in range(4):
    t.forward(150)
    t.circle(-230,90)
t.end_fill()

t.penup()
t.goto(-167.0,-57.0)
t.left(90)
t.pendown()
t.pencolor('white')

t.begin_fill()
t.fillcolor('white')
t.pencolor('white')
t.pensize(3)
t.forward(200)
t.right(90)
t.forward(230)
t.circle(-50,90)
t.forward(150)
t.right(90)
t.forward(60)
t.right(90)
t.forward(110)
t.circle(50,90)
t.forward(110)
t.left(90)
t.forward(160)
t.right(90)
t.forward(60)
t.end_fill()

t.penup()
t.backward(115)
t.right(90)
t.pendown()

t.begin_fill()
t.pencolor('white')
for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
t.end_fill()

t.penup()
t.right(90)
t.forward(200)
t.left(90)
t.pendown()
t.begin_fill()
t.pencolor('white')
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

t.penup()
t.goto(-150.0,-357.0)
t.pencolor('black')
t.pendown()
t.write("x i a o m i",font=("",60,"bold"))

t.penup()
t.goto(465.0,-260.0)
t.pendown()
t.pencolor('orange')
t.write("#NSK",font=("Bradley Hand ITC",30,"bold"))








