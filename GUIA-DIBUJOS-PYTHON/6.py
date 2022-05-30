from turtle import*
import turtle

speed(30)

penup()

left(90)
forward(100)

#rojo

right(45)

pendown()

pencolor("red")

fillcolor("red")
begin_fill()

forward(100)

right(180)

end_fill()

fillcolor("red")
begin_fill()
circle(10)
end_fill()

fillcolor("red")
begin_fill()

forward(100)
left(90)
forward(100)
left(89.9)
forward(100)

end_fill()

fillcolor("red")
begin_fill()
circle(10)
end_fill()

fillcolor("red")
begin_fill()

left(90)
forward(10)
right(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
right(90)
forward(10)

end_fill()

pencolor("white")
penup()
left(90)
forward(45)
left(90)
forward(37)

pendown()

right(90)

fillcolor("white")
begin_fill()
circle(13)
end_fill()

right(90)

penup()

forward(37)

left(90)
forward(50)
forward(18)

#azul

pendown()


pencolor("blue")

fillcolor("blue")
begin_fill()

left(90)
forward(100)
right(89.9)
forward(100)
right(180)

end_fill()

fillcolor("blue")
begin_fill()
circle(10)
end_fill()

fillcolor("blue")
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)

end_fill()

fillcolor("blue")
begin_fill()
circle(10)
end_fill()

fillcolor("blue")
begin_fill()

left(90)
forward(10)
right(90)
forward(10)
left(90)
forward(80)
left(90)
forward(10)
right(90)
forward(10)
left(90)

end_fill()

penup()

forward(75)
left(90)
forward(37.5)

pendown()

pencolor("white")

fillcolor("white")
begin_fill()
circle(13)
end_fill()

penup()

forward(62.5)
left(90)
forward(60)
left(90)
forward(37.5)

pendown()

fillcolor("white")
begin_fill()
circle(13)
end_fill()

right(90)

mainloop()