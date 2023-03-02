import turtle
t=turtle.Turtle()

t.penup()
t.backward(200)
t.left(90)
t.forward(200)
t.right(90)
t.pendown()


t.begin_fill()
t.fillcolor('blue')
t.pencolor('blue')
t.pensize(3)
for i in range(4):
    t.forward(400)
    t.circle(-20,90)
t.end_fill()

t.penup()
t.goto(-40.0,-370.0)
t.pendown()
t.pencolor('white')
t.write('f',font=("",400,"bold"))

t.penup()
t.goto(399.0,-286.0)
t.pendown()
t.pencolor('blue')
t.write('#NSK',font=("Monotype Corsiva",30,"bold"))
