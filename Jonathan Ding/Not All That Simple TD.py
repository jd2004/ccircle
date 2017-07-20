import ccircle
import Basic_Tower_Class
import Basic_Ammo_Class
import Basic_Enemy_Class
from Util import *
from math import *
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

enemies = []

towers = []

ammos = []

towerPrice = [100, 250, 400, 400, 400, 650, 800, 1000, 3000]

tower_select = -1

towerNam = ["Archer", "Catapult", "Shot Cannon", "Shell Cannon", "Spray Cannon", "Machine Gun", "Axe", "OctoGun",
            "Laser"]

grids = [
    [
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
    ],
    [
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
    ],
    [
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
    ],
    [
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
]


waves = [
    [1, 300, 6],
    [2, 400, 4],
    [1, 120, 20],
    [3, 600, 10],
    [2, 200, 40],
    [4, 500, 15],
    [5, 350, 100],
]
wave = 1

load = 0
load2 = 0

font1 = ccircle.Font("Montel.ttf")

money = 600
lives = 50
wave = 0

pause = 0

difficulty = 1


def draw_button(x, y, r, case, text):
    global pg
    global mouseX
    global mouseY
    window.drawCircle(x, y, r + 4, 0.0, 0.0, 0.0)
    window.drawCircle(x, y, r, 0.3, 0.4, 0.8)
    font1.draw(text, x - r / 2, y, r / 7, 0.8, 0.5, 0.6)
    isdown = ccircle.isMouseDown('left')
    if dst(mouseX, x, mouseY, y) <= r:
        window.drawCircle(x, y, r + 10, 0.0, 0.0, 0.0)
        window.drawCircle(x, y, r + 6, 0.35, 0.45, 0.85)
        font1.draw(text, x - r / 2, y, r / 6, 0.8, 0.5, 0.6)
        if isdown:
            pg = case


def draw_shop_button(x, y, r, tower, text):
    global mouseX
    global mouseY
    global money
    global tower_select
    window.drawRect(x - r / 2 - 2, y - r / 2 - 2, r + 4, r + 4, 0.0, 0.0, 0.0)
    window.drawRect(x - r / 2, y - r / 2, r, r, 0.2, 0.6, 0.5)
    font1.draw(text, x - r * 2 / 5, y - r / 3, r / 20, 0.8, 0.5, 0.6)
    font1.draw("$ " + str(towerPrice[tower]), x - r * 2 / 5, y - r / 8, r / 20, 0.8, 0.5, 0.6)
    stower = Basic_Tower_Class.Tower(x, y + 20, 0, tower)
    stower.draw(window)
    downis = ccircle.isMouseDown('left')
    if x + r / 2 > mouseX > x - r / 2 and y + r / 2 > mouseY > y - r / 2:
        window.drawRect(x - r / 2 - 10, y - r / 2 - 10, r + 20, r + 20, 0.0, 0.0, 0.0)
        window.drawRect(x - r / 2 - 8, y - r / 2 - 8, r + 16, r + 16, 0.2, 0.6, 0.5)
        font1.draw(text, x - r / 2, y - r / 3, r / 14, 0.8, 0.5, 0.6)
        font1.draw("$ " + str(towerPrice[tower]), x - r / 2, y - r / 8, r / 14, 0.8, 0.5, 0.6)
        stower.draw(window)
        if downis and tower_select == -1 and money >= towerPrice[tower]:
            money = money - towerPrice[tower]
            stower.draw(window)
            tower_select = tower


def home_page():
    window.clear(0.4, 0.8, 0.6)
    font1.draw("ULTIMATE CITY", 600, 100, 30, 0.3, 0.7, 0.9)
    font1.draw("TOWER DEFENSE", 590, 180, 30, 0.3, 0.7, 0.9)
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


def game_page():
    global enemies
    global enemy
    global tower
    global wave
    global load
    global load2
    global pg
    global lives
    global tower_select
    global money
    global dst
    if load >= 0 and load % waves[wave][1] == 0 and waves[wave][1] * waves[wave][2] - load >= 0:
        enemy = Basic_Enemy_Class.Enemy(135, 0, 'down', waves[wave][0])
        enemies.append(enemy)
    elif waves[wave][1] * waves[wave][2] - load < 0:
        wave = wave + 1
        load = -6000
    if wave > len(waves):
        pg = 5

    window.clear(0.0, 1.0, 0.5)
    for i in range(0, 10):
        for j in range(0, 10):
            if grids[difficulty - 1][i][j] == "e":
                window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                if tower_select != -1 and 80 * j < mouseX < 80 * j + 80 and 80 * i < mouseY < 80 * i + 80:
                    window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.0, 0.6, 0.0)
                    if ccircle.isMouseDown('left'):
                        t = Basic_Tower_Class.Tower(j * 80 + 55, i * 80 + 55, 0, tower_select)
                        grids[difficulty - 1][i][j] = t
                        towers.append(t)
                        tower_select = -1
            if grids[difficulty - 1][i][j] == "t":
                window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.5, 0.5)
            if grids[difficulty - 1][i][j] != "t" and grids[difficulty - 1][i][j] != "e":
                t = grids[difficulty - 1][i][j]
                window.drawRect(80 * j + 20, 80 * i + 20, 70, 70, 0.1, 0.8, 0.2)
                t.draw(window)
                if 80 * j < mouseX < 80 * j + 80 and 80 * i < mouseY < 80 * i + 80:
                    window.drawCircle(80 * j + 60, 80 * i + 60, t.rng, 0.4, 0.4, 0.4, 0.4)

    for enemy in list(enemies):
        enemy.draw(window)
        enemy.update(dst, difficulty)
        if enemy.x > 800:
            enemies.remove(enemy)
            lives = lives - 1
        if enemy.hp <= 0:
            enemies.remove(enemy)
            money = money + 3

    if tower_select != -1:
        tower = Basic_Tower_Class.Tower(mouseX, mouseY, 0, tower_select)
        tower.draw(window)

    font1.draw(str(lives) + " LIVES", 850, 100, 20, 1.0, 0.0, 0.0)
    font1.draw("$ " + str(money), 1100, 100, 20, 0.8, 1.0, 0.2)
    font1.draw("WAVE " + str(wave + 1), 1300, 100, 20, 0.0, 0.0, 1.0)
    for a in range(6):
        draw_shop_button(900 + 120 * a, 200, 100, a, towerNam[a])
    for a in range(6, 9):
        draw_shop_button(900 + 120 * (a - 6), 350, 100, a, towerNam[a])
    for tower in towers:
        not_shot = True
        tower.closest = tower.rng
        for enemy in enemies:
            if dst(tower.x, enemy.x, tower.y, enemy.y) < tower.closest:
                tower.closest = dst(tower.x, enemy.x, tower.y, enemy.y)
        for enemy in enemies:
            if dst(tower.x, enemy.x, tower.y, enemy.y) <= tower.rng and \
                    load2 % tower.rof == 0 and \
                    dst(tower.x, enemy.x, tower.y, enemy.y) <= tower.closest and \
                    not_shot:
                tower.closest = dst(tower.x, enemy.x, tower.y, enemy.y)
                bullet = Basic_Ammo_Class.Ammo(tower.x, tower.y,
                                               tower.spd * ((enemy.x - tower.x) / dst(tower.x, enemy.x, tower.y, enemy.y)),
                                               tower.spd * ((enemy.y - tower.y) / dst(tower.x, enemy.x, tower.y, enemy.y)),
                                               tower.which,
                                               atan2(enemy.y - tower.y, enemy.x - tower.x), tower)
                not_shot = False
                ammos.append(bullet)

    for bullet in list(ammos):
        bullet.draw(window)
        bullet.update(enemies)
        if bullet.deleted:
            ammos.remove(bullet)


def win_page():
    window.clear(1.0, 1.0, 1.0)


while window.isOpen():
    mouseX, mouseY = window.getMousePos()
    load = load + 1
    load2 = load2 + 1
    if pg == 1:
        home_page()
    elif pg == 2:
        about_page()
    elif pg == 3:
        settings_page()
    elif pg == 4:
        game_page()
    elif pg == 5:
        win_page()
    window.update()
