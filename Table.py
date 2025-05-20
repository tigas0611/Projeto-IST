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
        self.group_tables=[]
        
    def Position(self,scale,numrows,distable,numtable,tablesizex,tablesizey,divgap,divsize,distdiv,numdivrows,tablegapx,tablegapy,Xdiv,splitdiv,ax,bx):
        for i in range(numrows):
            for j in range(numdivrows):
                for k in range(2):
                    for l in range(numtable):
                        self.group_tables.append(g.Rectangle(
                            g.Point(scale*(distable + k*(ax)+ i*bx),
                                    scale*(Xdiv+distdiv + j*(2*Xdiv+numtable*(tablesizey+tablegapy)-tablegapy) +l*(tablesizey+tablegapy))),
                            g.Point(scale*(tablesizex + distable + (i+k)*(tablesizex+2*divgap + divsize)+ i*(tablegapx+tablesizex)),
                                    scale*(tablesizey + Xdiv+distdiv + j*(2*Xdiv+numtable*(tablesizey+tablegapy)-tablegapy+splitdiv) +l*(tablesizey+tablegapy)))))
        print(self.group_tables)

    def draw_group(self,win):
        for table in self.group_tables:
            table.draw(win)
            
class Table_Division():   
    def __init__(self):
        self.group_division=[]
        
    def Position(self,scale,numrows,numdivrows,distable,tablesizex,Xdiv,numtable,tablesizey,tablegapy,divgap,divsize,distdiv,splitdiv):
        divlenght=scale*(2*Xdiv+numtable*(tablesizey+tablegapy)-tablegapy)
        for i in range(numrows):
            for j in range(numdivrows):
                self.group_division.append(g.Rectangle(g.Point(scale*(distable+tablesizex+i*(2*tablesizex+2*divgap+divsize)) , scale*(distdiv+j*(divlenght+splitdiv))),
                                           g.Point(scale*(divsize+distable+tablesizex+i*(2*tablesizex+2*divgap+divsize)),scale*(divlenght+distdiv+j*(divlenght+splitdiv)))))

    def draw_group(self,win):    
            for division in self.group_division:
                division.draw(win)

class Docking_Station():
    def __init__(self):
        self.group_docking=[]
        
    def Position(self,line):
        if 'Docking'in line:
            value=line.strip().split()
            self.group_docking.append(eval(value[1]))
    
    def draw_group(self,win):
            for table in self.group_docking:
                table.draw(win)        
    
table = Table()
table_div = Table_Division()   
docking = Docking_Station()

for line in f:
    if line == None:
        continue
    
    elif 'Table size' in line:
        values = line.split(':')
        medidas = values[1].split('x')
        tablesizex = int(medidas[0])
        tablesizey = int(medidas[1])
        
    elif 'Divider width' in line:
        values = line.split(':')
        divwidth = int(values[1])
    
    elif 'Number of tables per divisory' in line:
        values = line.split(':')
        numtable = int(values[1])
    
    elif 'Number of dividers per row' in line:
        values = line.split(':')
        numdivrows = int(values[1])
        
    elif 'Number of rows' in line:
        values = line.split(':')
        numrows = int(values[1])
        
    elif 'Gap between tables' in line:
        values = line.split(':')
        tablegap = values[1].split('x')
        tablegapx = int(tablegap[0])
        tablegapy = int(tablegap[1])
        
    elif 'Gap between walls and tables' in line:
        values = line.split(':')
        distable = int(values[1])
        
    elif 'Gap between dividers and tables' in line:
        values = line.split(':')
        divtablegap = int(values[1])
    
    elif 'Docking Station size' in line:
        values = line.split(':')
        docking = values[1].split('x')
        dockingx = int(docking[0])
        dockingy = int(docking[1])
    
    elif 'Gap between walls and dividers' in line:
        values = line.split(':')
        distdiv = int(values[1])
    
    elif 'Divider extra size' in line:
        values = line.split(':')
        Xdiv = int(values[1])
        
    elif 'Gap between divider' in line:
        values = line.split(':')
        splitdiv = int(values[1])
        
    elif 'Scale' in line:
        values = line.split(':')
        scale = int(values[1])
  
f.close()
       
win = g.GraphWin('Planta da Sala', 800,600)

sizex = numrows*(2*(tablesizex + divtablegap) + divwidth) + (numrows-1)*tablegapx + 2*(distable)

sizey = 2*(distdiv) + 2*numdivrows*Xdiv + (numdivrows-1)*splitdiv + numtable*tablesizey 
+ (numtable-1)*tablegap
  
divlenght=scale*(2*Xdiv+numtable*(tablesizey+tablegapy)-tablegapy)

ax = tablesizex + 2*divtablegap + divwidth
ay = tablegapy + tablesizey

bx = ax + tablesizex + tablegapx
by = numtable*(ay) - tablesizey
#win.setCoords(0, scale*sizey, scale*sizex, 0)
        

table.Position(scale,numrows,distable,numtable,tablesizex,tablesizey,divtablegap,divwidth,distdiv,numdivrows,tablegapx,tablegapy,Xdiv,splitdiv,ax,bx)
table_div.Position(scale,numrows,numdivrows,distable,tablesizex,Xdiv,numtable,tablesizey,tablegapy,divtablegap,divwidth,distdiv,splitdiv)
#docking.Position(line)
    
table.draw_group(win)
table_div.draw_group(win)
#docking.draw_group(win)

win.getMouse()
win.close()




