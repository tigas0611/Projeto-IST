# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:51:07 2025

@author: gabri
"""

import graphics as gr
import Sala as sa
import QuitButton as qb
import Waiter as wa

f = open('salaxx.txt','r')

for line in f:
    if line == None:
        continue
    
    elif 'Window size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        windowsizeX = int(values2[0])
        windowsizeY = int(values2[1])
    
    elif 'Table size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        tablesizeX = int(values2[0])
        tableroomsizeY = int(values2[1])
        
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
        platedeliveryx = int(values2[0])
        platedeliveryy = int(values2[1])
    
    elif 'Gap between walls and dividers' in line:
        values = line.split(': ')
        dividerwallgapY = int(values[1])
    
    elif 'Divider extra size' in line:
        values = line.split(': ')
        dividerextraroomsizeY = int(values[1])
        
    elif 'Gap between dividers (horizontal)' in line:
        values = line.split(': ')
        dividergapX = int(values[1])
        
    elif 'Gap between dividers (vertical)' in line:
        values = line.split(': ')
        dividergapY = int(values[1])
    
f.close()

roomsizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + (numrows - 1)*dividergapX + dividersizeX
dividerroomsizeY = 2*dividerextraroomsizeY + numtables*(tableroomsizeY + tablegapY) - tablegapY
roomsizeY = 2*(dividerwallgapY) + numdividers*(dividergapY + dividerroomsizeY) - dividergapY

scale = windowsizeY/roomsizeY

tableoffsetX = tablesizeX + 2*tabledividergapX + dividersizeX
tableoffsetY = tablegapY + tableroomsizeY

divideroffsetY = dividerroomsizeY + dividergapY

table = sa.Table()
divider = sa.Divider()   
platedelivery = sa.PlateDelivery()

table.Position(numrows, tablewallgapX, numtables, tablesizeX, tableroomsizeY, dividerwallgapY, numdividers, dividerextraroomsizeY, tableoffsetX, dividergapX, tableoffsetY, divideroffsetY, scale)
divider.Position(numrows, numdividers, tablewallgapX, tablesizeX, dividergapX, dividergapY, dividersizeX, dividerwallgapY, divideroffsetY, tabledividergapX, dividerroomsizeY, scale)
platedelivery.Position(roomsizeX, platedeliveryx, platedeliveryy, scale)

win = gr.GraphWin('Planta da Sala', windowsizeX, windowsizeY)

table.draw_group(win)
divider.draw_group(win)
platedelivery.draw_group(win)

quitbutton = qb.QuitButton(win, gr.Point(scale, scale), gr.Point(scale*12, scale*9), 'Quit')
robot = wa.Waiter(win, gr.Point(scale*(roomsizeX + platedeliveryx)/2 + 7, scale*platedeliveryy/2), 5)

close = False
while close is False:
    mouseclick = win.getMouse()
    if quitbutton.pressed(mouseclick) is True:
        close = True
    else:
        robot.pathfinding(table.grouptables, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividersizeX, platedeliveryy, numrows, roomsizeX)
    
win.close()