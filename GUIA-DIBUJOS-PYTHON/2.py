import turtle as world
import Utils

# funcion/subrutina principal normalmente llamada 'main'
def main():
    global win, pen

    # inicializa el juego
    init()

    # dibujamos
    ang1 = 75
    ang2 = 0
    ang3 = -60
    ang4 = -154
    ang5 = -50
    r = 150
    x = -38
    y = 0

    pen.color( "black", "yellow" )
    pen.goto( x, y )
    #pen.begin_fill()
    pen.down()

    #punta
    pen.setheading( ang1 )
    pen.forward( r )
    pen.right (150)
    pen.forward (r)

    #puntaDerecha
    pen.setheading( ang2 )
    pen.forward( r )
    pen.right (145)
    pen.forward (r)

    #puntaAbajoDerecha
    pen.setheading( ang3 )
    pen.forward( r )
    pen.right (145)
    pen.forward (155)

    #puntaAbajoDerecha
    pen.setheading( ang4 )
    pen.forward( r )
    pen.right (145)
    pen.forward (150)
    
    #puntaIzquierda
    pen.setheading( ang5 )
    pen.left (-165)
    pen.forward( r )
    pen.right(145)
    pen.forward(148)
  
  
    pen.end_fill()
    pen.up()

    pen.goto( x, y + r/2 )
    pen.down()
    #pen.dot(10)
    pen.up()

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
    #win.tracer( 0, 0 )                                    # para dibujar ultra rapido
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
