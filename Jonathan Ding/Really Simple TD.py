import ccircle
import random
from math import*

'''
J # r + r r F
y           b
y    mini   ]
+    mono   +
y    poly   b
[           b
F g g + g # G 

G gives 100

g costs 20 hut 10 house 20 hotel 30
rent 5 10 15 20

y costs 50 hut 20 house 30 hotel 40
rent 10 15 25 40

r costs 80 hut 30 house 40 hotel 50
rent 15 25 40 60

b costs 120 hut 40 house 50 hotel 60
rent 25 45 70   

[ or ] costs 60
rent roll * 5

# gives 10 * random.randint(-3, 4)

+ costs 50
rent 20 * number of railroads

F gives does none

J skips your turn for 3 rounds
'''

window = ccircle.Window("TOWER DEFENSE!")

towers1 = [
    0, 0, 0, 0, 0,
]
towers2 = [
    0, 0, 0, 0, 0,
]
towers3 = [
    0, 0, 0, 0, 0,
]
towers4 = [
    0, 0, 0, 0, 0,
]
towers5 = [
    0, 0, 0, 0, 0,
]

window.toggleMaximized()

enemyX = [random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600),
          random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600),
          random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600),
          random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600),
          random.randint(400, 1200), random.randint(400, 1200), random.randint(400, 1200),
          random.randint(400, 1200), random.randint(400, 1200), random.randint(400, 1200),
          random.randint(700, 900)]
enemyY = [random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800,
          random.randint(1, 800) - 2500, random.randint(1, 800) - 2500, random.randint(1, 800) - 2500,
          random.randint(1, 800) - 2500, random.randint(1, 800) - 2500, random.randint(1, 800) - 2500,
          -3600]
enemyHP = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
           300, 300, 300, 300, 300, 300,
           1000]

enemySpeed = [1, 1, 1, 1, 1,
              1, 1, 1, 1, 1,
              1, 1, 1, 1, 1, 1,
              0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.6]

enemyDead = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

towerY = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
          1000, 1000, 1000, 1000, 1000, 1000, 1000]
towerX = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def draw_enemy(x, y, hp):
    window.drawCircle(x, y, 30, 1.0, 0.0, 0.0)
    window.drawCircle(x-10, y-10, 5, 0.0, 0.0, 0.0)
    window.drawCircle(x+10, y-10, 5, 0.0, 0.0, 0.0)
    window.drawRect(x - 50, y - 50, 100, 10, 1.0, 0.0, 0.0)
    window.drawRect(x - 50, y-50, hp, 10, 0.0, 1.0, 1.0)


def draw_foe(x, y, hp):
    window.drawCircle(x, y, 40, 0.0, 0.0, 1.0)
    window.drawCircle(x - 10, y - 10, 5, 0.0, 0.0, 0.0)
    window.drawCircle(x + 10, y - 10, 5, 0.0, 0.0, 0.0)
    window.drawRect(x - 150, y - 50, 300, 10, 1.0, 0.0, 0.0)
    window.drawRect(x - 150, y - 50, hp, 10, 0.0, 1.0, 1.0)


def draw_boss(x, y, hp):
    window.drawCircle(x, y, 50, 0.0, 0.0, 0.0)
    window.drawCircle(x - 15, y - 15, 5, 1.0, 0.0, 0.0)
    window.drawCircle(x + 15, y - 15, 5, 1.0, 0.0, 0.0)
    window.drawRect(x-500, y - 50, 1000, 10, 1.0, 0.0, 0.0)
    window.drawRect(x - 500, y - 50, hp, 10, 0.0, 1.0, 1.0)


def draw_tower(x, y):
    window.drawCircle(x, y, 200, 1.0, 1.0, 1.0, 0.2)
    window.drawCircle(x, y, 25, 1.0, 0.0, 0.0)
    window.drawCircle(x, y, 20, 0.0, 0.0, 1.0)


def dst(a, b, c, d):
    return sqrt(abs(a - b) + abs(c - d))

money = 300
timer = 0

