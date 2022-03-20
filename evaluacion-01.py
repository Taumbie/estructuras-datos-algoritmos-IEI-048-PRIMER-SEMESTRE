import turtle as tw

# configuramos el mundo de tortugas
tw.bgpic( "Laberinto.png" )
screen = tw.Screen()
screen.setup( 800, 600 )
screen.title( "Actividad 03" )

# creamos una tortuga
tortuga = tw.Turtle()
tortuga.shape( 'turtle' )
tortuga.setheading( 90 )
tortuga.speed( 4 )

# la preparamos para dibujar
tortuga.pensize( 6 )
tortuga.pencolor( "#FF0000" )
tortuga.setheading( 180 )

# dibujamos la solución
tortuga.penup()
tortuga.goto( 250, -200 )
tortuga.pendown()

tortuga.forward( 450 )
tortuga.setheading( 90 )
tortuga.forward(200)
tortuga.right(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)
tortuga.penup()

# eso es todo
tw.done()
