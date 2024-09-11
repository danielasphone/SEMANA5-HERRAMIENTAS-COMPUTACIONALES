# Proyecto de Juegos en Python con Turtle Graphics

## Descripción

Este proyecto es una colección de cinco juegos creados con Turtle Graphics utilizando Python. Cada uno de estos juegos ha sido modificado o mejorado para demostrar una variedad de técnicas y habilidades de programación así como herramientas. A continuación, te daré una explicación de lo que hace en cada juego.

## Juegos

### 1. **Paint**

**Descripción**: Una aplicación de dibujo básica, te permite crear gráficos y formas en una ventana de gráficos de Turtle. Puedes personalizar tus imágenes seleccionando entre la variedad de colores y herramientas.

**Características**:
- Selección de colores.
- Herramientas para dibujar líneas, círculos, rectángulos y triángulos.
- Tiene una interfaz fácil de usar que le permite cambiar rápidamente entre varios modos de dibujo.

**Código de Referencia**: [Paint en Grant Jenks](http://www.grantjenks.com/docs/freegames/paint.html)

### 2. **Snake**

**Descripción**: Es el juego de serpientes tradicional en el que manejas una serpiente que crece a medida que come la comida que aparece en la pantalla. El objetivo es evitar chocar contra la pantalla o contra ti mismo.

**Características**:
- Movimiento continuo de la serpiente.
- Generación aleatoria de comida.
- Cambio de colores para la serpiente y la comida (NO ROJO).

**Código de Referencia**: [Snake en Grant Jenks](http://www.grantjenks.com/docs/freegames/snake.html)

### 3. **Pacman**

**Descripción**: Es un juego de Pacman tradicional en el que maneja a Pacman en un laberinto y trata de comer todos los puntos mientras evita a los fantasmas. Se han hecho ajustes para cambiar el comportamiento de los fantasmas y el diseño del tablero.

**Características**:
- Modificación del tablero del juego.
- Aumento de la velocidad de los fantasmas.
- Mejora en la inteligencia de los fantasmas.

**Código de Referencia**: [Pacman en Grant Jenks](http://www.grantjenks.com/docs/freegames/pacman.html)

### 4. **Tiro Parabólico**

**Descripción**: Juego en el que manejas un arma de fuego que dispara proyectiles a varios objetivos en movimiento. Se han agregado mejoras, como la velocidad de los proyectiles y la capacidad de que se repongan los objetivos cuando salen de la pantalla.

**Características**:
- Aumento en la velocidad del proyectil y los objetivos.
- Los objetivos se reposicionan al salir de la pantalla.

**Código de Referencia**: [Cannon en Grant Jenks](http://www.grantjenks.com/docs/freegames/cannon.html)

### 5. **Memory**

**Descripción**: Juego de memoria en el que debes emparejar pares de cartas. Se han agregado mejoras, como contar cuántas veces tocas la pantalla, reconocer cuando todas las cartas se han destapado y mostrar el número de toques en la pantalla. El contenido de las cartas también se ha actualizado al reemplazar los números por iconos y símbolos.

**Características**:
- Contador de taps.
- Detección de cuando todos los cuadros están destapados.
- Cambio de contenido de los cuadros a iconos y símbolos.

**Código de Referencia**: [Memory en Grant Jenks](http://www.grantjenks.com/docs/freegames/memory.html)

## Requisitos 

1. **Instalar Python**:
   - Asegúrate de tener Python 3.6 para arriba. Descargalo desde [python.org](https://www.python.org/downloads/).

2. **Instalar Free Python Games**:
   - Utiliza `pip` para instalar la biblioteca Free Python Games:
     ```bash
     python3 -m pip install freegames
     ```