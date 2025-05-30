# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:47:07 2025
Classe Robot
@author: tiago
"""

import graphics as gr

class Robot:
    def __init__(self, win, center, size):
        self.center = center
        self.circle = gr.Circle(center, size)
        self.win = win
        self.circle.draw(win)
    
    def move(self, dx, dy):
        self.circle.move(dx,dy)
        self.center = self.circle.getCenter()

    def unDraw(self):
        self.circle.undraw()
            
    def drawRobot(self):
        self.circle.draw(self.win)
    
    def robotcolor(self,color):
        self.circle.setFill(color)
    