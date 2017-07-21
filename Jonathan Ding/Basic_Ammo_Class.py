import ccircle
from math import*
from Util import *

class Ammo:
    def __init__(self, x, y, xv, yv, which, rot, tower, imgs):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.which = which
        self.rot = rot
        self.tower = tower
        self.deleted = False
        self.imgs = imgs

    def draw(self, window):
        if self.which == 0:
            arrow = self.imgs[2]
            arrow.draw(self.x - 5, self.y - 12, 10, 25, self.rot)
        elif self.which == 1:
            rock = self.imgs[1]
            rock.draw(self.x - 10, self.y - 10, 20, 20, self.rot)
        elif self.which == 3:
            arrow = self.imgs[3]
            arrow.draw(self.x - 12, self.y - 10, 24, 20, self.rot)
        elif self.which == 7:
            arrow = self.imgs[4]
            arrow.draw(self.x - 4, self.y - 4, 8, 8, self.rot)
        else:
            ball = self.imgs[1]
            ball.draw(self.x - 10, self.y - 10, 20, 20, self.rot)

    def update(self, enemies):
        self.x = self.x + self.xv
        self.y = self.y + self.yv
        if dst(self.x, self.tower.x, self.y, self.tower.y) > self.tower.rng:
            self.deleted = True
        for enemy in enemies:
            if dst(self.x, enemy.x, self.y, enemy.y) < self.tower.spl:
                enemy.hp = enemy.hp - self.tower.dmg
                if self.which != 2:
                    self.deleted = True
