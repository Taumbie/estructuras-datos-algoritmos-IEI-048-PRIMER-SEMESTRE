from gettext import find
from turtle import*
import turtle

#techo

speed(10)
penup()
left(90)
forward(200)

pendown()
left(135)

fillcolor("light blue")
begin_fill()

forward(200)
left(45)
forward(40)
left(135)
forward(200)
right(90)
forward(200)
left(135)
forward(40)
left(45)
forward(200)

end_fill()

#parte central

penup()
left(45)
forward(120)
left(90)
forward(160)
pendown()
forward(200)
left(90)
forward(240)
left(90)
forward(200)

#base

backward(200)

fillcolor("light blue")
begin_fill()

right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(280)
right(90)
forward(30)
right(90)
forward(20)

end_fill()

#circulos

forward(240)
backward(120)
left(90)
penup()
forward(40)
pendown()
right(90)

fillcolor("light blue")
begin_fill()

circle(10)

end_fill()

left(90)
penup()
forward(60)
right(90)
pendown()

fillcolor("black")
begin_fill()

circle(60)

end_fill()

right(90)

mainloop()