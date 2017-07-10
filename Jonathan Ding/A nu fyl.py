import ccircle
import random
import time

cloudX = []
cloudY = []
cloudSize = []
cloudSpeed = []

window = ccircle.Window()
window.toggleMaximized()

while window.isOpen():
    window.clear(0.0, 0.0, 1.0)
    for i in range(100):
        cloudX.append(random.randint(1, 1600))
        cloudY.append(random.randint(1, 300))
        cloudSize.append(random.randint(1, 100))
        cloudSpeed.append(random.randint(1, 3))
        window.drawCircle(cloudX[i], cloudY[i], cloudSize[i], 1.0, 1.0, 1.0, 0.2)
        cloudX[i] += 1
        if cloudX[i] > 1600:
            cloudX[i] = 1
    window.update()
