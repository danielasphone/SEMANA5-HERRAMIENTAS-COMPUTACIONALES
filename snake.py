from turtle import *
from random import randrange
from freegames import square, vector

# Se inicializa la comida, la serpiente y la direccion
food = vector(0, 0) # comida comienza en esa posicion 
snake = [vector(10, 0)] # serpiente empieza con un segmento en esa posicion
aim = vector(0, -10) # direccion inicial es hacia abajo

# Lista de colores (NO ROJO)
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Asignar colores aleatorios a serpiente y comida
snake_color = colors[randrange(0, len(colors))]
food_color = colors[randrange(0, len(colors))]

# Asegurar que comida y serpiente no tengan el mismo color
while food_color == snake_color:
    food_color = colors[randrange(0, len(colors))] # Reasignar color hasta que sea diferente

def change(x, y):
    "Change snake direction."
    # Cambia la direccion en la que se mueve la serpiente
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    #para verificar que serpiente este dentro de limites de ventana 
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food randomly one step within the window."
    # Mueve comida de manera aleatoria un paso (10 unidades) dentro de la ventana
    food_move = vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10) # Movimiento aleatorio
    new_food = food + food_move # Calcula nueva posicion
    if inside(new_food): # Solo mueve si la nueva posicion esta dentro de los limites
        food.move(food_move)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

 # Verifica si la serpiente se ha salido de los limites o  mordido a si misma
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red') # Mostrar cabeza en rojo si la serpiente choca
        update()
        return # termina juego si ocurre colision

    snake.append(head)

  # Verifica si serpiente ha comido la comida
    if head == food:
        print('Snake:', len(snake)) # Muestra tamaño actual de serpiente en terminal
        # Reubica comida en nueva posicion aleatoria
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0) # Si no come moverse sin crecer

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)  # Dibujar la serpiente y con el color asignado

    square(food.x, food.y, 9, food_color) # Dibujar la comida y con el color asignado
    move_food()  # Llamar a la funcion para mover la comida
    update()
    ontimer(move, 100) # Configurar el temporizador para mover la serpiente

# Configuracion inicial del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right') # Cambiar direccion a derecha
onkey(lambda: change(-10, 0), 'Left') # Cambiar direccion a izquierda
onkey(lambda: change(0, 10), 'Up') # Cambiar direccion hacia arriba
onkey(lambda: change(0, -10), 'Down') # Cambiar direccion hacia abajo 
move() # Inicia movimiento de serpiente
done()