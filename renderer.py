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

vertexList = [[ 2,-2, 4],           #XYZ
              [ 2, 2, 4],
              [-2,-2, 4],
              [-2, 2, 4],
              [ 2,-2, 6],
              [ 2, 2, 6],
              [-2,-2, 6],
              [-2, 2, 6]]

triangleList = [[1,2,3],
                [2,3,4],
                [5,6,7],
                [6,7,8],
                [1,3,5],
                [3,5,6],
                [2,4,6],
                [4,6,8],
                [1,2,5],
                [2,5,6],
                [3,4,7],
                [4,7,8]]

triangleNumber = len(triangleList)
vertexNumber = len(vertexList)

screenX = []
screenY = []
skips = []

mult = 100
screenDistance = 0
focalDistance = 3

nugeAmount = 0.25


def drawTriangle(x):
    dw.goto(-screenY[triangleList[x][0] - 1], -screenX[triangleList[x][0]  - 1])
    dw.down()
    if triangleFill == True:
        dw.begin_fill()
    dw.goto(-screenY[triangleList[x][1] - 1], -screenX[triangleList[x][1] - 1])
    dw.goto(-screenY[triangleList[x][2] - 1], -screenX[triangleList[x][2] - 1])
    dw.goto(-screenY[triangleList[x][0] - 1], -screenX[triangleList[x][0] - 1])
    dw.up()
    if triangleFill == True:
        dw.end_fill()




def render():

    dw.clear()
    turtle.bgcolor('black')
    turtle.tracer(0, 0)
    screenX.clear()
    screenY.clear()
    skips.clear()
    for i in range(vertexNumber):
        tDistance =  screenDistance + focalDistance + vertexList[i][2]
        if tDistance <= 0:
            skips.append(i)
            screenX.append(0)
            screenY.append(0)
            continue

        screenX.append(-mult*((vertexList[i][0]*focalDistance)/(focalDistance+vertexList[i][2])))
        screenY.append(-mult*((vertexList[i][1]*focalDistance)/(focalDistance+vertexList[i][2])))

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
        print('drawing triangle', i + 1)
        drawTriangle(i)
        dw.up()
        turtle.update()

render()

while True:
    renderDo = 0
    if keyboard.is_pressed('a'):
        for i in range(vertexNumber):
            vertexList[i][1] = vertexList[i][1] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('d'):
        for i in range(vertexNumber):
            vertexList[i][1] = vertexList[i][1] - nugeAmount
            renderDo+=1
    if keyboard.is_pressed('s'):
        for i in range(vertexNumber):
            vertexList[i][0] = vertexList[i][0] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('w'):
        for i in range(vertexNumber):
            vertexList[i][0] = vertexList[i][0] - nugeAmount
            renderDo+=1
    if keyboard.is_pressed('f'):
        for i in range(vertexNumber):
            vertexList[i][2] = vertexList[i][2] + nugeAmount
            renderDo+=1
    if keyboard.is_pressed('r'):
        for i in range(vertexNumber):
            vertexList[i][2] = vertexList[i][2] - nugeAmount
            renderDo+=1    
    if renderDo > 0:
        render()
        renderDo = 0








