import ccircle
from math import*
import time

window = ccircle.Window('keebored')
mysound = ccircle.Sound()

b = 1

window.toggleMaximized()


def sound1(t, f):
    return sin(2 * pi * f * t)

while window.isOpen():
    window.clear(0.0, 0.0, 0.0)
    mouseX, mouseY = window.getMousePos()
    for i in range(10):
        window.drawRect(300 + i * 105, 250, 100, 300, 1.0, 1.0, 1.0)
        if ccircle.isMouseDown('left') and 1350 > mouseX > 300 and 550 > mouseY > 250:
            mysound.addSample(sound1(t, 500 * i))
            mysound.play()
            time.sleep(1)
    for i in range(9):
        window.drawRect(370 + i * 105, 250, 60, 160, 0.0, 0.0, 0.0)
    for m in range(44100):
        t = m / 44100
    window.update()
