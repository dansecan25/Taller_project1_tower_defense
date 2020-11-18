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
    coins=9999
    global price
    price=0
    global item
    item=''
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
    G_root.create_image(10, 7, anchor=NW, image=GBG, tags='fondo')

    name=str(Name.get())
    playerName=Label(G_root, text="Jugador: "+name, font=('Arial', 14))
    playerName.place(x=70, y=40)

###Rooks a seleccionar
    sand=LoadImg('sand_rook.png')
    G_root.snd=sand
    RookS=G_root.create_image(1020, 50, anchor=NW, image=sand, tags='ROOKS')
    G_root.create_text(1060, 163,  font=('Arial', 8), fill='black', text='Sand Rook=$50',)

    rock=LoadImg('rock_rook.png')
    G_root.rck=rock
    RookR=G_root.create_image(1120, 60, anchor=NW, image=rock, tags='ROOKR')
    G_root.create_text(1150, 163,  font=('Arial', 8), fill='black', text='Rock Rook=$100',)

    fire=LoadImg('fire_rook.png')
    G_root.fre=fire
    RookF=G_root.create_image(1020, 180, anchor=NW, image=fire, tags='ROOKF')
    G_root.create_text(1060, 290,  font=('Arial', 8), fill='black', text='Fire Rook=$150',)

    water=LoadImg('water_rook.png')
    G_root.wtr=water
    RookW=G_root.create_image(1120, 180, anchor=NW, image=water, tags='ROOKW')
    G_root.create_text(1150, 290,  font=('Arial', 8), fill='black', text='Water Rook=$150',)

    

    



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



    def select(event):
        global price
        global item
        x=event.x
        y=event.y
        print(str(y))
        print(str(x))
        print('Item inicial '+item)
        print('inicial price '+str(price))
        if x>1000:
            if x>=1020 and x<=1110:
                if y>=50 and y<=160:
                    S_BBOX=G_root.bbox('ROOKS')
                    G_root.create_rectangle(S_BBOX[0],S_BBOX[1],S_BBOX[2],S_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(S_BBOX)
                    price=50
                    item='sand_rook.png'
                    print('cAPTURE SUCCES')

                elif y>=180 and y<=275:
                    F_BBOX=G_root.bbox('ROOKF')
                    G_root.create_rectangle(F_BBOX[0],F_BBOX[1],F_BBOX[2],F_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(F_BBOX)
                    price=150
                    item='fire_rook.png'
                    print(item)
                    print(str(price))
                    print('cAPTURE SUCCES')
                    
            elif event.x>=1120 and event.x<=1300:
                if event.y>=50 and event.y<=160:
                    R_BBOX=G_root.bbox('ROOKR')
                    G_root.create_rectangle(R_BBOX[0],R_BBOX[1],R_BBOX[2],R_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(R_BBOX)
                    price=100
                    item='rock_rook.png'
                    print(item)
                    print(str(price))
                    print('cAPTURE SUCCES')

                elif event.y>=180 and event.y<=275:
                    W_BBOX=G_root.bbox('ROOKW')
                    G_root.create_rectangle(W_BBOX[0],W_BBOX[1],W_BBOX[2],W_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(W_BBOX)
                    price=150
                    item='water_rook.png'
                    print(item)
                    print(str(price))
                    print('cAPTURE SUCCES')
        elif x<1000:
            if price!=0 and item!='':
                place(x, y)
            else:
                print('No item selected')


        l=G_root.find_overlapping(event.x, event.y, event.x+60, event.y+60)
        p=G_root.find_all()



    def place(x,y):
        global coins
        global price
        global item
        l=G_root.find_overlapping(x, y, x+60, y+60)
        money=coins
        if money>=price:
            if x>=102 and x<=196:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=102
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                    

            elif x>=197 and x<=291:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=198
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


            elif x>=292 and x<=385:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=293
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


            elif x>=386 and x<=475:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=387
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


            elif x>=476 and x<=568:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=477
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

            elif x>=569 and x<=663:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=570
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

            elif x>=664 and x<=757:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=665
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


            elif x>=758 and x<=850:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=759
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

            elif x>=851 and x<=1000:
                if y>=156 and y<=246:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=156
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0
                    

                elif y>=247 and y<=336:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=247
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=337 and y<=431:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=337
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0


                elif y>=432 and y<=523:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=432
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=524 and y<=616:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=524
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

                elif y>=617 and y<=707:
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=852
                    pos_y=617
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') 
                    G_root.delete('rect')
                    tower_thread(pos_x, pos_y, tw)
                    item=''
                    price=0

            else:
                print('cant place')
                item=''
                price=0
                G_root.delete('rect')
        else:
            print('no placing')
            item=''
            price=0
            G_root.delete('rect')
            


    def tower_thread(x,y, objt):
        print('yes')





                
        #if money>value:


    
    if lines[0][0]=="0":
        print('0')
       
    elif lines[0][0]=="1":
        print('1')
        #1 indica que hay partida guardad, por lo que se procedera a leer el nombre para registrarlo y se leera la cantidad de monedas y el nivel en el que se encunetra el jugador


###Bindings
    g_root.bind("<Button-1>", select)
    
    
    




















    
              


        
    def Return():
        global user
        global coins
        mixer.music.stop()
        mixer.music.unload()
        name=str(Name.get())
        money=str(coins)
        if len(money)==3:
            money='0'+money
        elif len(money)==2:
            money='00'+money
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
