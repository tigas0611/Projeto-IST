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
        self.robô=C.Face(win,center,size)
        self.colision()
    def move(self):
        self.robô
        
    def colision(self):
        dx=self.robô.center.getX()
        dy=self.robô.center.getY()
        
        
        

robô=Waiter(win,g.Point(150,106,5))
robô.drawFace()
T.table.draw_group(win)
T.table_div.draw_group(win)
T.docking.draw_group(win)