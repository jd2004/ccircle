import ccircle
from math import*
'''
Archer --> Musketeer --> Sniper
Catapult --> Ballista --> Cannon
Air Blaster --> Wind Blaster --> Water Blaster
Shop --> Market --> Supermarket
Dwarf --> Troll --> Giant
2-shooter --> 4-shooter --> 8-shooter
Electrifier --> Zapper --> Thunderer
Smoker --> Poisoner --> Drainer
Machine-Gun --> Flamethrower --> Laser
'''

window = ccircle.Window()

pg = 1
enemiesX = []
enemiesY = []
towersX = []
towersY = []

towerNam = ["archer", "catapult", "air blaster", "shop", "dwarf", "2-shooter", "electrifier", "smoker", "machine-gun"]
towerRng = [100, 250, 150, 0, 50, 80, 210, 90, 160]
towerRof = [50, 160, 200, 0, 100, 80, 250, 5, 15]
towerDmg = [20, 75, 2, 0, 100, 20, 15, 3, 10]
towerSpd = [30, 40, 30, 0, 30, 25, 100, 100, 30]
towerPrice = [100, 250, 360, 400, 500, 600, 840, 1000, 1500]


def dst(a, b, c, d):
    return sqrt((abs(a - b))**2 + (abs(c - d))**2)


def draw_button(x, y, r, case):
    global pg
    window.drawCircle(x, y, r + 4, 0.0, 0.0, 0.0)
    window.drawCircle(x, y, r, 0.3, 0.4, 0.8)
    if dst(mouseX, x, mouseY, y) <= r:
        window.drawCircle(x, y, r + 10, 0.0, 0.0, 0.0)
        window.drawCircle(x, y, r + 6, 0.35, 0.45, 0.85)
        if ccircle.isMouseDown('left'):
            if case == 0:
                pg = 2


def home_page():
    window.clear(0.4, 0.8, 0.6)
    draw_button(200, 200, 100, 0)


def about_page():
    window.clear(0.8, 0.8, 0.6)


def settings_page():
    window.clear(0.3, 0.6, 0.5)


def game_page():
    window.clear(0.0, 1.0, 0.5)

while window.isOpen():
    mouseX, mouseY = window.getMousePos()

    if pg == 1:
        home_page()
    elif pg == 2:
        about_page()
    elif pg == 3:
        settings_page()
    elif pg == 4:
        game_page()
    window.update()
