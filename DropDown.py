# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:51:36 2025

@author: gabri
"""

import graphics as gr

"A classe DropDown é reponsável por criar um botão que permita ao utilizador ver o dropdown do programa."
class DropDown:
    "Quando iniciada a classe cria e desenha um retângulo verde com texto no meio."
    def __init__(self, win, startpoint, finishpoint, label):
        self.startpoint = startpoint
        self.finishpoint = finishpoint
        self.button = gr.Rectangle(startpoint, finishpoint)
        self.button.setFill('green')
        self.button.setOutline('black')
        self.button.setWidth(3)
        self.button.draw(win)
        self.label = gr.Text(self.button.getCenter(), label)
        self.label.setFill('white')
        self.label.setSize(12)
        self.label.setStyle("bold")
        self.label.draw(win)
      
    "A função pressed recebe um ponto e se esse ponto for no interior do reângulo cria e desenha o dropdown com o nome da disciplina, autores e ano letivo e espera que o utilizador pressione o mouse para remover o dropdown."
    def pressed(self,click, win, roomsizeX, roomsizeY):
        if self.startpoint.getX() < click.getX() < self.finishpoint.getX() and self.startpoint.getY() < click.getY() < self.finishpoint.getY():
            background = gr.Rectangle(gr.Point(roomsizeX*0.1, roomsizeY*0.1), gr.Point(roomsizeX*0.9, roomsizeY*0.9))
            title1 = gr.Text(gr.Point(roomsizeX/2, roomsizeY*0.3), 'Fundamentos de Programação')
            title2 = gr.Text(gr.Point(roomsizeX/2, roomsizeY*0.5), 'Gabriel Neto nr 113613 \n \nTiago Antunes nr 114532')
            title3 = gr.Text(gr.Point(roomsizeX/2, roomsizeY*0.7), '2024/2025')
            title1.setTextColor('white')
            title2.setTextColor('white')
            title3.setTextColor('white')
            title1.setStyle('bold')
            title2.setStyle('bold')
            title3.setStyle('bold')
            textsize = int(roomsizeY*0.15)
            title1.setSize(textsize)
            title2.setSize(textsize)
            title3.setSize(textsize)
            background.setFill('grey')
            background.draw(win)
            title1.draw(win)
            title2.draw(win)
            title3.draw(win)
            win.getMouse()
            background.undraw()
            title1.undraw()
            title2.undraw()
            title3.undraw()
      
    "As funções active e unactive mudam a cor do butão para dar feedback visual ao utilizador sobre o seu estado de funcionamento."
    def active(self):
        self.button.setFill('green')
        self.label.setFill('white')
        
    def unactive(self):
        self.button.setFill('dark green')
        self.label.setFill('grey')