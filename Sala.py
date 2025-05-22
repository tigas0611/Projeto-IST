# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:53:09 2025

@author: gabri
"""

import graphics as gr

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
                        
                        tablestart = gr.Point(currentoffsetX, currentoffsetY)
                        tablefinish = gr.Point(tablesizeX + currentoffsetX, tablesizeY + currentoffsetY)
                        
                        self.grouptables.append(gr.Rectangle(tablestart, tablefinish))

    def draw_group(self,win):
        for table in self.grouptables:
            table.draw(win)
            
class Divider():
    def __init__(self):
        self.groupdividers = []
        
    def Position(self,numrows,numdividers,tablewallgapX,tablesizeX,dividergapX,dividergapY,dividersizeX,dividerwallgapY,divideroffsetY,tabledividergapX,dividersizeY):
        for rownum in range(numrows):
            for dividernum in range(numdividers):
                
                currentoffsetX = tablewallgapX + tablesizeX + tabledividergapX + rownum*dividergapX
                currentoffsetY = dividerwallgapY + dividernum*divideroffsetY
                
                dividerstart = gr.Point(currentoffsetX, currentoffsetY)
                dividerfinish = gr.Point(dividersizeX + currentoffsetX, dividersizeY + currentoffsetY)
                
                self.groupdividers.append(gr.Rectangle(dividerstart, dividerfinish))

    def draw_group(self,win):    
            for divider in self.groupdividers:
                divider.draw(win)

class Platedelivery():
    def __init__(self):
        self.Platedelivery = []
        
    def Position(self,sizeX,Platedeliveryx,Platedeliveryy):
        
        platedeliverystart = gr.Point((sizeX - Platedeliveryx)/2, 0)
        platedeliveryfinish = gr.Point((sizeX + Platedeliveryx)/2, Platedeliveryy)
        
        self.Platedelivery.append(gr.Rectangle(platedeliverystart,platedeliveryfinish))
    
    def draw_group(self,win):
            for Platedelivery in self.Platedelivery:
                Platedelivery.draw(win)