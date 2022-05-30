import time
import threading
import turtle


class KeyPress():
    def __init__( self, win, key_name ):
        self._down = False

        win.onkeypress( self._press, key_name )
        win.onkeyrelease( self._release, key_name )

    def _press( self ):
        self._down = True

    def _release( self ):
        self._down = False

    def pressed( self ):
        return self._down


class MousePress():
    def __init__( self, win, button ):
        self._down = False
        self._x = None
        self._y = None
        self._lock = threading.Lock()

        win.onclick( self._press, button )
        win.onclick( self._release, button )

    def _press( self, x, y ):
        self._lock.acquire()
        self._down = True
        self._x = x
        self._y = y
        self._lock.release()

    def _release( self, x, y ):
        self._lock.acquire()
        self._down = False
        self._x = x
        self._y = y
        self._lock.release()

    def pressed( self ):
        if( self._down ):
            self._lock.acquire()
            r = self._down, self._x, self._y
            self._lock.release()
            return r
        else:
            return None

class Rectangle():
    def __init__(self, x, y, ancho, alto ):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto

    def colisiona( self, turtle ):
        self_x1 = self.x
        self_y1 = self.y
        self_x2 = self_x1 + self.ancho - 1
        self_y2 = self_y1 + self.alto - 1

        turtle_x1 = turtle.xcor() - int( turtle.ancho/2 )
        turtle_y1 = turtle.ycor() - int( turtle.alto/2 )
        turtle_x2 = turtle_x1 + turtle.ancho - 1
        turtle_y2 = turtle_y1 + turtle.alto - 1

        return self_x1 <= turtle_x2 and \
               turtle_x1 <= self_x2 and \
               self_y1 <= turtle_y2 and \
               turtle_y1 <= self_y2


_tick_prev = 0
def tick( win, fps ):
    global _tick_prev

    if( _tick_prev == 0 ):
        _tick_prev = time.time()

    #while( time.time() - _tick_prev < 1/fps ):
    #    win.update()
    tickExpected = 1.0 / fps;
    tickElapsed = time.time() - _tick_prev;
    if (tickElapsed < tickExpected):
        time.sleep( tickExpected - tickElapsed );

    now = time.time()
    dt = now - _tick_prev
    _tick_prev = now
    return dt


def colisiona( turtle1, turtle2 ):
    turtle1_x1 = turtle1.xcor() - int( turtle1.ancho/2 )
    turtle1_y1 = turtle1.ycor() - int( turtle1.alto/2 )
    turtle1_x2 = turtle1_x1 + turtle1.ancho - 1
    turtle1_y2 = turtle1_y1 + turtle1.alto - 1

    turtle2_x1 = turtle2.xcor() - int( turtle2.ancho/2 )
    turtle2_y1 = turtle2.ycor() - int( turtle2.alto/2 )
    turtle2_x2 = turtle2_x1 + turtle2.ancho - 1
    turtle2_y2 = turtle2_y1 + turtle2.alto - 1

    return turtle1_x1 <= turtle2_x2 and \
           turtle2_x1 <= turtle1_x2 and \
           turtle1_y1 <= turtle2_y2 and \
           turtle2_y1 <= turtle1_y2


def update( win ):
    try:
        win.update()
        return True
    except turtle.Terminator:
        return False
