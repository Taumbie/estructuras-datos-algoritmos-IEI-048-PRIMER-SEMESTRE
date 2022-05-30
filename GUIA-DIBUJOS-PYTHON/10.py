import turtle as world
import Utils

# funcion/subrutina principal normalmente llamada 'main'
def main():
    global win, pen

    # inicializa el juego
    init()

    # dibujamos

    x = 0
    y = 0
    
    pen.speed(0)

#capa donde esta el barco
    pen.color( "#4eeff5" )
    pen.begin_fill()
    pen.goto(-400,-80)
    pen.down()
    pen.right (0)
    pen.forward (795)
    pen.right (90)
    pen.forward (90)
    pen.right (90)
    pen.forward (795)
    pen.right (90)
    pen.forward (90)
    pen.end_fill()
    pen.up ()

#capa de "arena"
    pen.goto(-400,-170)
    pen.down ()
    pen.color ("#f8fac3")
    pen.begin_fill()
    pen.right (90)
    pen.forward (795)
    pen.right (90)
    pen.forward (70)
    pen.right (90)
    pen.forward (795)
    pen.right (90)
    pen.forward (70)
    pen.end_fill()
    pen.up()

#capa chikitita
    pen.goto(-400,-240)
    pen.down ()
    pen.color ("#4eeff5")
    pen.begin_fill()
    pen.right(90)
    pen.forward (795)
    pen.right (90)
    pen.forward (5)
    pen.right (90)
    pen.forward (795)
    pen.right (90)
    pen.forward (5)
    pen.end_fill()
    pen.up()

#ultima capa
    pen.goto(-400,-245)
    pen.down ()
    pen.color ("#3361f5")
    pen.begin_fill()
    pen.right(90)
    pen.forward (795)
    pen.right (90)
    pen.forward (40)
    pen.right (90)
    pen.forward (795)
    pen.right (90)
    pen.forward (40)
    pen.end_fill()
    pen.up()

#barkito UWU
    pen.goto(-40,-90)
    pen.down ()
    pen.color ("#b57002")
    pen.begin_fill()
    pen.right(90)
    pen.forward (80)
    pen.right(90)
    pen.forward (30)
    pen.up
    pen.goto(-40,-90)
    pen.down ()
    pen.forward(30)
    pen.circle(40, 180)
    pen.end_fill()
    

#fondo arriba
    pen.up()
    pen.color ("#095ddb")
    pen.begin_fill()
    pen.goto(-400,-80)
    pen.down()
    pen.right(90)
    pen.forward (795)
    pen.left(90)
    pen.forward (380)
    pen.left(90)
    pen.forward (795)
    pen.left(90)
    pen.forward (380)
    pen.end_fill()


#roca izq
    pen.up()
    pen.color ("#6e7580")
    pen.begin_fill()
    pen.goto(-400,-120)
    pen.down()
    pen.left(98)
    pen.forward (290)
    pen.left(96)
    pen.forward(260)
    pen.left(30)
    pen.forward(180)
    pen.left(45)
    pen.forward(100)
    pen.left(91)
    pen.forward(415)
    pen.end_fill()

#roca der
    pen.up ()
    pen.color ("#6e7580")
    pen.goto(420,-80)
    pen.begin_fill()
    pen.down ()
    pen.right (90)
    pen.forward(320)
    pen.right(105)
    pen.forward(50)
    pen.right(75)
    pen.forward(45)
    pen.left(70)
    pen.forward (60)
    pen.right(70)
    pen.forward(40)
    pen.left(65)
    pen.forward(100)
    pen.right(20)
    pen.forward(170)
    pen.right(20)
    pen.forward (10)#10
    pen.right(115)#115}
    pen.forward(320)
    pen.end_fill()
    pen.up()

#Agua entre rocas
    pen.color( "#061d91" )
    pen.goto(-110,-80)
    pen.begin_fill()
    pen.down()
    pen.left(90)
    pen.forward(210)
    pen.left(73)
    pen.forward(5)
    pen.left(107)
    pen.forward(215)
    pen.left(100)
    pen.forward(5)
    pen.left(90)
    pen.forward(10)
    pen.end_fill()
    pen.up()

#velero
    pen.color( "#6e7580" )
    pen.goto(-5,-90)
    pen.begin_fill()
    pen.down()
    pen.left(80)
    pen.forward(130)
    pen.right(90)
    pen.forward(7)
    pen.right(90)
    pen.forward(130)
    pen.right(90)
    pen.forward(7)
    pen.end_fill()
    pen.up()
    
#bandera
    pen.color( "white" )
    pen.goto(-2.5,-51)
    pen.begin_fill()
    pen.down()
    pen.right(90)
    pen.forward (95)
    pen.right(125)
    pen.forward(100)
    pen.right (120)
    pen.forward(90)
    pen.end_fill()
    pen.up()

#lineaa aestetik izq
    
    pen.color( "#a2a4a8" )
    pen.goto(-350,230)
    pen.down()
    pen.left(85)
    pen.forward(30)
    pen.left (23)
    pen.forward(50)
    pen.right (24)
    pen.forward(30)
    pen.right (7)
    pen.forward(60)
    pen.left (20)
    pen.forward(30)
    pen.left (20)
    pen.forward(60)
    pen.right (30)
    pen.forward(70)
    pen.right (30)
    pen.forward(46)
    pen.up()
    
#lineaa aestetik der

    pen.color( "#a2a4a8" )
    pen.goto(130,-80)
    pen.down()
    pen.left(180)
    pen.forward (20)
    pen.right (45)
    pen.forward (60)
    pen.right (23)
    pen.forward (80)
    pen.left(20)
    pen.forward (80)
    pen.left(20)
    pen.forward (60)
    pen.right (30)
    pen.forward (50)
    
    
    
    





    
    
    

    
    







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
