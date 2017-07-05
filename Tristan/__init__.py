import ccircle
from math import*

window = ccircle.Window("Let's just get it working!", 2021, 2021)

time = 0
while window.isOpen():
    window.clear(0, 1, 0.5)
    window.drawCircle(455, 488, 180, 0, 0.2, 0.5)
    window.drawRect(
        433, 500,
        128, 32 + 32 * (0.5 + 0.5 * cos(time)),
        0.1, 0.2, 1)
    window.drawCircle(370,400,55)
    window.drawCircle(534,400,55)
    window.drawCircle(370,400,33,0.2,0.2,0.2)
    window.drawCircle(534,400,33,0.2,0.2,0.2)
    window.drawCircle(788,233,70,0.888,0.877,0.523)
    time += 0.01
    window.update()
    #put the cookie down, NOW!!!
    #trolling is fun!
    #troller
    #NEKO LIVES MATTER!!!!! JOIN DA NEKO LIBERATION!