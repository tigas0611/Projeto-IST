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
        
    def Position(self,numrows,tablewallgapX,numtables,tablesizeX,tablesizeY,dividerwallgapY,numdividers,dividerextrasizeY,tableoffsetX,dividergapX,tableoffsetY,divideroffsetY):
        for rownum in range(numrows):
            for dividernum in range(numdividers):
                for d in range(2):
                    for tablenum in range(numtables):
                        
                        currentoffsetX = tablewallgapX + d*tableoffsetX + rownum*dividergapX
                        currentoffsetY = dividerextrasizeY + dividerwallgapY + dividernum*divideroffsetY + tablenum*tableoffsetY
                        
                        tablestart = g.Point(currentoffsetX, currentoffsetY)
                        tablefinish = g.Point(tablesizeX + currentoffsetX, tablesizeY + currentoffsetY)
                        
                        self.grouptables.append(g.Rectangle(tablestart, tablefinish))

    def draw_group(self,win):
        for table in self.grouptables:
            table.draw(win)
            
class Divider():
    def __init__(self):
        self.groupdividers = []
        
    def Position(self,numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividersizeX,dividerwallgapY,divideroffsetY):
        for rownum in range(numrows):
            for dividernum in range(numdividers):
                
                currentoffsetX = tablewallgapX + tablesizeX + tabledividergapX + rownum*dividergapX
                currentoffsetY = dividerwallgapY + dividernum*divideroffsetY
                
                dividerstart = g.Point(currentoffsetX, currentoffsetY)
                dividerfinish = g.Point(dividersizeX + currentoffsetX, dividersizeY + currentoffsetY)
                
                self.groupdividers.append(g.Rectangle(dividerstart, dividerfinish))

    def draw_group(self,win):    
            for divider in self.groupdividers:
                divider.draw(win)

class Platedelivery():
    def __init__(self):
        self.Platedelivery = []
        
    def Position(self,sizeX,Platedeliveryx,Platedeliveryy):
        
        platedeliverystart = g.Point((sizeX - Platedeliveryx)/2, 0)
        platedeliveryfinish = g.Point((sizeX + Platedeliveryx)/2, Platedeliveryy)
        
        self.Platedelivery.append(g.Rectangle(platedeliverystart,platedeliveryfinish))
    
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
        dividersizeX = int(values[1])
    
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
        
    elif 'Gap between dividers (horizontal)' in line:
        values = line.split(': ')
        dividergapX = int(values[1])
        
    elif 'Gap between dividers (vertical)' in line:
        values = line.split(': ')
        dividergapY = int(values[1])
    
f.close()

sizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + numrows*(dividersizeX + dividergapX) - dividergapX
dividersizeY = 2*dividerextrasizeY + numtables*(tablesizeY + tablegapY) - tablegapY
sizeY = 2*(dividerwallgapY) + numdividers*(dividergapY + dividersizeY) - dividergapY

tableoffsetX = tablesizeX + 2*tabledividergapX + dividersizeX
tableoffsetY = tablegapY + tablesizeY

divideroffsetY = dividersizeY + dividergapY

table.Position(numrows,tablewallgapX,numtables,tablesizeX,tablesizeY,dividerwallgapY,numdividers,dividerextrasizeY,tableoffsetX,dividergapX,tableoffsetY,divideroffsetY)
divider.Position(numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividersizeX,dividerwallgapY,divideroffsetY)
platedelivery.Position(sizeX,Platedeliveryx,Platedeliveryy)

win = g.GraphWin('Planta da Sala', 800,600)
win.setCoords(0, sizeY, sizeX, 0)    

table.draw_group(win)
divider.draw_group(win)
platedelivery.draw_group(win)

#win.getMouse()
#win.close()