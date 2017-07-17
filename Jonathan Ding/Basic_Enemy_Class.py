import ccircle
from math import*


class Enemy:
    def __init__(self, x, y, v, spd, hp, maxhp, which):
        self.x = x,
        self.y = y,
        self.v = v,
        self.spd = spd,
        self.maxhp = maxhp,
        self.hp = hp,
        self.which = which

    def draw(self, window):
        if self.which == 1:
            window.drawCircle(self.x, self.y, 30, 1.0, 0.0, 0.0)

    def update(self, window):
        if self.v == 'left':
            self.x = self.x - self.spd
        elif self.v == 'right':
            self.x = self.x + self.spd
        elif self.v == 'up':
            self.y = self.y - self.spd
        elif self.v == 'down':
            self.x = self.x + self.spd

        #if self.x > 825 or self.hp <= 0:



