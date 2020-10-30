# Actividad 5: Juego de Memorama

Este trabajo consiste en un juego de tiro parabólico, donde el jugador selcciona uno de los cuadrados de la pantalla, observa el número/carácter que aparece e intenta encontrar su par. Con cada par que se descubra se ira revelando la imagen detrás. En general, es un juego de entretenimiento, que puede servir como una buena forma de pasar el tiempo o de mejorar las habilidades de programación de quienes lo usan.

El juego se puede ejecutar desde cualquier lugar donde se pueda instalar Python, sea en una computadora Windows, Mac OS o Linux. 

El código inicial para este juego fue recuperado de: http://www.grantjenks.com/docs/freegames/memory.html 

# Requisitos
Tener la version de Python 2.7 en adelante

# Instalación
Para poder utilizar este código es necesaria la instalación de las siguientes librerias de Python
```shell
from random import *
from turtle import *
from freegames import path
```
Estas líneas de código son necesarias para correr correctamente el código.
Para mayor información sobre la librería Turtle puede consultar la página : https://docs.python.org/3/library/turtle.html

# Desarrollando
Puede crear una copia de este repositorio usando el comando de Git
```shell
git clone https://github.com/MajoDiaz/Memorama.git
```
Una vez creado la copia, puede porceder a trabajar sobre este repositorio creando su propia rama.

# Características del juego
* Lo primero que debe de aparecer al correr este código es una ventana de juego. Esta ventana esta dividida en cuadrados. Al seleccionar uno de los cuadrados aparece un número/carácter que el jugador deberá de ir memorizando para poder encontrar la imagen escondida.
* El objetivo de este juego es encontrar todos los pares. Una vez encontrados los pares el juego se detendrá.
* Se puede modificar el tamaño de los números/carácteres y el color de estos.

# Contribuciones
Si le gustaría contribuir, por favor haga un fork del repositorio y utilice una rama. Las solicitudes de pull son igualmente bienvenidas.
