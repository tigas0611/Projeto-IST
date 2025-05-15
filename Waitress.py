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
    def __init__(self,win,center,size,group):
        self.robo=C.Face(win,center,size)
        self.move(group)
    
    def move(self,group):
        i=0
        dx=1 
        dy=0
        while True:
            botão=win.checkKey()
            if botão=='d':
                dx=1
                dy=0
            if botão=='w':
                dx=0
                dy=-1
            if botão=='a':
                dx=-1
                dy=0
            if botão=='s':
                dx=0
                dy=1
            self.colision(group)
            self.robo.move(dx,dy)
            g.update(60)

        
    def colision(self,group):
        dx=self.robo.center.getX()
        dy=self.robo.center.getY()
        for i in group:
            ix1=i.getP1().getX()
            iy1=i.getP1().getY()
            ix2=i.getP2().getX()
            iy2=i.getP2().getY()
            if ix2>dx>ix1: 
                if iy1>dy>iy2:
                    i.setFill("red")
                    print(5)
                
                
    #def drawFace(self):
        #self.robo.drawFace()
        
        

robô=Waiter(win,g.Point(390,120),15,T.table.group_tables)
