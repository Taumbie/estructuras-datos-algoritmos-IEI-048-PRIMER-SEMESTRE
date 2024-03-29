import turtle as tw

# configuramos el mundo de tortugas
#tw.bgpic( "Grid 800x600.png" )
screen = tw.Screen()
screen.setup( 800, 600 )
screen.title( "Actividad 01" )

# creamos una tortuga
tortuga = tw.Turtle()
tortuga.shape( 'turtle' )
tortuga.setheading( 90 )
tortuga.speed( 4 )

# la preparamos para dibujar
tortuga.pensize( 4 )
tortuga.pencolor( "#2c0142" )
tortuga.penup()
tortuga.goto( 0, 0 )
tortuga.pendown()

# dibujo 4 cuadrados
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )
tortuga.right( 90 )
tortuga.forward( 100 )

# Reemplazo a la tortuga por una flecha
tortuga.penup()
tortuga.shape( 'arrow' )
tortuga.setheading( 90 )
tortuga.pencolor( "#fc0505" )
tortuga.goto( 200, 200 )
tortuga.pendown()

# dibujamos un circulo
tortuga.circle(50)

# Reemplazo flecha por tortuga
tortuga.penup()
tortuga.shape( 'turtle' )
tortuga.setheading( 90 )
tortuga.pencolor( "#0b5400" )
tortuga.goto( -150, 150 )
tortuga.pendown()

# Dibujo 4 rectangulos
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.right(90)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.right(90)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.right(90)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.right(90)
tortuga.forward(80)
tortuga.right(90)
tortuga.forward(40)
tortuga.penup()

# eso es todo
tw.done()
