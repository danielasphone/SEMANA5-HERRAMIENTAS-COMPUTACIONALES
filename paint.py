from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Se renombro funcion "circle" a "draw_circle" para evitar conflictos con la funcion "circle" de la biblioteca turtle
#Calcula radio basandose en la distancia entre start y end y utiliza funcion circle de turtle para dibujarlo
def draw_circle(start, end):
    "Draw circle from start to end."
    # Calcula radio 
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    
    up()
    # ajustamos punto inicial para dibujar circulo 
    goto(start.x, start.y - radius)
    down()
    
    begin_fill()
    circle(radius)  # usar circle de turtle para dibujar el circulo
    end_fill()

#Utilizamos punto "start" como una esquina y "end" como esquina opuesta 
#Se crean 4 lados usando un bucle 
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()  # Levanta el lapiz
    goto(start.x, start.y)  # Mueve el cursor al punto inicial
    down()  # Baja el lapiz para dibujar
    begin_fill() # Comienza a rellenar la forma

    #Dibuja rectangulo completando los 4 lados
    for cout in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

#Usa punto "start" como primer vertice y "end" para definir base, luego se completan los 3 lados
def triangle(start, end):
    "Draw triangle from start to end."
    up()  # Levanta el lapiz
    goto(start.x, start.y) # Mueve el cursor al punto inicial
    down() # Baja el lapiz para dibujar
    begin_fill() # Comienza a rellenar la forma

    #Dibuja un triangulo completando los 3 lados 
    for count in range(3): 
        forward(end.x - start.x) # Dibuja un lado del triangulo
        left(120) # Gira 120 grados a la izquierda para formar el angulo del triangulo

    end_fill() # Termina de rellenar el triangulo

#Determina si el usuario esta comenzando una nueva figura o si ya termino de definir la forma 
def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y) # Almacena punto inicio 
    else:
        shape = state['shape'] # Obtiene la forma que se va a dibujar
        end = vector(x, y)
        shape(start, end) #Llama funcion de figura seleccionada 
        state['start'] = None # Resetea el punto de inicio despues de dibujar

def store(key, value):
    "Store value in state at key."
    state[key] = value # Guarda valor en diccionario

# Diccionario: almacena el estado de inicio y la forma actual seleccionada
state = {'start': None, 'shape': line}
#Tamaño de la ventana de dibujo
setup(420, 420, 370, 0)
# Detecta clics en pantalla para iniciar el dibujo, asigna funcion tap a clic mouse
onscreenclick(tap)
listen()

# Asignacion de teclas para deshacer y cambiar colores
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Asignacion de teclas para seleccionar las formas a dibujar
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done() # Finaliza el programa y cierra la ventana
