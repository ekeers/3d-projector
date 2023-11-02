import turtle
import time
import keyboard
triangleFill = False
turtle.bgcolor('black')

dw = turtle.Turtle()
dw.hideturtle()
dw.color('green')
#dw.speed(0)
turtle.tracer(0, 0)

vertexX = [ 2, 2,-2,-2, 2, 2,-2,-2]
vertexY = [-2, 2,-2, 2,-2, 2,-2, 2]
vertexZ = [ 2, 2, 2, 2, 4 ,4 ,4 ,4]

triangleA = [1,2,5,6,1,5,2,6,1,2,3,4]
triangleB = [2,3,6,7,5,3,6,4,2,5,4,7]
triangleC = [3,4,7,8,3,7,4,8,5,6,7,8]

triangleNumber = len(triangleA)
vertexNumber = len(vertexX)

screenX = []
screenY = []
skips = []

mult = 100
screenDistance = 0
focalDistance = 3

nugeAmount = 0.25


def drawTriangle(x):
    dw.goto(-screenY[triangleA[x] - 1], -screenX[triangleA[x] - 1])
    dw.down()
    if triangleFill == True:
        dw.begin_fill()
    dw.goto(-screenY[triangleB[x] - 1], -screenX[triangleB[x] - 1])
    dw.goto(-screenY[triangleC[x] - 1], -screenX[triangleC[x] - 1])
    dw.goto(-screenY[triangleA[x] - 1], -screenX[triangleA[x] - 1])
    dw.up()
    if triangleFill == True:
        dw.end_fill()

if len(vertexY) != vertexNumber or len(vertexZ) != vertexNumber:
    print('error, missing or extra cordinates given')
    print('x:', + len(vertexX))
    print('y:', + len(vertexY))
    print('z:', + len(vertexZ))
    exit()

if triangleNumber != len(triangleB) or triangleNumber != len(triangleC):
    print('error, mising or extra cordinates for lines given')
    print('cordenadas A:', + len(triangleA))
    print('cordenadas B:', + len(triangleB))
    print('cordenadas C:', + len(triangleC))
    exit()

def render():
    global vertexY
    global vertexX
    global screenDistance
    dw.clear()
    turtle.bgcolor('black')
    turtle.tracer(0, 0)
    screenX.clear()
    screenY.clear()
    skips.clear()
    for i in range(vertexNumber):
        tDistance =  screenDistance + focalDistance + vertexZ[i]
        if tDistance <= 0:
            skips.append(i)
            screenX.append(0)
            screenY.append(0)
            continue

        screenX.append(-mult*((vertexX[i]*focalDistance)/(focalDistance+vertexZ[i])))
        screenY.append(-mult*((vertexY[i]*focalDistance)/(focalDistance+vertexZ[i])))

    for i in range(vertexNumber):
        if i in skips:
            print('skiped vertex', + i)
            continue
        dw.color('green')
        print('vertex', + i+1, 'of', + vertexNumber)
        print('X:', + screenX[i])
        print('Y:', + screenY[i])
        dw.up()
        dw.goto(-screenY[i], -screenX[i])
        dw.dot()
    dw.color('blue')
    for i in range(triangleNumber):
        print('tracing line', i + 1)
        drawTriangle(i)
        dw.up()
        turtle.update()

render()

while True:
    renderDo = 0
    if keyboard.is_pressed('a'):
        for i in range(vertexNumber):
            vertexY[i] = vertexY[i] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('d'):
        for i in range(vertexNumber):
            vertexY[i] = vertexY[i] - nugeAmount
            renderDo+=1
    if keyboard.is_pressed('s'):
        for i in range(vertexNumber):
            vertexX[i] = vertexX[i] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('w'):
        for i in range(vertexNumber):
            vertexX[i] = vertexX[i] - nugeAmount
            renderDo+=1
    if keyboard.is_pressed('f'):
        for i in range(vertexNumber):
            vertexZ[i] = vertexZ[i] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('r'):
        for i in range(vertexNumber):
            vertexZ[i] = vertexZ[i] - nugeAmount
            renderDo+=1    
    if renderDo > 0:
        render()
        renderDo = 0








