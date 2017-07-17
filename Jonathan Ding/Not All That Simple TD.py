import ccircle
import Basic_Tower_Class
import Basic_Enemy_Class
from math import*
'''
Archer 
Shot Cannon
Shell Cannon
Spray Cannon
Machine Gun 
Catapult
Axe
OctoGun
Shop?
Ice Beam?
'''

window = ccircle.Window()

window.toggleMaximized()

pg = 1
enemiesX = []
enemiesY = []
enemiesWhich = []
towersX = []
towersY = []
towerType = []

towerNam = ["Archer", "Catapult", "Shot Cannon", "Shell Cannon", "Spray Cannon", "Machine Gun", "Axe", "OctoGun"]
towerRng = []
towerRof = []
towerDmg = []
towerSpd = []
towerPrice = []

grid1 = [
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "t", "t", "t", "t", "t", "t", "t", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "t", "e"],
    ["e", "t", "t", "t", "t", "t", "t", "t", "t", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "t", "t", "t", "t", "e", "e", "e"],
    ["e", "t", "e", "t", "e", "e", "t", "e", "e", "e"],
    ["e", "t", "e", "t", "e", "e", "t", "e", "t", "t"],
    ["e", "t", "t", "t", "e", "e", "t", "t", "t", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]
]
grid2 = [
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "t", "t", "t", "t", "t", "t", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "t", "e", "e"],
    ["e", "e", "e", "e", "t", "t", "t", "t", "e", "e"],
    ["e", "e", "e", "e", "t", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "t", "t", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "t", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "t", "t", "t", "t", "t", "t", "t"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]
]
grid3 = [
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "t", "t", "t", "t", "t", "t", "t", "t"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]
]
grid4 = [
    ["e", "t", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "t", "t", "t", "t", "t", "t", "t", "t", "t"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]
]

waves = [
    ["wut"],
    ["what"],
    ["wat"],
    ["wht"],
    ["whot"]
]

font1 = ccircle.Font("Montel.ttf")

money = 500
lives = 50
wave = 0

pause = 0

difficulty = 1


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


def make_enemies(w):
    enemiesWhich.append(waves[w[1]])
    enemiesX.append()


def home_page():
    window.clear(0.4, 0.8, 0.6)
    font1.draw("NOT ALL", 660, 100, 30, 0.3, 0.7, 0.9)
    font1.draw("THAT SIMPLE", 590, 180, 30, 0.3, 0.7, 0.9)
    font1.draw("TOWER DEFENSE", 540, 260, 30, 0.3, 0.7, 0.9)
    draw_button(800, 600, 100, 4, "PLAY")
    draw_button(1100, 450, 80, 3, "SETTINGS")
    draw_button(500, 450, 80, 2, "HOW 2")


def about_page():
    window.clear(0.8, 0.8, 0.6)
    draw_button(800, 750, 70, 1, "BACK")


def settings_page():
    global difficulty
    window.clear(0.3, 0.6, 0.5)
    draw_button(800, 750, 70, 1, "BACK")
    draw_button(600, 300, 80, 3, "EASY")
    draw_button(1000, 300, 80, 3, "MEDIUM")
    draw_button(600, 500, 80, 3, "HARD")
    draw_button(1000, 500, 80, 3, "DEATH")
    if dst(mouseX, 600, mouseY, 300) <= 80:
        window.drawCircle(600, 300, 90, 0.0, 0.0, 0.0)
        window.drawCircle(600, 300, 86, 0.35, 0.45, 0.85)
        font1.draw("EASY", 560, 300, 15, 0.8, 0.5, 0.6)
        if ccircle.isMouseDown('left'):
            difficulty = 1
    elif dst(mouseX, 1000, mouseY, 300) <= 80:
        window.drawCircle(1000, 300, 90, 0.0, 0.0, 0.0)
        window.drawCircle(1000, 300, 86, 0.35, 0.45, 0.85)
        font1.draw("MEDIUM", 960, 300, 15, 0.8, 0.5, 0.6)
        if ccircle.isMouseDown('left'):
            difficulty = 2
    elif dst(mouseX, 600, mouseY, 500) <= 80:
        window.drawCircle(600, 500, 90, 0.0, 0.0, 0.0)
        window.drawCircle(600, 500, 86, 0.35, 0.45, 0.85)
        font1.draw("HARD", 560, 500, 15, 0.8, 0.5, 0.6)
        if ccircle.isMouseDown('left'):
            difficulty = 3
    elif dst(mouseX, 1000, mouseY, 500) <= 80:
        window.drawCircle(1000, 500, 90, 0.0, 0.0, 0.0)
        window.drawCircle(1000, 500, 86, 0.35, 0.45, 0.85)
        font1.draw("DEATH", 960, 500, 15, 0.8, 0.5, 0.6)
        if ccircle.isMouseDown('left'):
            difficulty = 4
    if difficulty == 1:
        window.drawCircle(600, 300, 80, 0.5, 0.6, 1.0, 0.4)
    elif difficulty == 2:
        window.drawCircle(1000, 300, 80, 0.5, 0.6, 1.0, 0.4)
    elif difficulty == 3:
        window.drawCircle(600, 500, 80, 0.5, 0.6, 1.0, 0.4)
    elif difficulty == 4:
        window.drawCircle(1000, 500, 80, 0.5, 0.6, 1.0, 0.4)

enemy = Enemy()


def game_page():
    window.clear(0.0, 1.0, 0.5)
    for i in range(0, 10):
        for j in range(0, 10):

            if difficulty == 1:
                if grid1[i][j] == "e":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                if grid1[i][j] == "t":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.5, 0.5)
            elif difficulty == 2:
                if grid2[i][j] == "e":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                if grid2[i][j] == "t":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.5, 0.5)
            elif difficulty == 3:
                if grid3[i][j] == "e":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                if grid3[i][j] == "t":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.5, 0.5)
            elif difficulty == 4:
                if grid4[i][j] == "e":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                if grid4[i][j] == "t":
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.5, 0.5)
        draw_button(1200, 750, 70, 1, "BACK")
        for e in range(10):
            enemiesX.append(150)
            enemiesY.append()

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
