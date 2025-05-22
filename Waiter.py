# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:10:03 2025
Waiter
@author: tiago
"""

import Cara as c
import graphics as g
import Table as t

win = t.win
Platedelivery = t.platedelivery.Platedelivery[0].getP2()


class Waiter():
    def __init__(self, win, center, size, group):
        self.robo = c.Face(win, center, size)
        self.move(group, center)

    def move(self, group, center):
        mark = []
        while True:
            dx = 0
            dy = 0
            cx = self.robo.center.getX()
            cy = self.robo.center.getY()
            botão = win.getMouse()
            print(botão)
            bx = botão.getX()
            by = botão.getY() 
            for j in mark:
                j.undraw()
            for i in group:
                mark.append(g.Circle(i.getCenter(), 1))
                ix1 = i.getP1().getX()
                iy1 = i.getP1().getY()
                ix2 = i.getP2().getX()
                iy2 = i.getP2().getY()
                if ix2 > bx and bx > ix1 and iy2 > by and by > iy1:
                    mark[group.index(i)].setFill('red')
                    mark[group.index(i)].draw(win)
                    dx = bx-cx
                    dy = by-cy

            # self.colision(group)
            self.robo.move(dx, dy)

    def colision(self, group):
        dx = self.robo.center.getX()
        dy = self.robo.center.getY()
        for i in group:
            ix1 = i.getP1().getX()
            iy1 = i.getP1().getY()
            ix2 = i.getP2().getX()
            iy2 = i.getP2().getY()
            if ix2+5 > dx and dx > ix1-5 and iy2+5 > dy and dy > iy1-5:
                i.setFill("black")
                return True

    # def drawFace(self):
        # self.robo.drawFace()


robô = Waiter(win, g.Point(Platedelivery.getX() + 5,
              Platedelivery.getY() - 5), 5, t.table.grouptables)
