# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:53:09 2025
Classes reponsáveis por desenhar a planta da sala
@author: gabri
"""

import graphics as gr

"A classe Table é reponsável por criar e desenhar todas as mesas presentes na sala assim como armazenar informação sobre elas."
class Table:
    "Quando iniciada a classe cria uma lista vazia para armazenar informação sobre todas as mesas criadas."
    def __init__(self):
        self.grouptables = []
        
    "A função position recebe multiplos parâmetros do ficheiro salaxx que são utilizados para calcular a posição de todas as mesas."
    def position(self, numrows, tablewallgapX, numtables, tablesizeX, tablesizeY, dividerwallgapY, numdividers, dividerextrasizeY, tableoffsetX, dividergapX, tableoffsetY, divideroffsetY):
        
        "O primeiro loop cria as mesas em todas as colunas especificadas na variável numrows."
        for rownum in range(numrows):
            
            "O segundo loop cria as mesas em todos os divisores de cada coluna especidicados na variável numdividers."
            for dividernum in range(numdividers):
                
                "O terceiro loop cria as mesas aos pares para que haja uma de cada lado do divisor, a variável d vem do inglês para duplo, double."
                for d in range(2):
                    
                    "Por fim, o quarto loop cria o número de mesas especificadas na variável numtables à esquerda do divisor."
                    for tablenum in range(numtables):
                        
                        "Estas duas variáveis calculam e armazenam as coordenadas do primeiro vértice de cada mesa."
                        currentoffsetX = tablewallgapX + d*tableoffsetX + rownum*dividergapX
                        currentoffsetY = dividerextrasizeY + dividerwallgapY + dividernum*divideroffsetY + tablenum*tableoffsetY
                        
                        "Estas duas variáveis criam os pontos necessários para desenhar cada mesa."
                        tablestart = gr.Point(currentoffsetX, currentoffsetY)
                        tablefinish = gr.Point(tablesizeX + currentoffsetX, tablesizeY + currentoffsetY)
                        
                        "Por fim, a mesa é adcionada à lista de mesas criadas."
                        self.grouptables.append(gr.Rectangle(tablestart, tablefinish))

    "A função drawGroup desenha todas as mesas já criadas."
    def drawGroup(self,win):
        for table in self.grouptables:
            table.setFill('chocolate4')
            table.draw(win)
           
"A classe Divider é reponsável por criar e desenhar todos os divisores presentes na sala assim como armazenar informação sobre eles."
class Divider():
    def __init__(self):
        "Quando iniciada a classe cria uma lista vazia para armazenar informação sobre todos os divisores criados."
        self.groupdividers = []
        
    "A função position recebe multiplos parâmetros do ficheiro salaxx que são utilizados para calcular a posição de todos os divisores."
    def position(self, numrows, numdividers, tablewallgapX, tablesizeX, dividergapX, dividergapY, dividersizeX, dividerwallgapY, divideroffsetY, tabledividergapX, dividersizeY):
        
        "O primeiro loop cria os divisores em todas as colunas especificadas na variável numrows."
        for rownum in range(numrows):
            
            "O segundo loop cria o número de divisores especificados na variável numdividers em cada coluna."
            for dividernum in range(numdividers):
                
                "Estas duas variáveis calculam e armazenam as coordenadas do primeiro vértice de cada divisor."
                currentoffsetX = tablewallgapX + tablesizeX + tabledividergapX + rownum*dividergapX
                currentoffsetY = dividerwallgapY + dividernum*divideroffsetY
                
                "Estas duas variáveis criam os pontos necessários para desenhar cada divisor."
                dividerstart = gr.Point(currentoffsetX, currentoffsetY)
                dividerfinish = gr.Point(dividersizeX + currentoffsetX, dividersizeY + currentoffsetY)
                
                "Por fim, o divisor é adcionado à lista de divisores criados."
                self.groupdividers.append(gr.Rectangle(dividerstart, dividerfinish))

    "A função drawGroup desenha todos os divisores já criados."
    def drawGroup(self,win):    
            for divider in self.groupdividers:
                divider.setFill('brown')
                divider.draw(win)

"A classe PlateDelivery é reponsável por criar e desenhar a entrega de pratos e armazenar informação sobre ela."
class PlateDelivery():
    def __init__(self):
        self.platedelivery = None
        
    "A função position recebe multiplos parâmetros do ficheiro salaxx que são utilizados para calcular a posição da entrega de pratos."
    def position(self, roomsizeX, platedeliveryx, platedeliveryy, bordersX, bordersY):
        
        "Estas duas variáveis criam os pontos necessários para desenhar a entrega de pratos."
        platedeliverystart = gr.Point(bordersX + (roomsizeX - platedeliveryx)/2, bordersY)
        platedeliveryfinish = gr.Point(bordersX + (roomsizeX + platedeliveryx)/2, platedeliveryy + bordersY)
        
        self.platedelivery = gr.Rectangle(platedeliverystart, platedeliveryfinish)
    
    "A função draw desenha a entrega de pratos."
    def draw(self,win):
        self.platedelivery.setFill('light grey')
        self.platedelivery.draw(win)
        
"A classe Chess e responsável por criar um padrão xadrez no chão do restaurante por motivos decorativos."
class Chess():
    "Quando iniciada a classe cria uma lista vazia para armazenar informação sobre todos os quadrados que fazem parte do xadrez."
    def __init__(self):
        self.chess = []
       
    "A função position recebe multiplos parâmetros do ficheiro salaxx que são utilizados para calcular a posição dos quadrados que fazem parte do xadrez."
    def position(self, platedeliveryY, roomsizeX):
        
        "O primeiro loop preenche a sala verticalemnete com quadrados."
        for rownum in range(int(roomsizeX/platedeliveryY) + 1):
            
            "O segundo loop preenche a sala horizontalmente com quadrados alternando as cores para formar um padrão xadrez."
            for squarenum in range(int(roomsizeX/platedeliveryY) + 1):
                currentoffsetY = 2*rownum*platedeliveryY
                currentoffsetX = 2*squarenum*platedeliveryY
                
                squarestart = gr.Point(currentoffsetX, currentoffsetY)
                squarefinish = gr.Point(currentoffsetX + platedeliveryY , currentoffsetY + platedeliveryY)
                
                square = gr.Rectangle(squarestart, squarefinish)
                square.setFill('cadetblue1')
                
                self.chess.append(square)
                
                currentoffsetX += platedeliveryY
                
                squarestart = gr.Point(currentoffsetX, currentoffsetY)
                squarefinish = gr.Point(currentoffsetX + platedeliveryY , currentoffsetY + platedeliveryY)
                
                square = gr.Rectangle(squarestart, squarefinish)
                square.setFill('thistle1')
                
                self.chess.append(square)
                
                currentoffsetX -= platedeliveryY
                currentoffsetY += platedeliveryY
                
                squarestart = gr.Point(currentoffsetX, currentoffsetY)
                squarefinish = gr.Point(currentoffsetX + platedeliveryY , currentoffsetY + platedeliveryY)
                
                square = gr.Rectangle(squarestart, squarefinish)
                square.setFill('thistle1')
                
                self.chess.append(square)
                
                currentoffsetX += platedeliveryY
                
                squarestart = gr.Point(currentoffsetX, currentoffsetY)
                squarefinish = gr.Point(currentoffsetX + platedeliveryY , currentoffsetY + platedeliveryY)
                
                square = gr.Rectangle(squarestart, squarefinish)
                square.setFill('cadetblue1')
                
                self.chess.append(square)
                
    "A função drawGroup desenha todos os quadrados que fazem parte do xadrez."
    def drawGroup(self,win):    
            for square in self.chess:
                square.draw(win)
        