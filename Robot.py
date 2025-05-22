# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:47:07 2025
Classe Cara
@author: tiago
"""

import graphics as g

class Robot:
    def __init__(self, window, center):
        self.center = center
        self.OvalP1X = self.center.getX() - 3
        self.OvalP1Y = self.center.getY() - 4
        self.OvalP2X = self.center.getX() + 3
        self.OvalP2Y = self.center.getY() + 4
        self.Oval = g.Oval(g.Point(self.OvalP1X,self.OvalP1Y),g.Point(self.OvalP2X,self.OvalP2Y))
        self.window = window
        self.drawRobot()
    
    def move(self, dx, dy):
        self.Oval.move(dx,dy)
        self.center = self.Oval.getCenter()




    def unDraw(self):
        self.Oval.undraw()
        
            
    def drawRobot(self):
        self.Oval.draw(self.window)
    
    
    