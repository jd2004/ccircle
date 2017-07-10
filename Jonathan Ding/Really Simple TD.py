import ccircle
import random
from math import*

window = ccircle.Window()

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
          random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600), random.randint(1, 1600)]
enemyY = [random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800, random.randint(1, 800) - 1800, random.randint(1, 800) - 1800,
          random.randint(1, 800) - 1800]
enemyHP = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]


def draw_enemy(x, y, hp):
    window.drawCircle(x, y, 30, 1.0, 0.0, 0.0)
    window.drawCircle(x-10, y-10, 5, 0.0, 0.0, 0.0)
    window.drawCircle(x+10, y-10, 5, 0.0, 0.0, 0.0)
    window.drawRect(x-hp/2, y-50, hp, 10, 0.0, 1.0, 1.0)


def draw_tower(x, y):
    window.drawRect(x-160, y-80, 320, 160, 1.0, 1.0, 1.0, 0.2)
    window.drawCircle(x, y, 25, 1.0, 0.0, 0.0)
    window.drawCircle(x, y, 20, 0.0, 0.0, 1.0)


money = 3000

while window.isOpen():
    window.clear(0.0, 1.0, 0.4)
    mouseX, mouseY = window.getMousePos()
    length, height = window.getSize()
    for i in range(1, 16):
        draw_enemy(enemyX[i], enemyY[i], enemyHP[i])
        enemyY[i] = enemyY[i] + 0.5
        if 0 <= enemyY[i] <= 1800:
            enemyHP[i] = enemyHP[i] + 0.1
        if enemyHP[i] <= 0:
            enemyHP[i] = 0
            window.drawCircle(enemyX[i], enemyY[i], 35, 0.0, 1.0, 0.4)

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
    for i in range(5):
        if towers2[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 252)
    for i in range(5):
        if towers3[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 420)
    for i in range(5):
        if towers4[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 588)
    for i in range(5):
        if towers5[i] == 1:
            draw_tower((320 * (i % 5)) + 160, 756)

    for i in range(5):
        window.drawLine(length * i / 5, 0, length * i / 5, height, 2, 1.0, 1.0, 1.0)
        window.drawLine(0, height * i / 5, length, height * i / 5, 2, 1.0, 1.0, 1.0)
    print(towers1[4])
    window.update()
