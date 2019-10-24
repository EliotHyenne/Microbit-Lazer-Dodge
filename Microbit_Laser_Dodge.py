import microbit
import random

grid = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
gameLost = False
score = 0

def getScore():
    return score

def resetScore():
    global score
    score = 0

def displayGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            microbit.display.set_pixel(j, i, grid[i][j])

def clearGrid():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = 0;

def displayCursor(x, y):
    if grid[y][x] == 0:
        grid[y][x] = 9
        displayGrid()
        grid[y][x] = 0
    else:
        lost(x, y)

def displayEnemy(x, y):
    grid[y][x] = 5

def removeEnemy(x, y):
    grid[y][x] = 0

def lost(x, y):
    gameLost = True

    while gameLost:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = 9
        grid[y][x] = 0
        displayGrid()
        microbit.sleep(250)
        clearGrid()
        displayGrid()
        microbit.sleep(250)

        if (microbit.button_a.was_pressed()):
            microbit.display.scroll("Score: " + str(getScore()), wait=True, loop=False)
            resetScore()
            gameLost = False

def wait():
    for i in range(25):
        microbit.sleep(5)
        updatePos()

def moveEnemy():
    #Top left corner
    if grid[0][0] == 5:
        displayEnemy(0, 0)
        wait()
        removeEnemy(0, 0)
        for pos in range(1, 5):
            displayEnemy(pos, pos)
            wait()
            removeEnemy(pos, pos)

    #Top right corner
    if grid[0][4] == 5:
        displayEnemy(4, 0)
        wait()
        removeEnemy(4, 0)
        for i in range(1,5):
            displayEnemy(4-i, i)
            wait()
            removeEnemy(4-i, i)

    #Bottom left corner
    if grid[4][0] == 5:
        displayEnemy(0, 4)
        wait()
        removeEnemy(0, 4)
        for i in range(1,5):
            displayEnemy(i, 4-i)
            wait()
            removeEnemy(i, 4-i)

    #Bottom right corner
    if grid[4][4] == 5:
        displayEnemy(4, 4)
        wait()
        removeEnemy(4, 4)
        for pos in range(3, -1, -1):
            displayEnemy(pos, pos)
            wait()
            removeEnemy(pos, pos)

    #Top row
    for i in range(1, 4):
        if grid[0][i] == 5:
            displayEnemy(i, 0)
            wait()
            removeEnemy(i, 0)
            for pos in range(1, 5):
                displayEnemy(i, pos)
                wait()
                removeEnemy(i, pos)

    #Bottom row
    for i in range(1, 4):
        if grid[4][i] == 5:
            displayEnemy(i, 4)
            wait()
            removeEnemy(i, 4)
            for pos in range(3, -1, -1):
                displayEnemy(i, pos)
                wait()
                removeEnemy(i, pos)

    #Left side
    for i in range(1, 4):
        if grid[i][0] == 5:
            displayEnemy(0, i)
            wait()
            removeEnemy(0, i)
            for pos in range(1, 5):
                displayEnemy(pos, i)
                wait()
                removeEnemy(pos, i)

    #Right side
    for i in range(1, 4):
        if grid[i][4] == 5:
            displayEnemy(4, i)
            wait()
            removeEnemy(4, i)
            for pos in range(3, -1, -1):
                displayEnemy(pos, i)
                wait()
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

while not gameLost:
    updatePos()
    createEnemy()
    score += 1
    moveEnemy()
