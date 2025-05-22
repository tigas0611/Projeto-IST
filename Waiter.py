# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:10:03 2025
Waiter
@author: tiago
"""

import Robot as ro
import graphics as gr


class Waiter():
    def __init__(self, win, center, group):
        self.win = win
        self.robo = ro.Robot(win, center)
        self.move(group, center)

    def move(self, group, center):
        while True:
            centerX = self.robo.center.getX()
            centerY = self.robo.center.getY()
            button = self.win.getMouse()
            buttonX = button.getX()
            buttonY = button.getY() 
            for i in group:
                mark = gr.Circle(i.getCenter(), 1)
                ix1 = i.getP1().getX()
                iy1 = i.getP1().getY()
                ix2 = i.getP2().getX()
                iy2 = i.getP2().getY()
                if ix1 < buttonX < ix2 and iy1 < buttonY < iy2:
                    mark = gr.Circle(i.getCenter(), 1)
                    mark.setFill('red')
                    mark.draw(self.win)
                    dx = buttonX-centerX
                    dy = buttonY-centerY
                    self.robo.move(dx, dy)
                    mark.undraw()
            #self.colision(group)
            
            

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


