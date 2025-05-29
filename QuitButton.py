# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:51:36 2025

@author: gabri
"""

import graphics as gr

class QuitButton:
    def __init__(self, win, startpoint, finishpoint, label):
        self.startpoint = startpoint
        self.finishpoint = finishpoint
        button = gr.Rectangle(startpoint, finishpoint)
        button.setFill('red')
        button.setOutline('black')
        button.setWidth(3)
        button.draw(win)
        label = gr.Text(button.getCenter(), label)
        label.setFill('white')
        label.setSize(12)
        label.setStyle("bold")
        label.draw(win)
        
    def pressed(self,click):
        if self.startpoint.getX() < click.getX() < self.finishpoint.getX() and self.startpoint.getY() < click.getY() < self.finishpoint.getY():
            return(True)
        else:
            return(False)