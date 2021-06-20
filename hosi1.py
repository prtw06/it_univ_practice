import turtle

turtle.color('blue', 'yellow')

turtle.begin_fill()
for _ in range(5):
    turtle.forward(300)
    turtle.right(360 / 5*2 )
turtle.end_fill()

turtle.done()
