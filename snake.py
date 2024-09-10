from turtle import *
from random import randrange
from freegames import square, vector

# Se inicializa la comida, la serpiente y la direccion
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    "Move food randomly one step within the window."
    food_move = vector(randrange(-1, 2) * 10, randrange(-1, 2) * 10)
    new_food = food + food_move
    if inside(new_food):
        food.move(food_move)

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red') # Mostrar cabeza en rojo si la serpiente choca
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')  # Dibujar cada parte del cuerpo de la serpiente

    square(food.x, food.y, 9, 'green') # Dibujar la comida
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
move()
done()