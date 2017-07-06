import ccircle
from math import*
window = ccircle.Window()
#window.toggleMaximized()
window.hideMouse()

points = []
color='blue'
size=4
cR=0.1
cG=0.5
cB=1.0
while window.isOpen():
    window.clear(0.2,0.2,0.2)
    mX,mY= window.getMousePos()
    if color == 'blue':
        cR = 0.1
        cG = 0.5
        cB = 1.0
    elif color == 'green':
        cR = 0.1
        cG = 0.5
        cB = 0.1
    elif color == 'yellow':
        cR = 1.0
        cG = 1.0
        cB = 0.0
    elif color == 'red':
        cR = 1.0
        cG = 0.0
        cB = 0.0
    elif color == 'black':
        cR = 0.0
        cG = 0.0
        cB = 0.0
    elif color == 'white':
        cR = 1.0
        cG = 1.0
        cB = 1.0
    elif color == 'eraser':
        cR = 0.2
        cG = 0.2
        cB = 0.2
    if ccircle.isMouseDown('left'):
        if mY < 50:
            if mX < 50:
                color='blue'
            elif mX < 100:
                color='green'
            elif mX < 150:
                color = 'yellow'
            elif mX < 200:
                color = 'red'
            elif mX < 250:
                color = 'black'
            elif mX < 300:
                color = 'white'
        elif mY < 100:
            if mX < 50:
                size = 4
            elif mX < 100:
                size = 8
            elif mX < 150:
                size = 12
            elif mX < 200:
                size = 16
            elif mX < 300:
                color = 'eraser'
        else:
            points.append((mX, mY, size, cR, cG, cB))
    for point in points:
        window.drawCircle(point[0], point[1], point[2], point[3], point[4], point[5])

    window.drawRect(0, 0, 50, 50, 0.1, 0.5, 1.0)
    window.drawRect(50, 0, 50, 50, 0.1, 0.5, 0.1)
    window.drawRect(100, 0, 50, 50, 1.0, 1.0, 0.0)
    window.drawRect(150, 0, 50, 50, 1.0, 0.0, 0.0)
    window.drawRect(200, 0, 50, 50, 0.0, 0.0, 0.0)
    window.drawRect(250, 0, 50, 50, 1.0, 1.0, 1.0)
    window.drawCircle(25, 75, 4, 0.0, 0.0, 0.0)
    window.drawCircle(75, 75, 8, 0.0, 0.0, 0.0)
    window.drawCircle(125, 75, 12, 0.0, 0.0, 0.0)
    window.drawCircle(175, 75, 16, 0.0, 0.0, 0.0)
    window.drawRect(200, 50, 100, 50, 0.3, 0.3, 0.3)

    if color == 'blue':
        window.drawCircle(mX, mY, size, 0.1, 0.5, 1.0)
    elif color == 'green':
        window.drawCircle(mX, mY, size, 0.1, 0.5, 0.1)
    elif color == 'yellow':
        window.drawCircle(mX, mY, size, 1.0, 1.0, 0.0)
    elif color == 'red':
        window.drawCircle(mX, mY, size, 1.0, 0.0, 0.0)
    elif color == 'black':
        window.drawCircle(mX, mY, size, 0.0, 0.0, 0.0)
    elif color == 'white':
        window.drawCircle(mX, mY, size, 1.0, 1.0, 1.0)
    elif color == 'eraser':
        window.drawCircle(mX, mY, size, 0.3, 0.3, 0.3)
    window.update()