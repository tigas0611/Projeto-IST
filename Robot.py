# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 11:47:07 2025
Classe Robot
@author: tiago
"""

import graphics as gr
import time as ti

"A classe Robot é responsável por criar o robô que serve as mesas e por implementar todos os metódos necessários ao seu funcionamento."
class Robot:
    
    "Quando iniciada a classe cria e desenha todos os componentes do robô assim como a sua docking station."
    def __init__(self, win, center, size):
        self.center = center
        self.circle = gr.Circle(center, size)
        self.action = gr.Circle(gr.Point(center.getX() - size/2, center.getY()), size/4)
        self.battery = gr.Circle(gr.Point(center.getX() + size/2, center.getY()), size/4)
        self.dock = gr.Circle(center, size + 1)
        self.circle.setFill('light grey')
        self.action.setFill('pink')
        self.battery.setFill('light green')
        self.dock.setFill('white')
        self.charge = 2
        self.dock.draw(win)
        self.circle.draw(win)
        self.battery.draw(win) 
        self.action.draw(win)
        
    "A função move movimenta o robô e todos os seus componentes nas direções verticais e horizontais."
    def move(self, dx, dy):
        self.circle.move(dx,dy)
        self.action.move(dx, dy)
        self.battery.move(dx, dy)
        self.center = self.circle.getCenter()
  
    "As três seguintes funções alteram a cor do indicador da esquerda do robô para indicar o seu estado atual."
    def setIdle(self):
        self.action.setFill('pink')

    def receivingRequest(self):
        self.action.setFill('orange')   
        
    def deliveringRequest(self):
        self.action.setFill('blue')
        
    "A função depleteBattery retira uma carga à bateria do robô e atualiza o indicador da direita para refletir essa mudança."
    def depleteBattery(self):
        self.charge -= 1
        if self.charge == 1:
            self.battery.setFill('yellow')
            return(False)
        elif self.charge == 0:
            self.battery.setFill('red')
            return(True)
        
    "A função chargeBattery recarrega a bateria e atualiza o indicador da direita para refletir essa mudança."
    def chargeBattery(self):
        self.battery.setFill('light blue')
        ti.sleep(2)
        self.charge == 2
        self.battery.setFill('light green')
            