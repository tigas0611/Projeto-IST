# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:01 2025
Proj class Table 
@author: tiago
"""
import graphics as g

f = open('salaxx.txt','r')

class Table:
    def __init__(self):
        self.grouptables = []
        
    def Position(self,numrows,tablewallgapX,numtables,tablesizeX,tablesizeY,dividerwallgapY,numdividers,dividerextrasizeY,ax,dividergapX,ay,by):
        for i in range(numrows):
            for j in range(numdividers):
                for k in range(2):
                    for l in range(numtables):
                        self.grouptables.append(g.Rectangle(g.Point((tablewallgapX + k*(ax) + i*dividergapX),(dividerextrasizeY + dividerwallgapY + j*(by) + l*(ay))),
                                                            g.Point((tablesizeX + tablewallgapX + k*(ax) + i*dividergapX),(tablesizeY + dividerextrasizeY+dividerwallgapY + j*(by) + l*(ay)))))

    def draw_group(self,win):
        for table in self.grouptables:
            table.draw(win)
            
class Divider():
    def __init__(self):
        self.groupdividers = []
        
    def Position(self,numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividerX,dividerwallgapY,by):
        for i in range(numrows):
            for j in range(numdividers):
                self.groupdividers.append(g.Rectangle(g.Point((tablewallgapX + tablesizeX + tabledividergapX + i*(dividergapX)) , (dividerwallgapY + j*(by))),
                                                      g.Point((dividerX + tablewallgapX + tablesizeX + tabledividergapX + i*(dividergapX)), (divlenght + dividerwallgapY + j*(divlenght + dividergapY)))))

    def draw_group(self,win):    
            for divider in self.groupdividers:
                divider.draw(win)

class Platedelivery():
    def __init__(self):
        self.Platedelivery = []
        
    def Position(self,sizeX,Platedeliveryx,Platedeliveryy): 
        self.Platedelivery.append(g.Rectangle(g.Point((sizeX/2) - (Platedeliveryx/2), 0), g.Point((sizeX/2) + (Platedeliveryx/2), Platedeliveryy)))
    
    def draw_group(self,win):
            for Platedelivery in self.Platedelivery:
                Platedelivery.draw(win)        
    
table = Table()
divider = Divider()   
platedelivery = Platedelivery()

for line in f:
    if line == None:
        continue
    
    elif 'Table size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        tablesizeX = int(values2[0])
        tablesizeY = int(values2[1])
        
    elif 'Divider width' in line:
        values = line.split(': ')
        dividerX = int(values[1])
    
    elif 'Number of tables per divisory' in line:
        values = line.split(': ')
        numtables = int(values[1])
    
    elif 'Number of dividers per row' in line:
        values = line.split(': ')
        numdividers = int(values[1])
        
    elif 'Number of rows' in line:
        values = line.split(': ')
        numrows = int(values[1])
        
    elif 'Gap between tables' in line:
        values = line.split(': ')
        tablegapY = int(values[1])
        
    elif 'Gap between walls and tables' in line:
        values = line.split(': ')
        tablewallgapX = int(values[1])
        
    elif 'Gap between dividers and tables' in line:
        values = line.split(': ')
        tabledividergapX = int(values[1])
    
    elif 'Plate delivery size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        Platedeliveryx = int(values2[0])
        Platedeliveryy = int(values2[1])
    
    elif 'Gap between walls and dividers' in line:
        values = line.split(': ')
        dividerwallgapY = int(values[1])
    
    elif 'Divider extra size' in line:
        values = line.split(': ')
        dividerextrasizeY = int(values[1])
        
    elif 'Gap between dividers (vertical)' in line:
        values = line.split(': ')
        dividergapY = int(values[1])
    
    elif 'Gap between dividers (horizontal)' in line:
        values = line.split(': ')
        dividergapX = int(values[1])
  
f.close()
       
win = g.GraphWin('Planta da Sala', 800,600)

sizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + dividerX + (numrows - 1)*dividergapX

divlenght = (2*dividerextrasizeY + numtables*(tablesizeY + tablegapY) - tablegapY)

sizeY = 2*(dividerwallgapY) + (numdividers - 1)*dividergapY + divlenght

ax = tablesizeX + 2*tabledividergapX + dividerX
ay = tablegapY + tablesizeY

by = divlenght + dividergapY

win.setCoords(0, sizeX, sizeY, 0)
        

table.Position(numrows,tablewallgapX,numtables,tablesizeX,tablesizeY,dividerwallgapY,numdividers,dividerextrasizeY,ax,dividergapX,ay,by)
divider.Position(numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividerX,dividerwallgapY,by)
platedelivery.Position(sizeX,Platedeliveryx,Platedeliveryy)
    
table.draw_group(win)
divider.draw_group(win)
platedelivery.draw_group(win)

win.getMouse()
win.close()