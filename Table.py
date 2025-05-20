# -*- coding: utf-8 -*-
"""
Created on Fri May  2 13:44:01 2025
Proj class Table 
@author: tiago
"""
import graphics as g

#win=g.GraphWin('planta', 800,600)
f=open('salaxx.txt','r')

class Table:
    def __init__(self):
        self.group_tables=[]


        
    def Position(self,scale,numrows,distable,numtable,tablesizex,tablesizey,divgap,divsize,distdiv,numdivrows,tablegapx,tablegapy,Xdiv,splitdiv):
        for i in range(numrows):
            for j in range(numdivrows):
                for k in range(2):
                    for l in range(numtable):
                        self.group_tables.append(g.Rectangle(
                            g.Point(scale*(distable + (i+k)*(tablesizex+2*divgap + divsize)+ i*(tablegapx+tablesizex)),
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
    if line==None:
        continue
    elif 'Tamanho das mesas' in line:
        values=line.split(':')
        medidas=values[1].split('x')
        tablesizex=int(medidas[0])
        tablesizey=int(medidas[1])
    elif 'Tamanho das divisórias' in line:
        values=line.split(':')
        divsize=int(values[1])
    
    elif 'num de mesas por divisoria' in line:
        values=line.split(':')
        numtable=int(values[1])
    
    elif 'num de divisórias por fila' in line:
        values=line.split(':')
        numdivrows=int(values[1])
        
    elif 'num de filas' in line:
        values=line.split(':')
        numrows=int(values[1])
        
    elif 'espaço entre mesas' in line:
        values=line.split(':')
        tablegap=values[1].split('x')
        tablegapy=int(tablegap[0])
        tablegapx=int(tablegap[1])
            
        
    elif 'espaço entre as mesas e as paredes' in line:
        values=line.split(':')
        distable=int(values[1])
        
    elif 'espaço entre as mesas e as divisórias' in line:
        values=line.split(':')
        divgap=int(values[1])
    
    elif 'Tamanho da docking Station' in line:
        values=line.split(':')
        docking=values[1].split('x')
        dockingx=int(docking[1])
        dockingy=int(docking[0])
    
    elif 'espaço entre as paredes e a divisórias' in line:
        values=line.split(':')
        distdiv=int(values[1])
    
    elif 'extra parte da divisória' in line:
        values=line.split(':')
        Xdiv=int(values[1])
        
    elif 'espaço entre divisórias' in line:
        values=line.split(':')
        splitdiv=int(values[1])
        
    elif 'escala' in line:
        values=line.split(':')
        scale=int(values[1])
         
sizex=numrows*(2*(tablesizex + divgap) + divsize) + (numrows-1)*tablegapx + 2*(distable)

sizey=2*(distdiv) + 2*numdivrows*Xdiv + (numdivrows-1)*splitdiv + numtable*tablesizey  
+ (numtable-1)*tablegap  

#win.setCoords(0, scale*sizey, scale*sizex, 0)
        
        
table.Position(scale,numrows,distable,numtable,tablesizex,tablesizey,divgap,divsize,distdiv,numdivrows,tablegapx,tablegapy,Xdiv,splitdiv)
table_div.Position(scale,numrows,numdivrows,distable,tablesizex,Xdiv,numtable,tablesizey,tablegapy,divgap,divsize,distdiv,splitdiv)
#docking.Position(line)
    
table.draw_group(win)
table_div.draw_group(win)
#docking.draw_group(win)

f.close()


