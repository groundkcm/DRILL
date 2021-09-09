import turtle

turtle.penup()
turtle.goto(0,-300)
turtle.pendown()

num = 4
while(num > 0):
    turtle.forward(500)
    turtle.left(90)
    num -= 1

x = 0
y = -300
while(num < 4):
    y += 100
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    num += 1

y += 100
turtle.right(90)
while(num > 0):
    x += 100
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(500)
    num -= 1

turtle.exitonclick()
