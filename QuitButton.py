# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 09:51:36 2025

@author: gabri
"""

import graphics as gr

"A classe QuitButton é reponsável por criar um botão que permita ao utilizador sair do programa de forma controlada."
class QuitButton:
    "Quando iniciada a classe cria e desenha um retângulo vermelho com texto no meio."
    def __init__(self, win, startpoint, finishpoint, label):
        self.startpoint = startpoint
        self.finishpoint = finishpoint
        self.button = gr.Rectangle(startpoint, finishpoint)
        self.button.setFill('red')
        self.button.setOutline('black')
        self.button.setWidth(3)
        self.button.draw(win)
        self.label = gr.Text(self.button.getCenter(), label)
        self.label.setFill('white')
        self.label.setSize(12)
        self.label.setStyle("bold")
        self.label.draw(win)
        
    "A função pressed recebe um ponto e retorna True se esse ponto for no interior do reângulo ou False em caso contrário."
    def pressed(self,click):
        if self.startpoint.getX() < click.getX() < self.finishpoint.getX() and self.startpoint.getY() < click.getY() < self.finishpoint.getY():
            return(True)
        else:
            return(False)
        
    "As funções active e unactive mudam a cor do butão para dar feedback visual ao utilizador sobre o seu estado de funcionamento."
    def active(self):
        self.button.setFill('red')
        self.label.setFill('white')
        
    def unactive(self):
        self.button.setFill('dark red')
        self.label.setFill('grey')