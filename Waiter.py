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
    def __init__(self, win, center, size):
        self.win = win
        self.robot = ro.Robot(win, center, size)
        
    def checkX(self, targetX):
        if targetX ==self.center.getX():
            return(True)
        else:
            return(False)
        
    def checkY(self, targetY):
        if targetY ==self.center.getY():
            return(True)
        else:
            return(False)
    
    def softmotionX(self,dx):
        if dx < 0:
            dx*=-1
            for i in range(int(dx)):
                self.robot.move(-1, 0)
                gr.update(60)
        else:
            for i in range(int(dx)):
                self.robot.move(1, 0)
                gr.update(60)
                
    def softmotionY(self,dy):
        if dy < 0:
            dy*=-1
            for i in range(int(dy)):
                self.robot.move(0, -1)
                gr.update(60)
        else:
            for i in range(int(dy)):
                self.robot.move(0, 1)
                gr.update(60)
                
    def actionindicator(self,action):
        'Serving Table'
        if action == 'Serve table':
            self.robot.robotcolor('blue')
            
        'Taking orders'
        if action == 'Take order':
            self.robot.robotcolor('orange')

    def pathfinding(self, group, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividersizeX, platedeliveryy, numrows, sizeX):
        selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy - self.robot.center.getY()
        dockingplatedeliverygapX = sizeX/2 - self.robot.center.getX()
        button = self.win.getMouse()
        buttonX = button.getX()
        buttonY = button.getY() 
        for tablenum in group:
            currenttablestartX = tablenum.getP1().getX()
            currenttablestartY = tablenum.getP1().getY()
            currenttablefinishX = tablenum.getP2().getX()
            currenttablefinishY = tablenum.getP2().getY()
            if currenttablestartX < buttonX < currenttablefinishX and currenttablestartY < buttonY < currenttablefinishY:
                mark = gr.Circle(tablenum.getCenter(), 1)
                mark.setFill('red')
                mark.draw(self.win)
                #---------------------------------------------
                "Pathfinding"
                self.softmotionY(selectionlanegapY)
                
                "Lane Select"
                tableeven = None
                rownum = 0
                while tableeven is None and rownum < numrows:
                    distancenoteven = tablewallgapX + tabledividergapX + rownum*dividergapX
                    distanceeven = distancenoteven + 2*tablesizeX + tabledividergapX + dividersizeX
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
                    
                self.softmotionX(targetX - self.robot.center.getX())
                
                "Table Select"
                self.softmotionY(mark.getCenter().getY() - self.robot.center.getY())
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
                        
                self.softmotionX(deliverypostionX - self.robot.center.getX())
                #processamento do pedido
                ti.sleep(2)
                
                #ir ao plate delivery
                self.softmotionX(targetX - self.robot.center.getX())
                selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy - self.robot.center.getY()
                self.softmotionY(selectionlanegapY)
                dockingplatedeliverygapX = sizeX/2 - self.robot.center.getX()
                self.softmotionX(dockingplatedeliverygapX)
                ti.sleep(2)

                #serve table
                self.softmotionX(targetX - self.robot.center.getX())
                self.softmotionY(mark.getCenter().getY() - self.robot.center.getY())
                self.softmotionX(deliverypostionX - self.robot.center.getX())
                
                #docking station regresso


                    


                    
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
            if currenttablefinishX+5 > (dx**2 + dy**2)*0.5 > currenttablestartX+5 and currenttablefinishY+5 > (dx**2 + dy**2)*0.5 > currenttablestartY+5:
                i.setFill("black")
                return True