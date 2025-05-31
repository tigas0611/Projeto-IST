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
        self.action = gr.Circle(gr.Point(center.getX() - size/2, center.getY()), size/4)
        self.battery = gr.Circle(gr.Point(center.getX() + size/2, center.getY()), size/4)
        self.dock = gr.Circle(center, size + 1)
        self.circle.setFill('light grey')
        self.action.setFill('pink')
        self.battery.setFill('light green')
        self.charge = 2
        self.circle.draw(win)
        self.battery.draw(win) 
        self.action.draw(win)
        self.dock.draw(win)
    
    def move(self, dx, dy):
        self.circle.move(dx,dy)
        self.action.move(dx, dy)
        self.battery.move(dx, dy)
        self.center = self.circle.getCenter()

    def unDraw(self):
        self.circle.undraw()
            
    def drawRobot(self, win):
        self.circle.draw(win)
        
    def setIdle(self):
        self.action.setFill('pink')

    def receivingRequest(self):
        self.action.setFill('orange')
        
    def deliveringRequest(self):
        self.action.setFill('light blue')
        
    def depleteBattery(self):
        self.charge -= 1
        if self.charge == 1:
            self.battery.setFill('yellow')
            return(False)
        elif self.charge == 0:
            self.battery.setFill('red')
            return(True)
        
    def chargeBattery(self):
        self.charge == 2
        self.battery.setFill('light green')
            