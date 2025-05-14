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
        self.group_tables=[]


        
    def Position(self,line):
        if 'Table'in line:
            value=line.strip().split()
            self.group_tables.append(eval(value[1]))

            #for i in range(1,len(values)):
                #values[i]=int(values[i])
            #for j in range(2):
                #for k in range(3):
                    #self.group_tables.append(g.Rectangle(g.Point(line[1]+j*198,line[2]+k*84),
                                                   #g.Point(line[3]+j*198,line[4]+k*84)))
        

    def draw_group(self,win):
        for table in self.group_tables:
            table.draw(win)
            
class Table_Division():   
    def __init__(self):
        self.group_division=[]

        
        
    def Position(self,line):
        if 'Division'in line:
            value=line.split()
            self.group_division.append(eval(value[1]))

    def draw_group(self,win):    
            for table in self.group_division:
                table.draw(win)



class Docking_Station():
    def __init__(self):
        self.group_docking=[]


        
    def Position(self,line):
        if 'Docking'in line:
            value=line.strip().split()
            self.group_docking.append(eval(value[1]))
            #for i in range(1,len(values)):
                #values[i]=int(values[i])
            #for j in range(2): 
                #self.group_docking.append(g.Rectangle(g.Point(line[1],line[2]),
                                               #g.Point(line[3],line[4])))
    
    def draw_group(self,win):
            for table in self.group_docking:
                table.draw(win)        
        
        
        
table=Table()
table_div=Table_Division()   
docking=Docking_Station()         

for line in f:
    if 'Parede'in line:
        value=line.split()
        parede=eval(value[1])    
        parede.draw(win)
    table.Position(line)
    table_div.Position(line)
    docking.Position(line)
    
table.draw_group(win)
table_div.draw_group(win)
docking.draw_group(win)




