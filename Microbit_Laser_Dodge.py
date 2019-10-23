import microbit
import random

grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

def displayGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            microbit.display.set_pixel(j, i, grid[i][j])

def displayCursor(x, y):
    grid[y][x] = 9
    displayGrid()
    grid[y][x] = 0

def displayEnemy(x, y):
    grid[y][x] = 5
    displayGrid()

def removeEnemy(x, y):
    grid[y][x] = 0

def moveEnemy():
    if grid[0][0] == 5:
        displayEnemy(0, 0)
        for wait in range(25):
            microbit.sleep(5)
            updatePos()
        removeEnemy(0, 0)
        for pos in range(1, 5):
            displayEnemy(pos, pos)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(pos, pos)

    if grid[0][4] == 5:
        displayEnemy(4, 0)
        for wait in range(25):
            microbit.sleep(5)
            updatePos()
        removeEnemy(4, 0)
        for i in range(1,5):
            displayEnemy(4-i, i)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(4-i, i)

    if grid[4][0] == 5:
        displayEnemy(0, 4)
        for wait in range(25):
            microbit.sleep(5)
            updatePos()
        removeEnemy(0, 4)
        for i in range(1,5):
            displayEnemy(i, 4-i)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(i, 4-i)

    if grid[4][4] == 5:
        displayEnemy(4, 4)
        for wait in range(25):
            microbit.sleep(5)
            updatePos()
        removeEnemy(4, 4)
        for pos in range(3, -1, -1):
            displayEnemy(pos, pos)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(pos, pos)

    for i in range(1, 4):
        if grid[0][i] == 5:
            displayEnemy(i, 0)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(i, 0)
            for pos in range(1, 5):
                displayEnemy(i, pos)
                for wait in range(25):
                    microbit.sleep(5)
                    updatePos()
                removeEnemy(i, pos)

    for i in range(1, 4):
        if grid[4][i] == 5:
            displayEnemy(i, 4)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(i, 4)
            for pos in range(3, -1, -1):
                displayEnemy(i, pos)
                for wait in range(25):
                    microbit.sleep(5)
                    updatePos()
                removeEnemy(i, pos)

    for i in range(1, 4):
        if grid[i][0] == 5:
            displayEnemy(0, i)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(0, i)
            for pos in range(1, 5):
                displayEnemy(pos, i)
                for wait in range(25):
                    microbit.sleep(5)
                    updatePos()
                removeEnemy(pos, i)

    for i in range(1, 4):
        if grid[i][4] == 5:
            displayEnemy(4, i)
            for wait in range(25):
                microbit.sleep(5)
                updatePos()
            removeEnemy(4, i)
            for pos in range(3, -1, -1):
                displayEnemy(pos, i)
                for wait in range(25):
                    microbit.sleep(5)
                    updatePos()
                removeEnemy(pos, i)

def createEnemy():
    side = random.randint(0, 4)
    place = random.randint(0, 4)

    if(side == 0):
        displayEnemy(place, 0)
    elif(side == 1):
        displayEnemy(4, place)
    elif(side == 2):
        displayEnemy(place, 4)
    elif(side == 3):
        displayEnemy(0, place)

def updatePos():
    x = 2
    y = 2

    if (microbit.accelerometer.get_x() <= -550):
        x = 0
    elif (-550 < microbit.accelerometer.get_x() <= -250):
        x = 1
    elif (-250 < microbit.accelerometer.get_x() <= 250):
        x = 2
    elif (250 < microbit.accelerometer.get_x() <= 550):
        x = 3
    elif (microbit.accelerometer.get_x() > 550):
        x = 4

    if (microbit.accelerometer.get_y() <= -550):
        y = 0
    elif (-550 < microbit.accelerometer.get_y() <= -250):
        y = 1
    elif (-250 < microbit.accelerometer.get_y() <= 250):
        y = 2
    elif (250 < microbit.accelerometer.get_y() <= 550):
        y = 3
    elif (microbit.accelerometer.get_y() > 550):
        y = 4

    displayCursor(x, y)

while True:
    # for wait in range(100):
    #     microbit.sleep(5)
    #     updatePos()
    updatePos()
    createEnemy()
    moveEnemy()
