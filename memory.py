from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯', '🦁', '🐮', '🐷', '🐸', '🐵', '🐔',
         '⚽️', '🏀', '🏈', '⚾️', '🎾', '🏐', '🎱', '🏓', '🚗', '🚕', '✈️', '🚀', '🚁', '🛳', '🚤', '🚲'] * 2 #Contenido de cada cuadro
state = {'mark': None, 'Taps': 0}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        state['Taps'] += 1 #Incremento en el contador de taps
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    if all(not hidden for hidden in hide): #Condicional para verificar si todos los cuadros fueron destapados
        up()
        goto(-100, 0)
        color('green')
        write("Ganaste!", font=('Arial', 30, 'bold'))


    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 7) #Digito centrado
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align="center")
    up()
    goto(-180, 180)
    color('black')
    write(f"Taps: {state['Taps']}", font=('Arial', 15, 'normal')) #Texto que muestra los taps

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
