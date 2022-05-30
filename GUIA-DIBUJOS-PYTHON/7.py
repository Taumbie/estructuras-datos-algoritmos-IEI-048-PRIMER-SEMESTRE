import turtle as world
import Utils

# funcion/subrutina principal normalmente llamada 'main'
def main():
    global win, pen

    # inicializa el juego
    init()

    # dibujamos

    ang = 0
    r = 200
    x = 0
    y = 0
    
    pen.speed(10)
    pen.color( "white" )
    pen.goto(0, 0 )
    pen.dot( 1000 )
    pen.color( "red" )
    pen.goto( x, y )
    pen.begin_fill()
    pen.down()

    pen.setheading( ang )
    pen.forward( r )
    pen.setheading( 90 + ang )
    pen.circle( r, 180 - ang*2)
    pen.goto( x, y  )

    pen.end_fill()
    pen.up()
    #Parte de abajo
    pen.down()
    pen.color( "black" )
    pen.setheading( ang )
    pen.forward( r )
    pen.setheading( 90 + ang )
    pen.circle( r, -180 - ang*2)
    pen.goto( x, y  )

    pen.up()
    pen.goto( x, y + r/2)
    pen.up()
    #Circulo central
    ang = 0
    r = 30
    x = 0
    y = 0
    
    pen.goto( 30, 0 )
    pen.down()
    pen.right(270)
    pen.left(90)
    pen.circle( r, 360 - ang*2)

    #Circulo Externo
    ang = 0
    r = 50
    x = 0
    y = 0
    
    pen.goto( 50, 0 )
    pen.down()
    pen.circle( r, 360 - ang*2)
    pen.up()
    
    pen.color( "black" )
    pen.goto( 0, 0)
    pen.dot (100)
    pen.color( "white" )
    pen.down()
    pen.goto(0, 0 )
    pen.dot(90)

    pen.color( "black" )
    pen.goto( 0, 0)
    pen.dot(50)

    pen.color( "white" )
    pen.goto( 0, 0)
    pen.dot(42)
    # Esperamos por la tecla ESC o a que cierren la ventana
    waitForExit()

    # game over
    world.bye()
    print( "Eso es todo amigos!!!" )

# funcion/subrutina para inicializar los elementos del programa
def init():
    global win, pen, k_esc

    # configuramos el mundo de tortugas
    win = world.Screen()                                # acceso a la ventana
    #win.tracer( 0, 0 )                                  # para dibujar ultra rapido
    win.setup( 800, 600, 100, 100 )                     # tamano de la ventana y posicion
    win.bgcolor( "white" )                              # color de fondo
    win.bgpic( "Grid 800x600.png" )                     # imagen de fondo
    win.title( "Pacman Shape" )                         # titulo

    # una tortuga para dibujar
    pen = world.Turtle()                                # creamos una "tortuga"
    pen.hideturtle()                                    # no queremos que se vea su forma
    pen.up()                                            # lapiz arriba

    # algunos mensajes
    pen.goto(  -70, -280 )
    pen.color( "black" )                                # color para pintar y color de relleno
    pen.write( "Presiona la tecla 'Esc' para salir" )

    # teclas presionadas
    k_esc = Utils.KeyPress( win, 'Escape' )

    # activa la escucha de eventos
    win.listen()


# espera por la tecla ESC o a que se cierre la ventana
def waitForExit():
    global k_esc

    waiting = True
    while( waiting ):
        if( k_esc.pressed() ):
            waiting = False
        elif( Utils.update( win ) == False ):
            waiting = False


# show time
main()
