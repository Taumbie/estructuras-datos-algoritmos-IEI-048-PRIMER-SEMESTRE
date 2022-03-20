import turtle as tw

# configuramos el mundo de tortugas
tw.bgpic( "Grid 800x600.png" )
screen = tw.Screen()
screen.setup( 800, 600 )
screen.title( "Actividad 02" )

# creamos una tortuga
tortuga = tw.Turtle()
tortuga.shape( 'turtle' )
tortuga.setheading( 90 )
tortuga.speed( 4 )

# la preparamos para dibujar
tortuga.pensize( 4 )
tortuga.pencolor( "#0d05f0" )

# dibujamos el tronco
tortuga.penup()
tortuga.goto( 0, 100 )
tortuga.pendown()

tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 50 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 50 )
tortuga.penup()

# dibujamos la cabeza
tortuga.penup()
tortuga.setheading( 90 )
tortuga.goto( 50, 225 )
tortuga.pendown()

tortuga.circle( 25 )
tortuga.penup()

# ojo izquierdo
tortuga.penup()
tortuga.setheading( 90 )
tortuga.goto( 15, 225 )
tortuga.pendown()

tortuga.dot( 5, "#000000" )
tortuga.penup()

# ojo derecho
tortuga.penup()
tortuga.setheading(90)
tortuga.goto(35,225 )
tortuga.pendown()
tortuga.dot( 5, "#000000" )
tortuga.penup()

# pierna izquierda
tortuga.penup()
tortuga.goto(0,0)
tortuga.setheading(90)
tortuga.pendown()

tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)

# pierna derecha
tortuga.penup()
tortuga.goto(30,0)
tortuga.setheading(90)
tortuga.pendown()

tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)

# brazo izquierdo
tortuga.penup()
tortuga.goto(0,100)
tortuga.pendown()

tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)


# brazo derecho
tortuga.penup()
tortuga.goto(50,200)
tortuga.setheading(0)
tortuga.pendown()

tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(20)
tortuga.right(90)
tortuga.forward(100)
tortuga.penup()

# eso es todo
tortuga.home()
tw.done()