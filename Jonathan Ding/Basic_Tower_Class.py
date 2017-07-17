import ccircle
from math import*


class Tower:
    def __init__(self, nam, x, y, r, rng, rof, dmg, spd, price, which):
        self.nam = nam
        self.x = x
        self.y = y
        self.r = r
        self.rng = rng
        self.rof = rof
        self.dmg = dmg
        self.spd = spd
        self.price = price
        self.which = which

    def draw(self, window):
        if self.which == 0:
            window.drawCircle(self.x, self.y, 40, 1.0, 0.0, 0.0)
        elif self.which == 1:
            window.drawCircle(self.x, self.y, 40, 1.0, 1.0, 0.0)
        elif self.which == 2:
            window.drawCircle(self.x, self.y, 40, 0.0, 1.0, 0.0)
        elif self.which == 3:
            window.drawCircle(self.x, self.y, 40, 0.0, 0.0, 1.0)




