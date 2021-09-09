import turtle

num = 4
while(num > 0):
    turtle.forward(500)
    turtle.left(90)
    num -= 1

x = 0
y = 0
while(num < 4):
    turtle.penup()
    turtle.goto(x,y+100)
    turtle.pendown()
    turtle.forward(500)
    num += 1

x += 100
y += 100
turtle.right(90)
while(num > 0):
    turtle.forward(500)
    turtle.penup()
    turtle.goto(x+100,y)
    turtle.pendown()
    num -= 1

turtle.exitonclick()
