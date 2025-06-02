# -*- coding: utf-8 -*-
"""
Created on Thu May 22 16:51:07 2025

@author: gabri
"""

import graphics as gr
import Sala as sa
import QuitButton as qb
import DropDown as dd
import Waiter as wa
'Metodo para ler as informações da planta que foram escritas nesse ficheiro'
f = open('salaxx.txt','r')

'Dvider = divisória'
'ilhas = modulos das divisórias com as mesas'
'Rows = coluna de ilhas(conjunto das divisórias e mesas)'



'Ele vai ler cada linha do ficheiro e agrupar os valores q essas linhas indicam as suas variaveis correspondentes'
for line in f:
    if line == None:
        continue
    
        'Escolha do tamanho do ecrã'
    elif 'Window size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        windowsizeX = int(values2[0])
        windowsizeY = int(values2[1])
        
        'Tamanho das mesas'
    elif 'Table size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        tablesizeX = int(values2[0])
        tablesizeY = int(values2[1])
        
        'largura das divisórias'
    elif 'Divider width' in line:
        values = line.split(': ')
        dividersizeX = int(values[1])
    
        'Numero de mesas criadas por cada lado das divisórias'
    elif 'Number of tables per divisory' in line:
        values = line.split(': ')
        numtables = int(values[1])
    
        'Os dois proximos blocos de código vao determinar o numero de divisórias por sala'
        
        'O numero de divisórias na vertical'
    elif 'Number of dividers per row' in line:
        values = line.split(': ')
        numdividers = int(values[1])
      
        'O numero de colunas'
    elif 'Number of rows' in line:
        values = line.split(': ')
        numrows = int(values[1])
        
        'Espaço vertical entre as mesas'
    elif 'Gap between tables' in line:
        values = line.split(': ')
        tablegapY = int(values[1])
        
        'Distancia que as mesas terão das paredes no caso da horizontal'
    elif 'Gap between walls and tables' in line:
        values = line.split(': ')
        tablewallgapX = int(values[1])
        
        'Distancia que as divisórias terão das mesas na horizontal'
    elif 'Gap between dividers and tables' in line:
        values = line.split(': ')
        tabledividergapX = int(values[1])
    
        'Tamanho do local de entrega dos pedidos e saida dos pratos'
    elif 'Plate delivery size' in line:
        values = line.split(': ')
        values2 = values[1].split(' x ')
        platedeliveryx = int(values2[0])
        platedeliveryy = int(values2[1])
        
        'Distancia que as divisórias terão das paredes no caso da vertical'
    elif 'Gap between walls and dividers' in line:
        values = line.split(': ')
        dividerwallgapY = int(values[1])
        
        'Extra comonente vertical das divisórias para alem do tamanho das mesas e do espço entre elas'
    elif 'Divider extra size' in line:
        values = line.split(': ')
        dividerextrasizeY = int(values[1])
        
        ' Distancia entre as divisórias de colunas diferentes (componente horizontal)'
    elif 'Gap between dividers (horizontal)' in line:
        values = line.split(': ')
        dividergapX = int(values[1])
        
        ' Distancia entre as divisórias da mesma coluna (componente horizontal)'
    elif 'Gap between dividers (vertical)' in line:
        values = line.split(': ')
        dividergapY = int(values[1])
'Já foram retiradas todas as informações do ficheiro não sendo mais necessário ele estar aberto'   
f.close()

'Tamanho da sala Horizontal'
roomsizeX = 2*(tablewallgapX + tablesizeX + tabledividergapX) + (numrows - 1)*dividergapX + dividersizeX
'Tamanho real das divisórias(vertical)'
dividersizeY = 2*dividerextrasizeY + numtables*(tablesizeY + tablegapY) - tablegapY

'Tamanho da sala Vertical'
roomsizeY = 2*(dividerwallgapY) + numdividers*(dividergapY + dividersizeY) - dividergapY

