# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:51:36 2025

@author: gabri
"""

import graphics as gr

class QuitButton:
    def __init__(self, win, center, size, label):
        self.center = center
        self.size = size
        self.circle = gr.Circle(center, size)
        self.circle.setFill('red')
        self.circle.setOutline('black')
        self.circle.setWidth(5)
        self.circle.draw(win)
        self.label = gr.Text(center, label)
        self.label.setFill('white')
        self.label.setSize(18)
        self.label.setStyle("bold")
        self.label.draw(win)
        
    def pressed(self,click):
        distance = ((self.center.getX() - click.getX())**2 + (self.center.getY() - click.getY())**2)**(1/2)
        if distance <= self.size:
            return(True)
        else:
            return(False)