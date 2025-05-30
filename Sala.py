# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:53:09 2025

@author: gabri
"""

import graphics as gr

class Table:
    def __init__(self):
        self.grouptables = []
        
    def Position(self, numrows, tablewallgapX, numtables, tablesizeX, tablesizeY, dividerwallgapY, numdividers, dividerextrasizeY, tableoffsetX, dividergapX, tableoffsetY, divideroffsetY, scale):
        for rownum in range(numrows):
            for dividernum in range(numdividers):
                for d in range(2):
                    for tablenum in range(numtables):
                        
                        currentoffsetX = tablewallgapX + d*tableoffsetX + rownum*dividergapX
                        currentoffsetY = dividerextrasizeY + dividerwallgapY + dividernum*divideroffsetY + tablenum*tableoffsetY
                        
                        tablestart = gr.Point(scale*currentoffsetX, scale*currentoffsetY)
                        tablefinish = gr.Point(scale*(tablesizeX + currentoffsetX), scale*(tablesizeY + currentoffsetY))
                        
                        self.grouptables.append(gr.Rectangle(tablestart, tablefinish))

    def draw_group(self,win):
        for table in self.grouptables:
            table.draw(win)
            
class Divider():
    def __init__(self):
        self.groupdividers = []
        
    def Position(self, numrows, numdividers, tablewallgapX, tablesizeX, dividergapX, dividergapY, dividersizeX, dividerwallgapY, divideroffsetY, tabledividergapX, dividersizeY, scale):
        for rownum in range(numrows):
            for dividernum in range(numdividers):
                
                currentoffsetX = tablewallgapX + tablesizeX + tabledividergapX + rownum*dividergapX
                currentoffsetY = dividerwallgapY + dividernum*divideroffsetY
                
                dividerstart = gr.Point(scale*currentoffsetX, scale*currentoffsetY)
                dividerfinish = gr.Point(scale*(dividersizeX + currentoffsetX), scale*(dividersizeY + currentoffsetY))
                
                self.groupdividers.append(gr.Rectangle(dividerstart, dividerfinish))

    def draw_group(self,win):    
            for divider in self.groupdividers:
                divider.draw(win)

class PlateDelivery():
    def __init__(self):
        self.platedelivery = []
        
    def Position(self, roomsizeX, platedeliveryx, platedeliveryy, scale):
        
        platedeliverystart = gr.Point(scale*(roomsizeX - platedeliveryx)/2, 0)
        platedeliveryfinish = gr.Point(scale*(roomsizeX + platedeliveryx)/2, scale*platedeliveryy)
        
        self.platedelivery.append(gr.Rectangle(platedeliverystart, platedeliveryfinish))
    
    def draw_group(self,win):
            for platedelivery in self.platedelivery:
                platedelivery.draw(win)