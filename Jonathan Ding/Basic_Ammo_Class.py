import ccircle
from math import*
from Util import *

class Ammo:
    def __init__(self, x, y, xv, yv, which, rot, tower):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.which = which
        self.rot = rot
        self.tower = tower
        self.deleted = False

    def draw(self, window):
        window.drawCircle(self.x, self.y, 10, 0.8, 0.8, 0.8)

    def update(self, enemies):
        self.x = self.x + self.xv
        self.y = self.y + self.yv
        if dst(self.x, self.tower.x, self.y, self.tower.y) > self.tower.rng:
            self.deleted = True
        for enemy in enemies:
            if dst(self.x, enemy.x, self.y, enemy.y) < self.tower.spl:
                enemy.hp = enemy.hp - self.tower.dmg
                self.deleted = True
