import turtle as world
import Utils

# funcion/subrutina principal normalmente llamada 'main'
def main():
    global win, pen

    # inicializa el juego
    init()

    # dibujamos

    #rectagulo
    pen.color ("black", "white")
    pen.goto(-200,250)
    pen.pensize(3)
    pen.speed(8)
    pen.begin_fill()
    
    #dibujorectagulo
    pen.down()
    pen.forward(400)
    pen.right(90)
    pen.forward(500)
    pen.right(90)
    pen.forward(400)
    pen.right(90)
    pen.forward(500)
    pen.end_fill()
    pen.up()

    #Numeros
    #ochoArriba
    pen.color("red")

    pen.goto(-150,200)
    pen.down()
    pen.circle(10,380)
    pen.up()

    pen.goto(-145,180)
    pen.down()
    pen.circle(15,380)
    pen.up()

    #ochoAbajo
    pen.color("red")
    #circuloPequeño
    pen.goto(160,-180)
    pen.down()
    pen.circle(10,380)
    pen.up()
    #circuloGrande
    pen.goto(160,-200)
    pen.down()
    pen.circle(15,380)
    pen.up()


    #romboPequeños
    pen.color("red")
    ang1 = -315

    pen.goto(-170,135)
    pen.color("red")
    pen.begin_fill()
    pen.down()
    pen.setheading(ang1)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.end_fill()  
    pen.up()

    pen.color("red")
    pen.begin_fill()
    pen.goto(140,-135)
    pen.down()
    pen.setheading(ang1)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.right(90)
    pen.forward(15)
    pen.end_fill()  
    pen.up()

    #rombosGrandes
    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(55, -170)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(55, 0)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(55, 160)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(-100, 160)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()   

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(-100, 0)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()   

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(-100, -170)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up() 

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(-18, -90)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
    pen.up()  

    ang2 = 48
    pen.begin_fill()
    pen.color("red")
    pen.begin_fill()
    pen.goto(-21, 80)
    pen.down()
    pen.setheading(ang2)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.right(90)
    pen.forward(35)
    pen.end_fill()
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
