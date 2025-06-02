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
        requests = []
        if dx < 0:
            dx*=-1
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick))
                self.robot.move(-1, 0)
                gr.update(60)
        else:
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick))
                self.robot.move(1, 0)
                gr.update(60)
        print(requests)
        return requests

    def softMotionY(self,dy):
        requests = []
        if dy < 0:
            dy*=-1
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick)) 
                self.robot.move(0, -1)
                gr.update(60)
        else:
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick)) 
                self.robot.move(0, 1)
                gr.update(60)
        print(requests)
        return requests
    
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
            
                return mark

                
        
        
    def obstacle(self, mouseclick):
        if self.pedidotacker(mouseclick) == False:
            gr.Circle(self.ped)
            
        
        

    def pathfinding(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark):
        mark.setFill('red')
        mark.draw(self.win)
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
                    targetY = currentrowY + dividerwallgapY/2
                else:
                    targetY = currentrowY + dividergapY/2


        
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
                
        tableinstructions = []
        requestbetweendelivers = []
        #Going to the table
        tableinstructions.append(targetY - self.robot.center.getY())
        requests = self.softMotionY(targetY - self.robot.center.getY())
        requestbetweendelivers.extend(requests)
        
        tableinstructions.append(targetX - self.robot.center.getX())
        requests = self.softMotionX(targetX - self.robot.center.getX())
        requestbetweendelivers.extend(requests) 
        
        tableinstructions.append(mark.getCenter().getY() - self.robot.center.getY())
        requests = self.softMotionY(mark.getCenter().getY() - self.robot.center.getY())
        requestbetweendelivers.extend(requests) 
        
        tableinstructions.append(deliverypositionX - self.robot.center.getX())
        requests = self.softMotionX(deliverypositionX - self.robot.center.getX())
        requestbetweendelivers.extend(requests)
        ti.sleep(2)
        
        #Going to Plate Delivery
        Platedeliveryinstructions = []
        Platedeliveryinstructions.append(targetX - self.robot.center.getX())
        requests = self.softMotionX(targetX - self.robot.center.getX())
        requestbetweendelivers.extend(requests)
        
        selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy
        Platedeliveryinstructions.append(selectionlanegapY - self.robot.center.getY())
        requests = self.softMotionY(selectionlanegapY - self.robot.center.getY())
        requestbetweendelivers.extend(requests)
        
        requests = self.softMotionX(targetX - self.robot.center.getX())   
        requestbetweendelivers.extend(requests)
        dockingplatedeliverygapX = roomsizeX/2 - self.robot.center.getX()
        requests = self.softMotionX(dockingplatedeliverygapX)
        requestbetweendelivers.extend(requests)
        requests = self.softMotionX(targetX - self.robot.center.getX())
        requestbetweendelivers.extend(requests)
        ti.sleep(2)
        
        #serve table
        requests = self.softMotionX(targetX - self.robot.center.getX())
        requestbetweendelivers.extend(requests)
        #instructions.append('x')
        requests = self.softMotionY(mark.getCenter().getY() - self.robot.center.getY())
        requestbetweendelivers.extend(requests)
        #instructions.append('x')
        requests = self.softMotionX(deliverypositionX - self.robot.center.getX())
        requestbetweendelivers.extend(requests)
        
        #---------------------------------------------
        mark.undraw()    
        #docking station regresso
        #self.robot.depleteBattery()
        return requestbetweendelivers
            
            
    def move(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mouseclick):
        requestsdelivering = []
        requestbetweendelivers = []
        if self.requesttacker(mouseclick) != None:
            requestsdelivering.append(self.requesttacker(mouseclick))
            while len(requestsdelivering) != 0:
                for mark in requestsdelivering:
                    print(mark)
                    requestbetweendelivers.extend(self.pathfinding(tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark))
                requestsdelivering = requestbetweendelivers
                requestbetweendelivers = []
            
                

                

        

                    
               
            
    