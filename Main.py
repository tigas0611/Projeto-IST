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
        platedeliveryx = int(values2[0])
        platedeliveryy = int(values2[1])
    
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

roomsizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + (numrows - 1)*dividergapX + dividersizeX
dividersizeY = 2*dividerextrasizeY + numtables*(tablesizeY + tablegapY) - tablegapY
roomsizeY = 2*(dividerwallgapY) + numdividers*(dividergapY + dividersizeY) - dividergapY

scaleY = windowsizeY/roomsizeY
scaleX = windowsizeX/roomsizeX

# scale used depends on the lower side
if scaleX < scaleY:
    scale = scaleX
    borderY = (windowsizeY/scale - roomsizeY)/2
    borderX = 0
else:
    scale = scaleY
    borderX = (windowsizeX/scale - roomsizeX)/2
    borderY = 0

dividerwallgapY += borderY
tablewallgapX += borderX


tableoffsetX = tablesizeX + 2*tabledividergapX + dividersizeX
tableoffsetY = tablegapY + tablesizeY

divideroffsetY = dividersizeY + dividergapY

table = sa.Table()
divider = sa.Divider()   
platedelivery = sa.PlateDelivery()

table.position(numrows, tablewallgapX, numtables, tablesizeX, tablesizeY, dividerwallgapY, numdividers, dividerextrasizeY, tableoffsetX, dividergapX, tableoffsetY, divideroffsetY)
divider.position(numrows, numdividers, tablewallgapX, tablesizeX, dividergapX, dividergapY, dividersizeX, dividerwallgapY, divideroffsetY, tabledividergapX, dividersizeY)
platedelivery.position(roomsizeX, platedeliveryx, platedeliveryy, borderX, borderY)

win = gr.GraphWin('Planta da Sala', windowsizeX, windowsizeY)
win.setCoords(0, windowsizeY/scale, windowsizeX/scale, 0)

roomsizeX = windowsizeX/scale
roomsizeY = windowsizeY/scale
            
table.drawGroup(win)
divider.drawGroup(win)
platedelivery.draw(win)

quitbutton = qb.QuitButton(win, gr.Point(1, 1), gr.Point(12, 9), 'Quit')
waiter = wa.Waiter(win, gr.Point((roomsizeX + platedeliveryx)/2 + 6, platedeliveryy/2), 4, table.grouptables, divider.groupdividers)

close = False
while close is False:
    quitbutton.active(win)
    mouseclick = win.getMouse()
    if quitbutton.pressed(mouseclick) is True:
        close = True
    else:
        quitbutton.unactive()
        waiter.pedidotacker(tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mouseclick)
    gr.update(60)
    
win.close()