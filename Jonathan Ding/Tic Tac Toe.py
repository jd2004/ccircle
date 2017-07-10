import ccircle
from math import*

window = ccircle.Window()

whoseTurn = 1

grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]

while window.isOpen():
    window.clear(1.0, 1.0, 1.0)
    mouseX, mouseY = window.getMousePos()
    length, height = window.getSize()
    window.drawRect(length / 3 - 3, 0, 6, height, 0, 0, 0)
    window.drawRect(length * 2 / 3 - 3, 0, 6, height, 0, 0, 0)
    window.drawRect(0, height / 3 - 3, length, 6, 0, 0, 0)
    window.drawRect(0, height * 2 / 3 - 3, length, 6, 0, 0, 0)
    if ccircle.isMouseDown('left'):
        if mouseX < length/3:
            if mouseY < height / 3:
                if grid[0] == 0:
                    grid[0] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            elif mouseY < height * 2 / 3:
                if grid[3] == 0:
                    grid[3] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            else:
                if grid[6] == 0:
                    grid[6] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
        elif mouseX < length * 2 / 3:
            if mouseY < height / 3:
                if grid[1] == 0:
                    grid[1] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            elif mouseY < height * 2 / 3:
                if grid[4] == 0:
                    grid[4] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            else:
                if grid[7] == 0:
                    grid[7] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
        else:
            if mouseY < height / 3:
                if grid[2] == 0:
                    grid[2] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            elif mouseY < height * 2 / 3:
                if grid[5] == 0:
                    grid[5] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
            else:
                if grid[8] == 0:
                    grid[8] = whoseTurn % 2 + 1
                    whoseTurn = whoseTurn + 1
    if grid[0] == 2:
        window.drawLine(length / 6 - 30, height / 6 - 30, length / 6 + 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 6 + 30, height / 6 - 30, length / 6 - 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
    if grid[0] == 1:
        window.drawCircle(length / 6, height / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 6, height / 6, 35, 1.0, 1.0, 1.0)
    if grid[1] == 2:
        window.drawLine(length / 2 - 30, height / 6 - 30, length / 2 + 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 2 + 30, height / 6 - 30, length / 2 - 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
    if grid[1] == 1:
        window.drawCircle(length / 2, height / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 2, height / 6, 35, 1.0, 1.0, 1.0)
    if grid[2] == 2:
        window.drawLine(length * 5 / 6 - 30, height / 6 - 30, length * 5 / 6 + 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length * 5 / 6 + 30, height / 6 - 30, length * 5 / 6 - 30, height / 6 + 30, 5, 0.0, 0.0, 0.0)
    if grid[2] == 1:
        window.drawCircle(length * 5 / 6, height / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length * 5 / 6, height / 6, 35, 1.0, 1.0, 1.0)
    if grid[3] == 2:
        window.drawLine(length / 6 - 30, height / 2 - 30, length / 6 + 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 6 + 30, height / 2 - 30, length / 6 - 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
    if grid[3] == 1:
        window.drawCircle(length / 6, height / 2, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 6, height / 2, 35, 1.0, 1.0, 1.0)
    if grid[4] == 2:
        window.drawLine(length / 2 - 30, height / 2 - 30, length / 2 + 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 2 + 30, height / 2 - 30, length / 2 - 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
    if grid[4] == 1:
        window.drawCircle(length / 2, height / 2, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 2, height / 2, 35, 1.0, 1.0, 1.0)
    if grid[5] == 2:
        window.drawLine(length * 5 / 6 - 30, height / 2 - 30, length * 5 / 6 + 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length * 5 / 6 + 30, height / 2 - 30, length * 5 / 6 - 30, height / 2 + 30, 5, 0.0, 0.0, 0.0)
    if grid[5] == 1:
        window.drawCircle(length * 5 / 6, height / 2, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length * 5 / 6, height / 2, 35, 1.0, 1.0, 1.0)
    if grid[6] == 2:
        window.drawLine(length / 6 - 30, height * 5 / 6 - 30, length / 6 + 30, height * 5 / 6 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 6 + 30, height * 5 / 6 - 30, length / 6 - 30, height * 5 / 6 + 30, 5, 0.0, 0.0, 0.0)
    if grid[6] == 1:
        window.drawCircle(length / 6, height * 5 / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 6, height * 5 / 6, 35, 1.0, 1.0, 1.0)
    if grid[7] == 2:
        window.drawLine(length / 2 - 30, height * 5 / 6 - 30, length / 2 + 30, height * 5 / 6 + 30, 5, 0.0, 0.0, 0.0)
        window.drawLine(length / 2 + 30, height * 5 / 6 - 30, length / 2 - 30, height * 5 / 6 + 30, 5, 0.0, 0.0, 0.0)
    if grid[7] == 1:
        window.drawCircle(length / 2, height * 5 / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length / 2, height * 5 / 6, 35, 1.0, 1.0, 1.0)
    if grid[8] == 2:
        window.drawLine(length * 5 / 6 - 30, height * 5 / 6 - 30, length * 5 / 6 + 30, height * 5 / 6 + 30,
                        5, 0.0, 0.0, 0.0)
        window.drawLine(length * 5 / 6 + 30, height * 5 / 6 - 30, length * 5 / 6 - 30, height * 5 / 6 + 30,
                        5, 0.0, 0.0, 0.0)
    if grid[8] == 1:
        window.drawCircle(length * 5 / 6, height * 5 / 6, 40, 0.0, 0.0, 0.0)
        window.drawCircle(length * 5 / 6, height * 5 / 6, 35, 1.0, 1.0, 1.0)
    window.update()
