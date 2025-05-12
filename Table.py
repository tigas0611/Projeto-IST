# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:01 2025
Proj class Table 
@author: tiago
"""
import graphics as g

win=g.GraphWin('planta', 600,800)
f=open('salaxx.txt','r')

class Table:
    def __init__(self):
        self.tables=[]
        self.divisórias=[]      
        
    def mesa(self,line,win):
        if line[0]=='table':
            for i in range(1,len(values)):
                values[i]=int(values[i]) 
            self.tables.append(g.Rectangle(g.Point(line[1],line[2]),
                                           g.Point(line[3],line[4])))
            
    def divisoria(self,x,y):
        self.divisórias.append(g.Rectangle(g.Point(x+1,y-10),g.Point(x+3,y+6*14)))
        for i in self.divisórias:    
            i.draw(win)
        
            
        
table=Table()

for line in f:
    values=line.split()
    if values[0]=='parede':
        for i in range(1,len(values)):
            values[i]=int(values[i])    
        paredes=g.Rectangle(g.Point(values[1],values[2]),g.Point(values[3],values[4]))

    table.mesa(values,win)