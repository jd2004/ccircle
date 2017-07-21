import ccircle
from math import*

towerNam = ["Archer", "Catapult", "Shot Cannon", "Shell Cannon", "Spray Cannon", "Machine Gun", "Axe",
            "Laser"]
towerRng = [250, 400, 200, 200, 290, 210, 120, 1000,
            300, 500, 140, 140, 140, 260, 140, 1500]
towerRof = [90, 300, 100, 100, 100, 20, 500, 10,
            70, 240, 80, 80, 80, 15, 300, 7]
towerDmg = [15, 40, 2, 25, 20, 2, 8, 4,
            20, 50, 3, 35, 25, 5, 8, 9]
towerSpd = [4, 2, 2.8, 2.8, 2.8, 4.5, 10, 6,
            5, 2.4, 3, 3, 3, 6, 10, 7]
towerSpl = [20, 20, 20, 80, 20, 20, 20, 20, 20]


class Tower:
    def __init__(self, x, y, r, which, images):
        self.nam = towerNam[which]
        self.lvl = 0
        self.x = x
        self.y = y
        self.r = r
        self.rng = towerRng[which + 8 * self.lvl]
        self.rof = towerRof[which + 8 * self.lvl]
        self.dmg = towerDmg[which + 8 * self.lvl]
        self.spd = towerSpd[which + 8 * self.lvl]
        self.spl = towerSpl[which]
        self.which = which
        self.closest = 1000
        self.image = images[which + 8 * self.lvl]
        self.images = images
        self.angle = 0

    def draw(self):
        self.image.draw(self.x - 35, self.y - 35, 70, 70, self.angle)

    def refresh(self):
        self.rng = towerRng[self.which + 8 * self.lvl]
        self.rof = towerRof[self.which + 8 * self.lvl]
        self.dmg = towerDmg[self.which + 8 * self.lvl]
        self.spd = towerSpd[self.which + 8 * self.lvl]
        self.image = self.images[self.which + 8 * self.lvl]