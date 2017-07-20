import ccircle
from math import*

towerNam = ["Archer", "Catapult", "Shot Cannon", "Shell Cannon", "Spray Cannon", "Machine Gun", "Axe", "OctoGun",
            "Laser"]
towerRng = [200, 400, 150, 150, 150, 210, 80, 120, 1000]
towerRof = [70, 300, 100, 100, 100, 20, 500, 120, 10]
towerDmg = [15, 40, 30, 25, 20, 2, 8, 12, 4]
towerSpd = [4, 1, 1.2, 1.2, 1.2, 2.4, 2, 1, 3]
towerSpl = [20, 20, 20, 80, 20, 20, 20, 20, 20]


class Tower:
    def __init__(self, x, y, r, which):
        self.nam = towerNam[which]
        self.x = x
        self.y = y
        self.r = r
        self.rng = towerRng[which]
        self.rof = towerRof[which]
        self.dmg = towerDmg[which]
        self.spd = towerSpd[which]
        self.spl = towerSpl[which]
        self.which = which
        self.closest = 1000

    def draw(self, window):
        if self.which == 0:
            window.drawCircle(self.x, self.y, 30, 1.0, 0.0, 0.0)
        elif self.which == 1:
            window.drawCircle(self.x, self.y, 30, 1.0, 1.0, 0.0)
        elif self.which == 2:
            window.drawCircle(self.x, self.y, 30, 0.0, 1.0, 0.0)
        elif self.which == 3:
            window.drawCircle(self.x, self.y, 30, 0.0, 0.0, 1.0)
        elif self.which == 4:
            window.drawCircle(self.x, self.y, 30, 0.0, 1.0, 1.0)
        elif self.which == 5:
            window.drawCircle(self.x, self.y, 30, 1.0, 1.0, 1.0)
        elif self.which == 6:
            window.drawCircle(self.x, self.y, 30, 1.0, 0.0, 1.0)
        elif self.which == 7:
            window.drawCircle(self.x, self.y, 30, 0.0, 0.0, 0.0)
        elif self.which == 8:
            window.drawCircle(self.x, self.y, 30, 0.5, 0.5, 0.5)




