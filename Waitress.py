# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:10:03 2025
Waiter
@author: tiago
"""

import Cara as C
import graphics as g
import Table as T

win=T.win
class Waiter():
    def __init__(self,win,center,size):
        self.robo=C.Face(win,center,size)
        self.colision()
    def move(self):
        self.robo
        
    def colision(self):
        dx=self.robo.center.getX()
        dy=self.robo.center.getY()
    def drawFace(self):
        self.robo.drawFace()
        
        

robô=Waiter(win,g.Point(130,106),5)
robô.drawFace()
T.table.draw_group(win)
T.table_div.draw_group(win)
T.docking.draw_group(win)