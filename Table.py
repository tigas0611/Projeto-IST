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
    def __init__(self,values,win):
        self.group_tables=[]
        self.group_division=[]
        self.tables(values)
        self.division(values)
        self.planta(win)

        
    def tables(self,line):
        if line[0]=='mesa':
            for i in range(1,len(values)):
                values[i]=int(values[i])
            for j in range(2):
                for k in range(3):
                    self.group_tables.append(g.Rectangle(g.Point(line[1]+j*198,line[2]+k*84),
                                                   g.Point(line[3]+j*198,line[4]+k*84)))

            
    def division(self,line):
        if line[0]=='divisória':
            for i in range(1,len(values)):
                values[i]=int(values[i])
            for j in range(2): 
                self.group_division.append(g.Rectangle(g.Point(line[1]+j*198,line[2]),
                                               g.Point(line[3]+j*198,line[4])))
        
    def planta(self,win):
        for table in self.group_tables:
            table.draw(win)
        for divisoria in self.group_division:
            divisoria.draw(win)
            


class Docking_station():
    def __init__(self):
        self.base()
        
            
        

for line in f:
    values=line.split()
    table=Table(values,win)
    if values[0]=='parede':
        for i in range(1,len(values)):
            values[i]=int(values[i])    
        paredes=g.Rectangle(g.Point(values[1],values[2]),g.Point(values[3],values[4]))
        paredes.draw(win)
    
    print(table.group_tables)
