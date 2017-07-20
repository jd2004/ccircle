import ccircle
from math import*

enemyHp = [100, 60, 300, 40, 800, 1500, 40000]
enemySpd = [0.5, 1, 0.2, 2.5, 0.06, 0.6, 0.01]


class Enemy:
    def __init__(self, x, y, v, which):
        self.x = x
        self.y = y
        self.v = v
        self.spd = enemySpd[which - 1]
        self.maxhp = enemyHp[which - 1]
        self.hp = enemyHp[which - 1]
        self.which = which

    def draw(self, window):
        if self.which == 1:
            window.drawCircle(self.x, self.y, 30, 1.0, 0.0, 0.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.5, 0.5, 0.0)
        if self.which == 2:
            window.drawCircle(self.x, self.y, 20, 1.0, 1.0, 0.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.5, 0.5, 0.0)
        if self.which == 3:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.5, 0.5, 0.0)
        if self.which == 4:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.5, 0.2, 0.0)
        if self.which == 5:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.7, 0.0, 0.0)
        if self.which == 6:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.9, 0.1, 0.3)
        if self.which == 7:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.5, 0.5, 0.5)
        if self.which == 8:
            window.drawCircle(self.x, self.y, 45, 0.0, 1.0, 1.0)
            window.drawRect(self.x - self.hp / 2, self.y - 30, self.hp, 8, 0.1, 0.1, 0.9)

    def update(self, dst, diff):
        if self.v == 'left':
            self.x = self.x - self.spd
        elif self.v == 'right':
            self.x = self.x + self.spd
        elif self.v == 'up':
            self.y = self.y - self.spd
        elif self.v == 'down':
            self.y = self.y + self.spd
        if diff == 1:
            if dst(self.x, 135, self.y, 135) < 5:
                self.v = 'right'
            if dst(self.x, 700, self.y, 135) < 5:
                self.v = 'down'
            if dst(self.x, 700, self.y, 300) < 5:
                self.v = 'left'
            if dst(self.x, 135, self.y, 300) < 5:
                self.v = 'down'
            if dst(self.x, 135, self.y, 700) < 5:
                self.v = 'right'
            if dst(self.x, 295, self.y, 700) < 5:
                self.v = 'up'
            if dst(self.x, 295, self.y, 445) < 5:
                self.v = 'right'
            if dst(self.x, 535, self.y, 445) < 5:
                self.v = 'down'
            if dst(self.x, 535, self.y, 700) < 5:
                self.v = 'right'
            if dst(self.x, 700, self.y, 700) < 5:
                self.v = 'up'
            if dst(self.x, 700, self.y, 615) < 5:
                self.v = 'right'
        if diff == 2:
            if dst(self.x, 135, self.y, 135) < 5:
                self.v = 'right'
            if dst(self.x, 615, self.y, 135) < 5:
                self.v = 'down'
            if dst(self.x, 615, self.y, 300) < 5:
                self.v = 'left'
            if dst(self.x, 375, self.y, 300) < 5:
                self.v = 'down'
            if dst(self.x, 375, self.y, 465) < 5:
                self.v = 'left'
            if dst(self.x, 300, self.y, 465) < 5:
                self.v = 'down'
            if dst(self.x, 300, self.y, 620) < 5:
                self.v = 'right'
        if diff == 3:
            if dst(self.x, 135, self.y, 540) < 5:
                self.v = 'right'
        if diff == 4:
            if dst(self.x, 135, self.y, 135) < 5:
                self.v = 'right'
