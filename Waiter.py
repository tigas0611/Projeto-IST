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
    def __init__(self, win, center, size, tablegroup, dividergroup):
        self.win = win
        self.robot = ro.Robot(win, center, size)
        self.tablegroup = tablegroup
        self.dividergroup = dividergroup
        
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
    
    def softMotionX(self,dx):
        if dx < 0:
            dx*=-1
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                self.robot.move(-1, 0)
                gr.update(60)
        else:
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                self.robot.move(1, 0)
                gr.update(60) 
                
    def softMotionY(self,dy):
        if dy < 0:
            dy*=-1
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                self.robot.move(0, -1)
                gr.update(60)
        else:
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                self.robot.move(0, 1)
                gr.update(60)
                
    def colision(self, group):
        dx = self.robot.center.getX()
        dy = self.robot.center.getY()
        for obstacle in group:
            currenttablestartX = obstacle.getP1().getX()
            currenttablestartY = obstacle.getP1().getY()
            currenttablefinishX = obstacle.getP2().getX()
            currenttablefinishY = obstacle.getP2().getY()
            if currenttablefinishX+5 > (dx**2 + dy**2)*0.5 > currenttablestartX+5 and currenttablefinishY+5 > (dx**2 + dy**2)*0.5 > currenttablestartY+5:
                obstacle.setFill("black")
                return True
            
    def requesttacker(self, mouseclick):
        mouseclickX = mouseclick.getX()
        mouseclickY = mouseclick.getY() 
        for tablenum in self.tablegroup:
            currenttablestartX = tablenum.getP1().getX()
            currenttablestartY = tablenum.getP1().getY()
            currenttablefinishX = tablenum.getP2().getX()
            currenttablefinishY = tablenum.getP2().getY()
            if currenttablestartX < mouseclickX < currenttablefinishX and currenttablestartY < mouseclickY < currenttablefinishY:
                mark = gr.Circle(tablenum.getCenter(), 1)
                mark.setFill('red')
                mark.draw(self.win)
                return mark

        
        
    def obstacle(self, mouseclick):
        if self.pedidotacker(mouseclick) == False:
            gr.Circle(self.ped)
            
        
        

    def pathfinding(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark):
        currenttablefinishX = mark.getCenter().getX() + tablesizeX/2
        currenttablestartX = mark.getCenter().getX() - tablesizeX/2
        selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy
        dockingplatedeliverygapX = roomsizeX/2 - self.robot.center.getX()
                #---------------------------------------------
        "Pathfinding"
        self.robot.receivingRequest()
                
        affinity = abs(selectionlanegapY - mark.getCenter().getY()) + abs(selectionlanegapY - self.robot.center.getY())
        targetY = selectionlanegapY - self.robot.center.getY() 
        for dividernum in range(numdividers):
            currentrowY = dividerwallgapY + (dividersizeY + dividergapY)*(dividernum+1) - dividergapY
            if  abs(currentrowY - mark.getCenter().getY()) + abs(currentrowY - self.robot.center.getY()) < affinity:
                affinity = currentrowY
                if dividernum == numdividers-1:
                    targetY = currentrowY + dividerwallgapY/2 - self.robot.center.getY()
                else:
                    targetY = currentrowY + dividergapY/2 - self.robot.center.getY()  


        
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
            if   tablewallgapX/2 < midlanehalfsizeX:
                targetX = tablewallgapX/2
            else:
                targetX = tablewallgapX - midlanehalfsizeX
            extremes = True
        elif currenttablefinishX > roomsizeX - tablewallgapX - tablesizeX:
            if   tablewallgapX/2 < midlanehalfsizeX:
                targetX = roomsizeX - tablewallgapX/2
            else: 
                targetX = roomsizeX - tablewallgapX + midlanehalfsizeX
            extremes = True
        elif tableeven is True:
            targetX = distanceeven + midlanehalfsizeX
            extremes = False
        elif tableeven is False:
            targetX = distancenoteven - midlanehalfsizeX
            extremes = False
                
                
        "Table Select"
        
        if extremes is True:
            if tableeven is False:
                deliverypositionX = tablewallgapX - 6
            elif tableeven is True:
                deliverypositionX = roomsizeX - tablewallgapX + 6
        elif extremes is False:
            if tableeven is True:
                deliverypositionX = distanceeven + 6
            elif tableeven is False: 
                deliverypositionX = distancenoteven - 6
                
        #Going to the table
        instructions = []
        #self.softMotionY(targetY)
        #self.softMotionX(targetX - self.robot.center.getX())
        #self.softMotionY(mark.getCenter().getY() - self.robot.center.getY())            
        #self.softMotionX(deliverypositionX - self.robot.center.getX())
        instructions.append('y') 
        instructions.append(targetY)
        
        instructions.append('x')
        instructions.append(targetX - self.robot.center.getX())
        instructions.append('y')
        instructions.append(mark.getCenter().getY() - self.robot.center.getY())  
        instructions.append('x')
        instructions.append(deliverypositionX - self.robot.center.getX())
        ti.sleep(2)
            
        #Going to Plate Delivery
        #self.softMotionX(targetX - self.robot.center.getX())
        #selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy - self.robot.center.getY()
        #self.softMotionY(selectionlanegapY)
        #dockingplatedeliverygapX = roomsizeX/2 - self.robot.center.getX()
        #self.softMotionX(dockingplatedeliverygapX)
        #ti.sleep(2)
        #serve table
        #self.softMotionX(targetX - self.robot.center.getX())
        #self.softMotionY(mark.getCenter().getY() - self.robot.center.getY())
        #self.softMotionX(deliverypositionX - self.robot.center.getX())
            
        #docking station regresso
        #self.robot.depleteBattery()
        return instructions
            
            
    def move(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mouseclick):
        mark = self.requesttacker(mouseclick)
        
        instructions = self.pathfinding(tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark)
        print(instructions)
        for move in range(len(instructions)):
            if instructions[move] == 'x':
                self.softMotionX(instructions[move+1])
            
            elif instructions[move] == 'y':
                self.softMotionY(instructions[move+1])
                

                

        #---------------------------------------------
        mark.undraw()

                    
               
            
    