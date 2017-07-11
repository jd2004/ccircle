import ccircle
import random
import time

cloudX = []
cloudY = []
cloudSize = []
cloudSpeed = []

window = ccircle.Window()
window.toggleMaximized()

bouncyX = []
bouncyY = []
bouncySpeed = []
wind = []


while window.isOpen():
    window.clear(0.0, 0.0, 1.0)
    for i in range(40):
        window.drawRect(0, 650 + i * 5, 1600, 200, 1 - 0.03 * i, 1.0, 0.1)
    for i in range(80):
        cloudX.append(random.randint(1, 1600))
        cloudY.append(random.randint(1, 300))
        cloudSize.append(random.randint(60, 140))
        cloudSpeed.append(random.randint(1, 3))
        window.drawCircle(cloudX[i], cloudY[i], cloudSize[i], 1.0, 1.0, 1.0, 0.3)
        cloudX[i] += cloudSpeed[i]
        if cloudX[i] > 1600:
            cloudX[i] = 1
    for i in range(500000):
        window.hideMouse()
        mouseX, mouseY = window.getMousePos()
        bouncyX.append(random.randint(1, 1600))
        bouncyY.append(random.randint(20, 600))
        bouncySpeed.append(random.randint(1, 3))
        wind.append(random.randint(-2, 2))
        if ccircle.isMouseDown('left') and bouncyY[i] - 15 <= mouseY <= bouncyY[i] + 15:
            bouncySpeed[i] = bouncySpeed[i] + 6
            if bouncyX[i] + 15 >= mouseX >= bouncyX[i]:
                wind[i] = wind[i] + 10
            if bouncyX[i] - 15 <= mouseX < bouncyX[i]:
                wind[i] = wind[i] - 10
            '''if bouncyY[i] + 15 >= mouseX >= bouncyY[i]:
               bouncySpeed[i] = bouncySpeed[i] + 6
            if bouncyY[i] - 15 <= mouseX < bouncyY[i]:
               bouncySpeed[i] = bouncySpeed[i] + 6'''
        bouncyX[i] = bouncyX[i] + wind[i]
        bouncySpeed[i] = bouncySpeed[i] + 0.1
        if bouncyY[i] < 650:
            bouncyY[i] = bouncyY[i] + bouncySpeed[i]
        elif bouncyY[i] >= 650:
            bouncySpeed[i] = bouncySpeed[i] * -0.95
            bouncyY[i] = bouncyY[i] + bouncySpeed[i]
        if bouncyX[i] > 1600:
            wind[i] = -wind[i]
        if bouncyX[i] < 0:
            wind[i] = -wind[i]
        wind[i] = wind[i] * 0.95
        window.drawCircle(bouncyX[i], bouncyY[i], 30, 1.0, 0.3, 0.3)
        window.drawCircle(bouncyX[i] - 3, bouncyY[i], 27, 1.0, 0.0, 0.0)
        window.drawCircle(bouncyX[i] - 5, bouncyY[i], 24, 0.8, 0.0, 0.0)
        window.drawCircle(mouseX, mouseY, 30, 0.3, 1.0, 0.3)
        window.drawCircle(mouseX - 3, mouseY, 27, 0.0, 1.0, 0.0)
        window.drawCircle(mouseX - 5, mouseY, 24, 0.0, 0.8, 0.0)
    window.update()
