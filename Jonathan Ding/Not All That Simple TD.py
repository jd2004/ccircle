import ccircle
import "Basic Tower Class.py"
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

window.toggleMaximized()

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

font1 = ccircle.Font("Montel.ttf")


def dst(a, b, c, d):
    return sqrt((abs(a - b))**2 + (abs(c - d))**2)


def draw_button(x, y, r, case, text):
    global pg
    window.drawCircle(x, y, r + 4, 0.0, 0.0, 0.0)
    window.drawCircle(x, y, r, 0.3, 0.4, 0.8)
    font1.draw(text, x - r / 2, y, r / 7, 0.8, 0.5, 0.6)
    if dst(mouseX, x, mouseY, y) <= r:
        window.drawCircle(x, y, r + 10, 0.0, 0.0, 0.0)
        window.drawCircle(x, y, r + 6, 0.35, 0.45, 0.85)
        font1.draw(text, x - r / 2, y, r / 6, 0.8, 0.5, 0.6)
        if ccircle.isMouseDown('left'):
            pg = case

cannon = Tower("yo", 600, 600, 0, 100, 100, 100, 100, 100, 100)


def home_page():
    window.clear(0.4, 0.8, 0.6)
    font1.draw("NOT ALL", 660, 100, 30, 0.3, 0.7, 0.9)
    font1.draw("THAT SIMPLE", 590, 180, 30, 0.3, 0.7, 0.9)
    font1.draw("TOWER DEFENSE", 540, 260, 30, 0.3, 0.7, 0.9)
    draw_button(800, 600, 100, 4, "play")
    draw_button(1100, 450, 80, 3, "settings")
    draw_button(500, 450, 80, 2, "How 2")
    cannon.draw(0)


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
