import ccircle
from math import*

window = ccircle.Window()


class Tower:
    def __init__(self, nam, x, y, r, rng, rof, dmg, spd, price):
        self.nam = nam
        self.x = x
        self.y = y
        self.r = r
        self.rng = rng
        self.rof = rof
        self.dmg = dmg
        self.spd = spd
        self.price = price

    def draw_tower(self, which):
        if which == 0:
            window.drawCircle(self.x, self.y, 40, 1.0, 0.0, 0.0),
        elif which == 1:
            window.drawCircle(self.x, self.y, 40, 1.0, 1.0, 0.0)
        elif which == 2:
            window.drawCircle(self.x, self.y, 40, 0.0, 1.0, 0.0)
        elif which == 3:
            window.drawCircle(self.x, self.y, 40, 0.0, 0.0, 1.0)

archer = Tower("archer", 400, 400, 0, 200, 10, 10, 10, 5923)

while window.isOpen():
    window.clear(0.0, 0.0, 0.0)
    archer.draw_tower(0)
    window.update()


