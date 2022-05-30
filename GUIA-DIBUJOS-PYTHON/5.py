from turtle import*
import turtle

speed(5)


left(90)
penup()
forward(200)
right(90)

#fondo

fillcolor("black")
begin_fill()

pendown()

forward(150)
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(300)
right(90)
forward(150)

end_fill()

# N derecha

right(90)

pencolor("dark red")

penup()

forward(37)
left(90)
backward(17)

pendown()

backward(34)

penup()

forward(68)

pendown()

fillcolor("dark red")
begin_fill()

forward(34)
right(90)
forward(226)
right(95)
forward(34)


right(85)
forward(223)

end_fill()

# N medio

right(90)
forward(34)
right(90)
forward(226)

pencolor("red")

fillcolor("red")
begin_fill()

right(163)
forward(236)
left(73)
forward(34)
left(107)
forward(232)
left(65)
forward(34)

end_fill()

penup()

# N izquierdo

pencolor("dark red")

left(188)
forward(102)

pendown()

fillcolor("dark red")
begin_fill()

right(172)
forward(34)
left(82)
forward(110)
left(16.5)
forward(117)
left(163.5)
forward(226)

end_fill()

right(30)

mainloop()