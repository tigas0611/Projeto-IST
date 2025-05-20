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


        
    def Position(self,scale,nºrows,distable,nºtable,tablesizex,tablesizey,divgap,divsize,distdiv,nºdivrows,tablegapx,tablegapy,Xdiv):
        for i in range(nºrows):
            for j in range(nºdivrows):
                for k in range(2):
                    for l in range(nºtable):
                        self.group_tables.append(g.Rectangle(g.Point(scale*(distable + (i+k)*(tablesizex+2*divgap + divsize)+ i*(tablegapx+tablesizex)),
                                                                     scale*(Xdiv+distdiv + j*(2*Xdiv+nºtable*(tablesizey+tablegapy)-tablegapy) +l*(tablesizey+tablegapy))),
                                                         g.Point(scale*(tablesizex + distable + (i+k)*(tablesizex+2*divgap + divsize)+ i*(tablegapx+tablesizex)),
                                                                 scale*(tablesizey + 2*distdiv + j*(2*Xdiv+nºtable*(tablesizey+tablegapy)-tablegapy) +l*(tablesizey+tablegapy)))))
        print(self.group_tables)


    def draw_group(self,win):
        for table in self.group_tables:
            table.draw(win)
            
class Table_Division():   
    def __init__(self):
        self.group_division=[]

        
        
    def Position(self,line):
        
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
#indiferença o nome da variavel values ou qualquer outro intermedio ser igual pois usamos só para aceder a valores dentro dela
for line in f:
    if 'Tamanho das mesas' in line:
        values=line.split(':')
        medidas=values[1].split('x')
        tablesizey=int(medidas[0])
        tablesizex=int(medidas[1])
    if 'Tamanho das divisórias' in line:
        values=line.split(':')
        divsize=int(values[1])
    
    if 'nº de mesas por divisoria' in line:
        values=line.split(':')
        nºtable=int(values[1])
    
    if 'nº de divisórias por fila' in line:
        values=line.split(':')
        nºdivrows=int(values[1])
        
    if 'nº de filas' in line:
        values=line.split(':')
        nºrows=int(values[1])
        
    if 'espaço entre mesas' in line:
        values=line.split(':')
        tablegap=values[1].split('x')
        tablegapy=int(tablegap[0])
        tablegapx=int(tablegap[1])
            
        
    if 'espaço entre as mesas e as paredes' in line:
        values=line.split(':')
        distable=int(values[1])
        
    if 'espaço entre as mesas e as divisórias' in line:
        values=line.split(':')
        divgap=int(values[1])
    
    if 'Tamanho da docking Station' in line:
        values=line.split(':')
        docking=values[1].split('x')
        dockingx=int(docking[1])
        dockingy=int(docking[0])
    
    if 'espaço entre as paredes e a divisórias' in line:
        values=line.split(':')
        distdiv=int(values[1])
    
    if 'extra parte da divisória' in line:
        values=line.split(':')
        Xdiv=int(values[1])
        
    if 'espaço entre divisórias' in line:
        values=line.split(':')
        splitdiv=int(values[1])
        
    if 'escala' in line:
        values=line.split(':')
        scale=int(values[1])
         
sizex=nºrows*(2*(tablesizex + divgap) + divsize) + (nºrows-1)*tablegapx + 2*(distable)

sizey=2*(distdiv) + 2*nºdivrows*Xdiv + (nºdivrows-1)*splitdiv + nºtable*tablesizey  
+ (nºtable-1)*tablegap  

#win.setCoords(0, scale*sizey, scale*sizex, 0)
        
        
table.Position(scale,nºrows,distable,nºtable,tablesizex,tablesizey,divgap,divsize,distdiv,nºdivrows,tablegapx,tablegapy,Xdiv)
#table_div.Position(line)
#docking.Position(line)
    
table.draw_group(win)
#table_div.draw_group(win)
#docking.draw_group(win)




