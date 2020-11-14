from tkinter import *
from threading import Thread
import threading
import os
import time
from tkinter import messagebox
import math
from random import randrange as ale
from pygame import mixer

###Para las imagenes
global user
usl=os.environ['USERPROFILE']
user=usl[:2]+'/Users/'+usl[+9:]


def LoadImg(imgName):
    global user
    route=os.path.join(user+'/Desktop/proyecto_taller_1/Images', imgName)
    imagen=PhotoImage(file=route)
    return imagen


#Pantalla principal
root=Tk()
root.title('Tower Defense')
root.minsize(1000, 600)
root.resizable(width=NO, height=NO)

#Canvas
C_root=Canvas(root, width=1020, height=620, bg='black')
C_root.place(x=-10, y=-10)

#Registro del nombre
Name=Entry(C_root, width=15, font=('Arial', 14))
Name.place(x=410, y=300)

mixer.init()
mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
mixer.music.play(loops=-1)


def INICIO():
    global coins
    coins='0000'
    mixer.music.unload()
    root.withdraw()
    g_root=Toplevel()
    g_root.title('Tower Defense')
    g_root.minsize(1200, 773)
    g_root.resizable(width=NO, height=NO)

    G_root=Canvas(g_root, width=1520, height=800, bg='green')
    G_root.place(x=-10, y=-10)

    GBG=LoadImg('tablero.png')
    G_root.fondo=GBG
    G_root.create_image(10, 7, anchor=NW, image=GBG)

    name=str(Name.get())
    playerName=Label(G_root, text="Jugador: "+name, font=('Arial', 14))
    playerName.place(x=70, y=40)



    def Error():
        print("Error:el nombre debe tener 8 caracteres, en caso de no cumplir la extension, agregar - para completar de la forma Gabo----")
        mixer.music.stop()
        mixer.music.unload()
        g_root.destroy()
        root.deiconify()
        mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
        mixer.music.play(loops=-1)

    if len(name)!=8:
        return Error()


    mixer.music.load(user+'/Desktop/proyecto_taller_1/music/kokuten.mp3')
    mixer.music.play(loops=-1)
    

    f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'r')
    lines=f.readlines()
    f.close()


###asignar un bbox a cada cuadro de la matriz
###Fila 1
    G_root.create_rectangle(102, 156, 196, 246, outline="", tags="f1c1")
    G_root.create_rectangle(197, 156, 291, 246, outline="", tags="f1c2")
    G_root.create_rectangle(292, 156, 385, 246, outline="", tags="f1c3")
    G_root.create_rectangle(386, 156, 475, 246, outline="", tags="f1c4")
    G_root.create_rectangle(476, 156, 568, 246, outline="", tags="f1c5")
    G_root.create_rectangle(569, 156, 663, 246, outline="", tags="f1c6")
    G_root.create_rectangle(664, 156, 757, 246, outline="", tags="f1c7")
    G_root.create_rectangle(758, 156, 850, 246, outline="", tags="f1c8")
    G_root.create_rectangle(851, 156, 942, 246, outline="", tags="f1c9")
####Fila 2
    G_root.create_rectangle(102, 246, 196, 336, outline="", tags="f2c1")
    G_root.create_rectangle(197, 246, 291, 336, outline="", tags="f2c2")
    G_root.create_rectangle(292, 246, 385, 336, outline="", tags="f2c3")
    G_root.create_rectangle(386, 246, 475, 336, outline="", tags="f2c4")
    G_root.create_rectangle(476, 246, 568, 336, outline="", tags="f2c5")
    G_root.create_rectangle(569, 246, 663, 336, outline="", tags="f2c6")
    G_root.create_rectangle(664, 246, 757, 336, outline="", tags="f2c7")
    G_root.create_rectangle(758, 246, 850, 336, outline="", tags="f2c8")
    G_root.create_rectangle(851, 246, 942, 336, outline="", tags="f2c9")
####Fila 3
    G_root.create_rectangle(102, 337, 196, 431, outline="", tags="f3c1")
    G_root.create_rectangle(197, 337, 291, 431, outline="", tags="f3c2")
    G_root.create_rectangle(292, 337, 385, 431, outline="", tags="f3c3")
    G_root.create_rectangle(386, 337, 475, 431, outline="", tags="f3c4")
    G_root.create_rectangle(476, 337, 568, 431, outline="", tags="f3c5")
    G_root.create_rectangle(569, 337, 663, 431, outline="", tags="f3c6")
    G_root.create_rectangle(664, 337, 757, 431, outline="", tags="f3c7")
    G_root.create_rectangle(758, 337, 850, 431, outline="", tags="f3c8")
    G_root.create_rectangle(851, 337, 942, 431, outline="", tags="f3c9")

