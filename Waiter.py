# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:10:03 2025
Waiter
@author: tiago
"""

import Robot as ro
import graphics as gr
import time as ti
'Classe Waiter que tem como base a classe Robô'
class Waiter():
    def __init__(self, win, center, size, tablegroup, dividergroup):
        self.size = size
        self.win = win
        self.robot = ro.Robot(win, center, size)
        self.tablegroup = tablegroup
        self.dividergroup = dividergroup
        self.obstacles = []

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
        'Para o programa ter interação com o utilizador mesmo em alturas de movimento e até mesmo animação de movimento'
    def softMotionX(self,dx):
        requests = []
        obstacles = []
        if dx < 0:
            dx*=-1
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick))
                    if self.requesttacker(mouseclick) == None:
                        obstacle = self.obstacle(mouseclick)
                        self.obstacles.extend(obstacle)
                self.robot.move(-1, 0)
                gr.update(120)
        else:
            for i in range(int(dx)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick))
                    if self.requesttacker(mouseclick) == None:
                        obstacle = self.obstacle(mouseclick)
                        self.obstacles.extend(obstacle)
                self.robot.move(1, 0)
                gr.update(120)
                
        dados = [requests, obstacles]
        return dados

    def softMotionY(self,dy):
        requests = []
        obstacles = []
        if dy < 0:
            dy*=-1
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick)) 
                    if self.requesttacker(mouseclick) == None:
                        obstacle = self.obstacle(mouseclick)
                        self.obstacles.extend(obstacle)
                self.robot.move(0, -1)
                gr.update(120)
        else:
            for i in range(int(dy)):
                mouseclick = self.win.checkMouse()
                if mouseclick != None:
                    self.requesttacker(mouseclick)
                    requests.append(self.requesttacker(mouseclick))
                    if self.requesttacker(mouseclick) == None:
                        obstacle = self.obstacle(mouseclick)
                        self.obstacles.extend(obstacle)
                self.robot.move(0, 1)
                gr.update(120)
                
        dados = [requests, obstacles]
        return dados
    'Quando os pontos no perimetro do robo entram em contacto com algum objeto da lista referida ele para e o objeto fica preto'
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
                ti.sleep(2)
                obstacle.undraw()
                
    
    'Considera qualquer clique do utilizador q estaje no interior de alguma mesa como pedido'        
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
            


                
        
        'Criação de objetos nos pontos onde o utilizador clica'   
    def obstacle(self, mouseclick):
            obstacle = []
            obstacle.append(gr.Circle(mouseclick, 2*self.size/3 ))
            for human in obstacle:
                human.setFill('black')
                human.draw(self.win)
            return obstacle
                    
            
        
        
    'Sistema de colunas e linhas por onde o robo se desloca para ir de encontro ao ponto desejado'
    def pathfinding(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark):
        currenttablefinishX = mark.getCenter().getX() + tablesizeX/2
        currenttablestartX = mark.getCenter().getX() - tablesizeX/2
        selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy
                #---------------------------------------------
        "Pathfinding"
        self.robot.receivingRequest()
                
        affinity = abs(selectionlanegapY - mark.getCenter().getY()) + abs(selectionlanegapY - self.robot.center.getY())
        targetY = selectionlanegapY
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
        dados = [targetX, targetY, mark, deliverypositionX, roomsizeX, platedeliveryy, dividerwallgapY]
        return dados
            
    'Movimento entre as colunas e linhas criadas no pathfind que leva o robo do seu ponto até a mesa de entrega de pratos'
    def Platedeliverymove(self, targetX, targetY, mark, roomsizeX, platedeliveryy, dividerwallgapY):
        mark.setFill('red')
        mark.draw(self.win)
        requestbetweendelivers = []
        obstacles = []
        valores = self.softMotionX(targetX - self.robot.center.getX())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        
        selectionlanegapY = (dividerwallgapY - platedeliveryy)/2 + platedeliveryy
        valores = self.softMotionY(selectionlanegapY - self.robot.center.getY())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        
        valores = self.softMotionX(targetX - self.robot.center.getX())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        dockingplatedeliverygapX = roomsizeX/2 - self.robot.center.getX()
        valores = self.softMotionX(dockingplatedeliverygapX)
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        ti.sleep(2)
        mark.undraw()
        
        dados = [requestbetweendelivers, obstacles]
        return dados


    'Movimento entre as colunas e linhas criadas no pathfind que leva o robo do seu ponto até a mesa referida'
    def Tablemove(self, targetX, targetY, mark, deliverypositionX):
        mark.setFill('red')
        mark.draw(self.win)
        requestbetweendelivers = []
        obstacles = []
        #Going to the table

        valores = self.softMotionY(targetY - self.robot.center.getY())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)
        
        valores  = self.softMotionX(targetX - self.robot.center.getX())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        
        valores = self.softMotionY(mark.getCenter().getY() - self.robot.center.getY())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)

        
        valores = self.softMotionX(deliverypositionX - self.robot.center.getX())
        requests = valores[0]
        obstacle = valores[1]
        requestbetweendelivers.extend(requests)
        obstacles.extend(obstacle)
        
        ti.sleep(2)
        mark.undraw()
        dados = [requestbetweendelivers, obstacles]
        return dados

    'Movimento geral do robo'
    def move(self, tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, platedeliveryx, numrows, numdividers, roomsizeX, mouseclick):
        requestsdelivering = []
        requestbetweendelivers = []        
        if self.requesttacker(mouseclick) != None:
            requestsdelivering.append(self.requesttacker(mouseclick))
            while len(requestsdelivering) != 0:
                for i in range(2):
                    for mark in requestsdelivering:
                        dados = self.pathfinding(tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mark)
                        valores = self.Tablemove(dados[0], dados[1], dados[2], dados[3])
                        requestbetweendelivers.extend(valores[0])
                        self.obstacles.extend(valores[1])
                        
                    valores = self.Platedeliverymove(dados[0], dados[1], dados[2], dados[4], dados[5], dados[6])
                    requestbetweendelivers.extend(valores[0])
                    self.obstacles.extend(valores[0])

                    if i == 1:
                        if  self.robot.depleteBattery() == True :
                            
                            valores = self.softMotionX(platedeliveryx/2 + 6)
                            requestbetweendelivers.extend(valores[0])
                            self.obstacles.extend(valores[1])
                            
                            valores = self.softMotionY(-1*(platedeliveryy/2 + self.size))
                            requestbetweendelivers.extend(valores[0])
                            self.obstacles.extend(valores[1])
                            self.robot.chargeBattery()
                    
                requestsdelivering = requestbetweendelivers
                requestbetweendelivers = []
        else:
            self.obstacles.extend(self.obstacle(mouseclick))
            
            
                

                

        

                    
               
            
    