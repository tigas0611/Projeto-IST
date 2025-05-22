# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:47:07 2025
Classe Cara
@author: tiago
"""

import graphics as gr

class Robot:
    def __init__(self, win, center):
        self.center = center
        self.ovalstartX = self.center.getX() - 3
        self.ovalstartY = self.center.getY() - 4
        self.ovalfinishX = self.center.getX() + 3
        self.ovalfinishY = self.center.getY() + 4
        self.oval = gr.Oval(gr.Point(self.ovalstartX, self.ovalstartY), gr.Point(self.ovalfinishX, self.ovalfinishY))
        self.win = win
        self.drawRobot()
    
    def move(self, dx, dy):
        self.oval.move(dx,dy)
        self.center = self.oval.getCenter()

    def unDraw(self):
        self.oval.undraw()
            
    def drawRobot(self):
        self.oval.draw(self.win)
    
    
    