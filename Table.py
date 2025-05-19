# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:01 2025
Proj class Table 
@author: tiago
"""
import graphics as g

win=g.GraphWin('planta', 800,600)
f=open('salaxx.txt','r')

class Table:
    def __init__(self):
        self.group_tables=[]


        
    def Position(self,rows,dist,nºtable,):
        for i in range(rows):
            for j in range(div):
                for k in range(2):
                    self.group_tables.append(g.Rectangle(g.Point(distable+,),
                                                         g.Point(,)))
                    


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
    if 'Tamanho das mesas' in line:
        values=line.split(':')
        medidas=values.split(':')
        tablesizex=int(medidas[0])
        tablesizex=int(medidas[1])
    if 'Tamanho das divisórias' in line:
        line.split(':')
        divsize=int(line[1])
    
    if 'nº de mesas por divisoria' in line:
        line.split(':')
        tablediv=int(line[1])
    
    if 'nº de divisórias por fila' in line:
        line.split(':')
        nºdivrows=int(line[1])
        
    if 'nº de filas' in line:
        line.split(':')
        nºrows=int(line[1])
        
    if 'espaço entre filas' in line:
        line.split(':')
        rowsgap=int(line[1])
        
    if 'espaço entre mesas' in line:
        line.split(':')
        tablegap=int(line[1])
        
    if 'espaço entre as mesas e as paredes' in line:
        line.split(':')
        distable=int(line[1])
        
    if 'espaço entre as mesas e as divisórias' in line:
        line.split(':')
        divgap=int(line[1])
    
    if 'Tamanho da docking Station' in line:
        line.split(':')
        docking=int(line[1])
    
    if 'espaço entre as paredes e a divisórias' in line:
        line.split(':')
        distdiv=int(line[1])
    
    if 'extra parte da divisória' in line:
        line.split(':')
        Xdiv=int(line[1])
        
    if 'espaço entre divisórias' in line:
        line.split(':')
        splitdiv=int(line[1])
        
    if 'escala' in line:
        line.split(':')
        scale=int(line[1])
         
sizex=nºrows*(2*(tablesizex + divgap) + divsize) + (nºrows-1)*rowsgap + 2*(distable)

sizey=2*(distdiv) + 2*nºdivrows*Xdiv + (nºdivrows-1)*splitdiv + tablediv*tablesizey  
+ (tablediv-1)*tablegap  

win.setCoords(0, scale*sizey, scale*sizex, 0)
        
        
    table.Position(line)
    table_div.Position(line)
    docking.Position(line)
    
table.draw_group(win)
table_div.draw_group(win)
docking.draw_group(win)




