# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:10:03 2025
Waiter
@author: tiago
"""

import Robot as ro
import graphics as gr
import time as ti

class Waiter():
    def __init__(self, win, center, group, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividersizeX, platedeliveryy, numrows, sizeX):
        self.win = win
        self.robot = ro.Robot(win, center)
        self.move(group, center, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividersizeX, platedeliveryy, numrows, sizeX)

    def move(self, group, center, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividersizeX, platedeliveryy, numrows, sizeX):
        while True:
            centerX = self.robot.center.getX()
            centerY = self.robot.center.getY()
            
            selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy - centerY
            dockingplatedeliverygapX = sizeX/2 - centerX
            
            button = self.win.getMouse()
            buttonX = button.getX()
            buttonY = button.getY() 
            for i in group:
                currenttablestartX = i.getP1().getX()
                currenttablestartY = i.getP1().getY()
                currenttablefinishX = i.getP2().getX()
                currenttablefinishY = i.getP2().getY()
                if currenttablestartX < buttonX < currenttablefinishX and currenttablestartY < buttonY < currenttablefinishY:
                    mark = gr.Circle(i.getCenter(), 1)
                    mark.setFill('red')
                    mark.draw(self.win)
                    #---------------------------------------------
                    "Pathfinding"
                    self.robot.move(0, selectionlanegapY)
                    ti.sleep(1)
                    self.robot.move(dockingplatedeliverygapX, 0)
                    ti.sleep(1)
                    
                    "Lane Select"
                    tableeven = None
                    rownum = 0
                    while tableeven is None and rownum < numrows:
                        distanceeven = tablewallgapX + 2*(tablesizeX + tabledividergapX) + dividersizeX + rownum*dividergapX
                        distancenoteven = tablewallgapX + tabledividergapX + rownum*dividergapX
                        if currenttablestartX < distancenoteven + tablesizeX:
                            tableeven = False
                        elif currenttablestartX < distanceeven:
                            tableeven = True
                        rownum += 1
                    
                    midlanehalfsizeX = (dividergapX - dividersizeX - 2*(tablesizeX + tabledividergapX))/2
                    
                    if currenttablestartX < tablewallgapX + tablesizeX:
                        targetX = tablewallgapX/2
                        extremes = True
                    elif currenttablefinishX > sizeX - tablewallgapX - tablesizeX:
                        targetX = sizeX - tablewallgapX/2
                        extremes = True
                    elif tableeven is True:
                        targetX = distanceeven + midlanehalfsizeX
                        extremes = False
                    elif tableeven is False:
                        targetX = distancenoteven - midlanehalfsizeX
                        extremes = False
                    self.robot.move(targetX - self.robot.center.getX(), 0)
                    ti.sleep(1)
                    
                    "Table Select"
                    self.robot.move(0, mark.getCenter().getY() - self.robot.center.getY())
                    ti.sleep(1)
                    if extremes is True:
                        if tableeven is False:
                            deliverypostionX = tablewallgapX - 4
                        elif tableeven is True:
                            deliverypostionX = sizeX - tablewallgapX + 4
                    elif extremes is False:
                        if tableeven is True:
                            deliverypostionX = distanceeven + 4
                        elif tableeven is False: 
                            deliverypostionX = distancenoteven - 4
                    self.robot.move(deliverypostionX - self.robot.center.getX(), 0)
                    ti.sleep(1)
                    self.robot.move(targetX - self.robot.center.getX(), 0)
                    #---------------------------------------------
                    mark.undraw()
            #self.colision(group)
            
            

    def colision(self, group):
        dx = self.robot.center.getX()
        dy = self.robot.center.getY()
        for i in group:
            currenttablestartX = i.getP1().getX()
            currenttablestartY = i.getP1().getY()
            currenttablefinishX = i.getP2().getX()
            currenttablefinishY = i.getP2().getY()
            if currenttablefinishX+5 > dx and dx > currenttablestartX-5 and currenttablefinishY+5 > dy and dy > currenttablestartY-5:
                i.setFill("black")
                return True

    # def drawFace(self):
        # self.robot.drawFace()


