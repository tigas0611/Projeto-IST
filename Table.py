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
        
    def Position(self,numrows,distable,numtable,tablesizex,tablesizey,distdiv,numdivrows,Xdiv,ax,divgapx,ay,by):
        for i in range(numrows):
            for j in range(numdivrows):
                for k in range(2):
                    for l in range(numtable):
                        self.grouptables.append(g.Rectangle(g.Point((distable + k*(ax) + i*divgapx),(Xdiv + distdiv + j*(by) + l*(ay))),
                                                            g.Point((tablesizex + distable + k*(ax) + i*divgapx),(tablesizey + Xdiv+distdiv + j*(by) + l*(ay)))))

    def draw_group(self,win):
        for table in self.grouptables:
            table.draw(win)
            
class TableDivision():
    def __init__(self):
        self.groupdividers = []
        
    def Position(self,numrows,numdivrows,distable,tablesizex,divgapx,divgapy,divwidth,distdiv,by):
        for i in range(numrows):
            for j in range(numdivrows):
                self.groupdividers.append(g.Rectangle(g.Point((distable + tablesizex + divtablegap + i*(divgapx)) , (distdiv + j*(by))),
                                                      g.Point((divwidth + distable + tablesizex + divtablegap + i*(divgapx)), (divlenght + distdiv + j*(divlenght + divgapy)))))

    def draw_group(self,win):    
            for divider in self.groupdividers:
                divider.draw(win)

class Platedelivery():
    def __init__(self):
        self.Platedelivery = []
        
    def Position(self,sizex,Platedeliveryx,Platedeliveryy): 
        self.Platedelivery.append(g.Rectangle(g.Point((sizex/2) - (Platedeliveryx/2), 0), g.Point((sizex/2) + (Platedeliveryx/2), Platedeliveryy)))
    
    def draw_group(self,win):
            for Platedelivery in self.Platedelivery:
                Platedelivery.draw(win)        
    
table = Table()
table_div = TableDivision()   
plates = Platedelivery()

for line in f:
    if line == None:
        continue
    
    elif 'Table size' in line:
        values = line.split(': ')
        medidas = values[1].split(' x ')
        tablesizex = int(medidas[0])
        tablesizey = int(medidas[1])
        
    elif 'Divider width' in line:
        values = line.split(': ')
        divwidth = int(values[1])
    
    elif 'Number of tables per divisory' in line:
        values = line.split(': ')
        numtable = int(values[1])
    
    elif 'Number of dividers per row' in line:
        values = line.split(': ')
        numdivrows = int(values[1])
        
    elif 'Number of rows' in line:
        values = line.split(': ')
        numrows = int(values[1])
        
    elif 'Gap between tables' in line:
        values = line.split(': ')
        tablegapy = int(values[1])
        
    elif 'Gap between walls and tables' in line:
        values = line.split(': ')
        distable = int(values[1])
        
    elif 'Gap between dividers and tables' in line:
        values = line.split(': ')
        divtablegap = int(values[1])
    
    elif 'Plate delivery size' in line:
        values = line.split(': ')
        Platedelivery = values[1].split(' x ')
        Platedeliveryx = int(Platedelivery[0])
        Platedeliveryy = int(Platedelivery[1])
    
    elif 'Gap between walls and dividers' in line:
        values = line.split(': ')
        distdiv = int(values[1])
    
    elif 'Divider extra size' in line:
        values = line.split(': ')
        Xdiv = int(values[1])
        
    elif 'Gap between dividers (vertical)' in line:
        values = line.split(': ')
        divgapy = int(values[1])
    
    elif 'Gap between dividers (horizontal)' in line:
        values = line.split(': ')
        divgapx = int(values[1])
  
f.close()
       
win = g.GraphWin('Planta da Sala', 800,600)

sizex = 2*(tablesizex + divtablegap + distable) + divwidth + (numrows - 1)*divgapx

divlenght = (2*Xdiv + numtable*(tablesizey + tablegapy) - tablegapy)

sizey = 2*(distdiv) + (numdivrows - 1)*divgapy + divlenght

ax = tablesizex + 2*divtablegap + divwidth
ay = tablegapy + tablesizey

by = divlenght + divgapy

win.setCoords(0, sizex, sizey, 0)
        

table.Position(numrows,distable,numtable,tablesizex,tablesizey,distdiv,numdivrows,Xdiv,ax,divgapx,ay,by)
table_div.Position(numrows,numdivrows,distable,tablesizex,divgapx,divgapy,divwidth,distdiv,by)
plates.Position(sizex,Platedeliveryx,Platedeliveryy)
    
table.draw_group(win)
table_div.draw_group(win)
plates.draw_group(win)

win.getMouse()
win.close()