'escala para maior preenchimento do ecrã na componete X e Y'
scaleY = windowsizeY/roomsizeY
scaleX = windowsizeX/roomsizeX
'Escala aplicada depende da menor razão entre as componetes X e Y do tamanho da sala com o tamanho do ecrã'
if scaleX < scaleY:
    scale = scaleX
    'Componente X e Y dos espaços vazios n preenchidos pela escala'
    borderY = (windowsizeY/scale - roomsizeY)/2
    borderX = 0
else:
    'Componente X e Y dos espaços vazios n preenchidos pela escala'
    scale = scaleY
    borderX = (windowsizeX/scale - roomsizeX)/2
    borderY = 0

'Espaços vazios adicionados às bordas da sala'
dividerwallgapY += borderY
tablewallgapX += borderX

'Valores deslocamento dos processos de construção das mesas'
tableoffsetX = tablesizeX + 2*tabledividergapX + dividersizeX
tableoffsetY = tablegapY + tablesizeY

'Valores deslocamento dos processos de construção das divisórias'
divideroffsetY = dividersizeY + dividergapY


'Objetos das classes Table, Divider, PlateDelivery'
table = sa.Table()
divider = sa.Divider()   
platedelivery = sa.PlateDelivery()

'Criação das mesas no Table, diviórias no Divider e '
table.position(numrows, tablewallgapX, numtables, tablesizeX, tablesizeY, dividerwallgapY, numdividers, dividerextrasizeY, tableoffsetX, dividergapX, tableoffsetY, divideroffsetY)
divider.position(numrows, numdividers, tablewallgapX, tablesizeX, dividergapX, dividergapY, dividersizeX, dividerwallgapY, divideroffsetY, tabledividergapX, dividersizeY)
platedelivery.position(roomsizeX, platedeliveryx, platedeliveryy, borderX, borderY)

'Criação do ecrã'
win = gr.GraphWin('Planta da Sala', windowsizeX, windowsizeY)

'Adaptação do sala para o ecrã'
win.setCoords(0, windowsizeY/scale, windowsizeX/scale, 0)

'Para calculos porteriores as salas terão os valores vistos no ecrã'
roomsizeX = windowsizeX/scale
roomsizeY = windowsizeY/scale
            
'Construção dos objetos no ecrã'
table.drawGroup(win)
divider.drawGroup(win)
platedelivery.draw(win)


'Botão de saida'
quitbutton = qb.QuitButton(win, gr.Point(1, 1), gr.Point(12, 9), 'Quit')
'Dropdown do trbalho'
dropdown = dd.DropDown(win, gr.Point(17, 1), gr.Point(40, 9), 'Dropdown')
'Classe do robô'
waiter = wa.Waiter(win, gr.Point((roomsizeX + platedeliveryx)/2 + 6, platedeliveryy/2), 4, table.grouptables, divider.groupdividers)

'Sistema de opção escolha das possiveis ações do programa'
close = False
'Enquanto o valor da variavel close fôr Falso o programa se manterá aberto'
while close is False:
    'Como o programa está aberto o Botão de saida e o Dropdown estão ligados'
    quitbutton.active()
    dropdown.active()
    'Espera da ação do utilizador para criar a ação reciproca'
    mouseclick = win.getMouse()
    'Se o Dropdown for pressionado será mostrado no ecrã'
    dropdown.pressed(mouseclick, win, roomsizeX, roomsizeY)
    'Se o botão pressionado pelo o utilizador for o Botão de Saida o valor da variavel close torna se verdadeiro e o programa vai se desligar'
    if quitbutton.pressed(mouseclick) is True:
        close = True
        'Caso n ocorra a pressão do Botão de saida e do Dropdown estes n vão ser ativados e será processado pelo waiter para ver se o local que o utilizador clicou é uma mesa'
    else:
        quitbutton.unactive()
        dropdown.unactive()
        waiter.move(tablewallgapX, tablesizeX, tabledividergapX, dividerwallgapY, dividergapX, dividergapY, dividersizeX, dividersizeY, platedeliveryy, numrows, numdividers, roomsizeX, mouseclick)
'Com a saida do loop o botão de saida foi pressionado por isso a janela vai ser fechada' 
win.close()