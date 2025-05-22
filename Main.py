# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:51:07 2025

@author: gabri
"""

import graphics as gr
import Sala as sa

f = open('salaxx.txt','r')

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

sizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + (numrows - 1)*dividergapX + dividersizeX
dividersizeY = 2*dividerextrasizeY + numtables*(tablesizeY + tablegapY) - tablegapY
sizeY = 2*(dividerwallgapY) + numdividers*(dividergapY + dividersizeY) - dividergapY

tableoffsetX = tablesizeX + 2*tabledividergapX + dividersizeX
tableoffsetY = tablegapY + tablesizeY

divideroffsetY = dividersizeY + dividergapY

table = sa.Table()
divider = sa.Divider()   
platedelivery = sa.Platedelivery()

table.Position(numrows,tablewallgapX,numtables,tablesizeX,tablesizeY,dividerwallgapY,numdividers,dividerextrasizeY,tableoffsetX,dividergapX,tableoffsetY,divideroffsetY)
divider.Position(numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividersizeX,dividerwallgapY,divideroffsetY,tabledividergapX,dividersizeY)
platedelivery.Position(sizeX,Platedeliveryx,Platedeliveryy)

win = gr.GraphWin('Planta da Sala', 800,600)
win.setCoords(0, sizeY, sizeX, 0)

table.draw_group(win)
divider.draw_group(win)
platedelivery.draw_group(win)

win.getMouse()
win.close()