####Fila 4
    G_root.create_rectangle(102, 432, 196, 523, outline="", tags="f4c1")
    G_root.create_rectangle(197, 432, 291, 523, outline="", tags="f4c2")
    G_root.create_rectangle(292, 432, 385, 523, outline="", tags="f4c3")
    G_root.create_rectangle(386, 432, 475, 523, outline="", tags="f4c4")
    G_root.create_rectangle(476, 432, 568, 523, outline="", tags="f4c5")
    G_root.create_rectangle(569, 432, 663, 523, outline="", tags="f4c6")
    G_root.create_rectangle(664, 432, 757, 523, outline="", tags="f4c7")
    G_root.create_rectangle(758, 432, 850, 523, outline="", tags="f4c8")
    G_root.create_rectangle(851, 432, 942, 523, outline="", tags="f4c9")

####Fila 5
    G_root.create_rectangle(102, 524, 196, 616, outline="", tags="f5c1")
    G_root.create_rectangle(197, 524, 291, 616, outline="", tags="f5c2")
    G_root.create_rectangle(292, 524, 385, 616, outline="", tags="f5c3")
    G_root.create_rectangle(386, 524, 475, 616, outline="", tags="f5c4")
    G_root.create_rectangle(476, 524, 568, 616, outline="", tags="f5c5")
    G_root.create_rectangle(569, 524, 663, 616, outline="", tags="f5c6")
    G_root.create_rectangle(664, 524, 757, 616, outline="", tags="f5c7")
    G_root.create_rectangle(758, 524, 850, 616, outline="", tags="f5c8")
    G_root.create_rectangle(851, 524, 942, 616, outline="", tags="f5c9")
####Fila 6
    G_root.create_rectangle(102, 617, 196, 707, outline="", tags="f6c1")
    G_root.create_rectangle(197, 617, 291, 707, outline="", tags="f6c2")
    G_root.create_rectangle(292, 617, 385, 707, outline="", tags="f6c3")
    G_root.create_rectangle(386, 617, 475, 707, outline="", tags="f6c4")
    G_root.create_rectangle(476, 617, 568, 707, outline="", tags="f6c5")
    G_root.create_rectangle(569, 617, 663, 707, outline="", tags="f6c6")
    G_root.create_rectangle(664, 617, 757, 707, outline="", tags="f6c7")
    G_root.create_rectangle(758, 617, 850, 707, outline="", tags="f6c8")
    G_root.create_rectangle(851, 617, 942, 707, outline="", tags="f6c9")



    
    if lines[0][0]=="0":
        print('0')
        #posteriormente ingresar codigo para, el 0 indica que no hay partida guardada
    elif lines[0][0]=="1":
        print('1')
        #1 indica que hay partida guardad, por lo que se procedera a leer el nombre para registrarlo y se leera la cantidad de monedas y el nivel en el que se encunetra el jugador
        

    
    




















    
              


        
    def Return():
        global user
        global coins
        mixer.music.stop()
        mixer.music.unload()
        name=str(Name.get())
        money=coins
        f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w')
        f.write('10'+name+money)
        f.close
        g_root.destroy()
        root.deiconify()
        mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
        mixer.music.play(loops=-1)

###Botones del juego
    returN=Button(G_root, command=Return, bg='yellow', fg='black', text='Back')
    returN.place(x=25, y=40)
    








#Comando para salirse de la pantalla
def Exit():
    mixer.music.stop()
    mixer.music.unload()
    root.destroy()
    


def reset():
    f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w')
    f.write('00')
    f.close
    
#Button
rests=LoadImg('restart.png')
C_root.botn=rests

RESET=Button(C_root, command=reset, image=rests)
RESET.place(x=850, y=500)


EXIT=Button(C_root, command=Exit, bg='white', fg='black', text='Exit')
EXIT.place(x=30, y=20)

START=Button(C_root, command=INICIO, bg='red', fg='black', text='Start')
START.place(x=600, y=280)








root.mainloop()
