import ccircle
from math import*

window = ccircle.Window()


class Ammo:
    def __init__(self, x, y, which, rot):
        self.x = x
        self.y = y
        self.type = which