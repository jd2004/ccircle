import ccircle
from math import*

towerNam = ["Archer", "Catapult", "Shot Cannon", "Shell Cannon", "Spray Cannon", "Machine Gun", "Axe", "OctoGun"]
towerRng = [300, 400, 150, 150, 150, 210, 80, 120]
towerRof = [300, 400, 150, 150, 150, 210, 80, 120]
towerDmg = [300, 400, 150, 150, 150, 210, 80, 120]
towerSpd = [300, 400, 150, 150, 150, 210, 80, 120]


class Tower:
    def __init__(self, x, y, r, which):
        print(which)
        self.nam = towerNam[which - 1]
        self.x = x
        self.y = y
        self.r = r
        self.rng = towerRng[which - 1]
        self.rof = towerRof[which - 1]
        self.dmg = towerDmg[which - 1]
        self.spd = towerSpd[which - 1]
        self.which = which

    def draw(self, window):
        if self.which == 0:
            window.drawCircle(self.x, self.y, 30, 1.0, 0.0, 0.0)
        elif self.which == 1:
            window.drawCircle(self.x, self.y, 30, 1.0, 1.0, 0.0)
        elif self.which == 2:
            window.drawCircle(self.x, self.y, 30, 0.0, 1.0, 0.0)
        elif self.which == 3:
            window.drawCircle(self.x, self.y, 30, 0.0, 0.0, 1.0)




