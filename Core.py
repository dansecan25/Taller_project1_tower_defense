from tkinter import *
from threading import Thread
import threading
import os
import time
from tkinter import messagebox
import math
from random import randrange as ale

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



def INICIO():
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

    f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'r')
    lines=f.readlines()
    f.close()
    if lines[0]=="0":
        #posteriormente ingresar codigo para, el 0 indica que no hay partida guardada
    elif lines[0]=="1":
        #1 indica que hay partida guardad, por lo que se procedera a leer el nombre para registrarlo y se leera la cantidad de monedas y el nivel en el que se encunetra el jugador
        

    
    






















    def Return():
        g_root.destroy()
        root.deiconify()

###Botones del juego
    returN=Button(G_root, command=Return, bg='yellow', fg='black', text='Back')
    returN.place(x=25, y=40)
    








#Comando para salirse de la pantalla
def Exit():
    root.destroy()
    



#Button
EXIT=Button(C_root, command=Exit, bg='white', fg='black', text='Exit')
EXIT.place(x=30, y=20)

START=Button(C_root, command=INICIO, bg='red', fg='black', text='Start')
START.place(x=510, y=280)








root.mainloop()