while window.isOpen():
    window.clear(0.0, 1.0, 0.4)
    mouseX, mouseY = window.getMousePos()
    length, height = window.getSize()
    money = money + 0.05
    timer = timer + 1

    for i in range(0, 15):
        draw_enemy(enemyX[i], enemyY[i], enemyHP[i])
        enemyY[i] = enemyY[i] + enemySpeed[i] / 2
        for m in range(0, 25):
            if dst(enemyX[i], towerX[m], enemyY[i], towerY[m]) < 15:
                enemyHP[i] = enemyHP[i] - 0.3
                if enemyDead[i] != 1:
                    window.drawLine(towerX[m], towerY[m], enemyX[i], enemyY[i], 2, 1.0, 0.0, 0.0)
        if enemyHP[i] <= 0:
            enemyHP[i] = 0
            enemyDead[i] = 1
            window.drawCircle(enemyX[i], enemyY[i], 35, 0.0, 1.0, 0.4)
            window.drawRect(enemyX[i] - 60, enemyY[i] - 55, 120, 30, 0.0, 1.0, 0.4)

    for i in range(16, 21):
        draw_foe(enemyX[i], enemyY[i], enemyHP[i])
        enemyY[i] = enemyY[i] + enemySpeed[i] / 2
        for m in range(0, 25):
            if dst(enemyX[i], towerX[m], enemyY[i], towerY[m]) < 15:
                enemyHP[i] = enemyHP[i] - 0.3
                if enemyDead[i] != 1:
                    window.drawLine(towerX[m], towerY[m], enemyX[i], enemyY[i], 2, 1.0, 0.0, 0.0)
        if enemyHP[i] <= 0:
            enemyHP[i] = 0
            enemyDead[i] = 1
            window.drawCircle(enemyX[i], enemyY[i], 45, 0.0, 1.0, 0.4)
            window.drawRect(enemyX[i] - 160, enemyY[i] - 55, 320, 30, 0.0, 1.0, 0.4)

    draw_boss(enemyX[22], enemyY[22], enemyHP[22])
    enemyY[22] = enemyY[22] + enemySpeed[22] / 2
    for m in range(0, 25):
        if dst(enemyX[22], towerX[m], enemyY[22], towerY[m]) < 15:
            enemyHP[22] = enemyHP[22] - 0.3
            if enemyDead[22] != 1:
                window.drawLine(towerX[m], towerY[m], enemyX[22], enemyY[22], 2, 1.0, 0.0, 0.0)
    if enemyHP[22] <= 0:
        enemyHP[22] = 0
        enemyDead[22] = 1
        window.drawCircle(enemyX[22], enemyY[22], 55, 0.0, 1.0, 0.4)
        window.drawRect(enemyX[22] - 510, enemyY[22] - 55, 1020, 30, 0.0, 1.0, 0.4)

    if ccircle.isMouseDown('left') and money >= 100:
        if mouseY < 168:
            if mouseX < 320 and towers1[0] != 1:
                towers1[0] = 1
                money = money - 100
            elif 320 < mouseX < 640 and towers1[1] != 1:
                towers1[1] = 1
                money = money - 100
            elif 640 < mouseX < 960 and towers1[2] != 1:
                towers1[2] = 1
                money = money - 100
            elif 960 < mouseX < 1280 and towers1[3] != 1:
                towers1[3] = 1
                money = money - 100
            elif 1280 < mouseX < 1600 and towers1[4] != 1:
                towers1[4] = 1
                money = money - 100
        elif mouseY < 336:
            if mouseX < 320 and towers2[0] != 1:
                towers2[0] = 1
                money = money - 100
            elif 320 < mouseX < 640 and towers2[1] != 1:
                towers2[1] = 1
                money = money - 100
            elif 640 < mouseX < 960 and towers2[2] != 1:
                towers2[2] = 1
                money = money - 100
            elif 960 < mouseX < 1280 and towers2[3] != 1:
                towers2[3] = 1
                money = money - 100
            elif 1280 < mouseX < 1600 and towers2[4] != 1:
                towers2[4] = 1
                money = money - 100
        elif mouseY < 504:
            if mouseX < 320 and towers3[0] != 1:
                towers3[0] = 1
                money = money - 100
            elif 320 < mouseX < 640 and towers3[1] != 1:
                towers3[1] = 1
                money = money - 100
            elif 640 < mouseX < 960 and towers3[2] != 1:
                towers3[2] = 1
                money = money - 100
            elif 960 < mouseX < 1280 and towers3[3] != 1:
                towers3[3] = 1
                money = money - 100
            elif 1280 < mouseX < 1600 and towers3[4] != 1:
                towers3[4] = 1
                money = money - 100
        elif mouseY < 672:
            if mouseX < 320 and towers4[0] != 1:
                towers4[0] = 1
                money = money - 100
            elif 320 < mouseX < 640 and towers4[1] != 1:
                towers4[1] = 1
                money = money - 100
            elif 640 < mouseX < 960 and towers4[2] != 1:
                towers4[2] = 1
                money = money - 100
            elif 960 < mouseX < 1280 and towers4[3] != 1:
                towers4[3] = 1
                money = money - 100
            elif 1280 < mouseX < 1600 and towers4[4] != 1:
                towers4[4] = 1
                money = money - 100
        elif mouseY < 840:
            if mouseX < 320 and towers5[0] != 1:
                towers5[0] = 1
                money = money - 100
            elif 320 < mouseX < 640 and towers5[1] != 1:
                towers5[1] = 1
                money = money - 100
            elif 640 < mouseX < 960 and towers5[2] != 1:
                towers5[2] = 1
                money = money - 100
            elif 960 < mouseX < 1280 and towers5[3] != 1:
                towers5[3] = 1
                money = money - 100
            elif 1280 < mouseX < 1600 and towers5[4] != 1:
                towers5[4] = 1
                money = money - 100
    for i in range(5):
        if towers1[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 84)
            towerX[i] = ((320 * (i % 5)) + 160)
            towerY[i] = 84
    for i in range(5):
        if towers2[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 252)
            towerX[i + 5] = ((320 * (i % 5)) + 160)
            towerY[i + 5] = 252
    for i in range(5):
        if towers3[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 420)
            towerX[i + 10] = ((320 * (i % 5)) + 160)
            towerY[i + 10] = 420
    for i in range(5):
        if towers4[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 588)
            towerX[i + 15] = ((320 * (i % 5)) + 160)
            towerY[i + 15] = 588
    for i in range(5):
        if towers5[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 756)
            towerX[i + 20] = ((320 * (i % 5)) + 160)
            towerY[i + 20] = 756

    for i in range(5):
        window.drawLine(length * i / 5, 0, length * i / 5, height, 2, 1.0, 1.0, 1.0)
        window.drawLine(0, height * i / 5, length, height * i / 5, 2, 1.0, 1.0, 1.0)

    if enemyHP[22] == 0:
        print('WINNER')
    elif timer >= 16000:
        print('LOSER')

    window.update()
