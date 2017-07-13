import ccircle
from math import*

window = ccircle.Window()

class Button:
    def __init__(self, x, y, r, case):
        self.x = x,
        self.y = y,
        self.r = r,
        self.case = case

    def draw_button(self):
        def dst(a, b, c, d):
            return sqrt(abs(a - b) + abs(c - d))
        mousex, mousey = window.getMousePos()
        window.drawCircle(self.x, self.y, self.r, 0.3, 0.4, 0.8)
        '''if ccircle.isMouseDown('left') & dst(mousex, self.x, mousey, self.y) <= self.r:

            if self.case == 0:
            elif self.case == 1:
            elif self.case == 2:
            elif self.case == 3:'''
