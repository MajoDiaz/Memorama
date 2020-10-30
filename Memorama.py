from random import *
from turtle import *
from freegames import path

#A01701879 María José Díaz Sánchez
#A00829556 Santiago Gonzalez Irigoyen
#Este código es un juego de memorama
#30 de octubre de 2020

'''Aquí se inicializa el contandor taps'''
taps = 0
car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
##

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
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
    ''' Se hace global la variable taps para evitar problemas y se le
    suma un 1 por cada tap que haya '''
    global taps
    taps += 1

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    #contar número de cuadrados cubiertos, empezando con 64
    d=64

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
        else:
            #cada vez que se encuentre un cuadrado destapado (se checan todos)
            #se resta uno de 'd'
            d=d-1

    mark = state['mark']

    if mark is not None and hide[mark]:
        '''Aquí se dibuja el número de cada uno de los cuadros'''
        '''Para que los números aparezcan en el centro debemos de
        jugar con la función goto, que es la que mueve el texto
        En este caso se cambio la posicion de x+18.82', y+12 que logro
        centrar mejor el número de los cuadros'''

        x, y = xy(mark)
        up()
        goto(x + 13.82, y + 6)
        color('black')
        lar = ['#','$','%','@','&']
        if tiles[mark] < len(lar):
            write(lar[tiles[mark]], font=('Arial', 30, 'normal'))
        else:
            write(tiles[mark], font=('Arial', 30, 'normal'))

        write(tiles[mark], font=('Arial', 30, 'normal'))

    '''Aqui se ponen las insrticciones para que aparezca el contador
    arriba a la derecha de la pantalla en letras azules'''

    color('blue')
    goto(180,180)
    write(taps)
    update()
    ontimer(draw, 100)
    #cuando se detecten 0 cuadrados cubiertos se cierra el programa
    if d == 0:
        quit()

#Aquí se genera el ambiente del juego
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
