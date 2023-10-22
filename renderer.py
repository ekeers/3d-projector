import turtle
import time
import keyboard

turtle.bgcolor('black')

dw = turtle.Turtle()
dw.hideturtle()
dw.color('green')
#dw.speed(0)
turtle.tracer(0, 0)


vX = [ 2, 2,-2,-2, 2, 2,-2,-2]
vY = [-2, 2,-2, 2,-2, 2,-2, 2]
vZ = [2, 2, 2, 2, 4 ,4 ,4 ,4 ]   #no poner negativos o jodes el sistema

lineA = [1,3,5,7,1,2,5,6,1,2,3,4]
lineB = [2,4,6,8,3,4,7,8,5,6,7,8]

lN = 12
vN = len(vX)
svX = []
svY = []


mult = 100
sD = 3
fD = 3

nA = 0.25


def drawLine(x):
    dw.goto(-svY[lineA[x] - 1], -svX[lineA[x] - 1])
    dw.down()
    dw.goto(-svY[lineB[x] - 1], -svX[lineB[x] - 1])


if len(vY) != vN or len(vZ) != vN:
    print('error, missing or extra cordinates given')
    print('x:', + len(vX))
    print('y:', + len(vY))
    print('z:', + len(vZ))
    exit()

if len(lineA) != len(lineB):
    print('error, mising or extra cordinates for lines given')
    print('cordenadas A:', + len(lineA))
    print('cordenadas B:', + len(lineB))
    exit()

def render():
    global vY
    global vX
    global sD
    dw.clear()
    turtle.bgcolor('black')
    turtle.tracer(0, 0)
    svX.clear()
    svY.clear()

    for i in range(vN):
        tDistance =  sD + fD + vZ[i]
        div = tDistance / vZ[i]
        svX.append(mult*(vX[i] / div))
        svY.append(mult*(vY[i] / div))

    for i in range(vN):
        dw.color('green')
        print('vertex', + i+1, 'of', + vN)
        print('X:', + svX[i])
        print('Y:', + svY[i])
        dw.up()
        dw.goto(-svY[i], -svX[i])
        dw.dot()
    dw.color('blue')
    for i in range(lN):
        print('tracing line', i + 1)
        drawLine(i)
        dw.up()
        turtle.update()




render()

while True:
    if keyboard.is_pressed('d'):
        for i in range(vN):
            vY[i] = vY[i] + nA
        render()
    if keyboard.is_pressed('a'):
        for i in range(vN):
            vY[i] = vY[i] - nA
        render()
    if keyboard.is_pressed('w'):
        for i in range(vN):
            vX[i] = vX[i] + nA
        render()
    if keyboard.is_pressed('s'):
        for i in range(vN):
            vX[i] = vX[i] - nA
        render()
    if keyboard.is_pressed('f'):
        for i in range(vN):
            sD = sD + nA
        render()
    if keyboard.is_pressed('r'):
        for i in range(vN):
            sD = sD - nA
        render()








