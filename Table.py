# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:01 2025
Proj class Table 
@author: tiago
"""
import graphics as g

win=g.GrapghWin('planta', 600,800)
f=open('salaxx.txt','r')

class Table:
    def __init__(self):
        self.tables=[]
        self.mesa()
        
    def mesa(self,line):
        if line[0]=='table':
            self.tables.append(g.Rectangle(g.Point(line[1],line[2]),
                                           g.Point(line[3],line[4])))
            self.tables.draw(win)
            self.divisoria(line[3],line[4])
    def divisoria(self,x,y):
        self.divisória.append(g.Rectangle())
table=Table()

for line in f:
    table
    if line[0]=='parede':
        paredes=g.Rectancle(g.Point(line[1],line[2]),g.Point(line[3],line[4]))
        