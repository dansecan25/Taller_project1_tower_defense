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
root.minsize(1000, 651)
root.resizable(width=NO, height=NO)

#Canvas
C_root=Canvas(root, width=1020, height=700, bg='black')
C_root.place(x=-10, y=-10)

#Registro del nombre
Name=Entry(C_root, width=15, font=('Arial', 14))
Name.place(x=420, y=430)

bACKg=LoadImg('backG.png')
C_root.bgggg=bACKg
C_root.create_image(10,9,anchor=NW,image=bACKg)

def anima(obj,i):
    if i!=20:
        C_root.move(obj,0,10)
        C_root.after(150,anima,obj,i+1)
        

title=LoadImg('title.png')
C_root.titirl=title
l=C_root.create_image(350,0,anchor=NW,image=title)
anima(l,0)



mixer.init()
mixer.music.set_volume(0.2)
mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
mixer.music.play(loops=-1)


def INICIO():
    global rectann_flag
    rectann_flag=False
    global coins
    coins=9999
    global price
    price=0
    global item
    item=''
    global maTRooks
    maTRooks=[]
    global maTava
    mixer.music.unload()
    root.withdraw()
    g_root=Toplevel()
    g_root.title('Tower Defense')
    g_root.minsize(1200, 773) #773
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
        mixer.music.set_volume(0.2)
        mixer.music.stop()
        mixer.music.unload()
        g_root.destroy()
        root.deiconify()
        mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
        mixer.music.play(loops=-1)

    if len(name)!=8:
        return Error()

    mixer.music.set_volume(0.1)
    mixer.music.load(user+'/Desktop/proyecto_taller_1/music/kokuten.mp3')
    mixer.music.play(loops=-1)
    

    f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'r')
    lines=f.readlines()
    f.close()


        
        
        
        
    



###Selecting and placing rooks
    
    def select(event): #funcion para seleccionar el rook
        global price 
        global item
        global rectann_flag
        if rectann_flag==True:
            G_root.delete('rect')
            rectann_flag=False
        x=event.x
        y=event.y
        if x>1000:
            if x>=1020 and x<=1110:
                if y>=50 and y<=160:
                    S_BBOX=G_root.bbox('ROOKS')  #crea una bbox para posteriormente obetener las coordenadas alrededor del rook seleccionado
                    G_root.create_rectangle(S_BBOX[0],S_BBOX[1],S_BBOX[2],S_BBOX[3], outline='red', width=3, tags='rect') #crea el rectangulo alrededor del rook seleccionado
                    G_root.delete(S_BBOX) #elimina la caja invisble para evitar problemas
                    price=50 #setea el precio del rook elegido
                    item='sand_rook.png'
                    hp=12
                    rectann_flag=True #para senialar que ya hay un rook seleccionado
   

                elif y>=180 and y<=275:
                    F_BBOX=G_root.bbox('ROOKF')
                    G_root.create_rectangle(F_BBOX[0],F_BBOX[1],F_BBOX[2],F_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(F_BBOX)
                    price=150
                    item='fire_rook.png'
                    hp=16
                    rectann_flag=True

                    
            elif event.x>=1120 and event.x<=1300:
                if event.y>=50 and event.y<=160:
                    R_BBOX=G_root.bbox('ROOKR')
                    G_root.create_rectangle(R_BBOX[0],R_BBOX[1],R_BBOX[2],R_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(R_BBOX)
                    price=100
                    item='rock_rook.png'
                    hp=14
                    rectann_flag=True


                elif event.y>=180 and event.y<=275:
                    W_BBOX=G_root.bbox('ROOKW')
                    G_root.create_rectangle(W_BBOX[0],W_BBOX[1],W_BBOX[2],W_BBOX[3], outline='red', width=3, tags='rect')
                    G_root.delete(W_BBOX)
                    price=150
                    item='water_rook.png'
                    hp=16
                    rectann_flag=True

        elif x<1000:
            if price!=0 and item!='':
                pLace=Thread(target=place, args=(x, y,0,0,0,0,maTrizX,maTrizY)) #crea un thread para poner el rook
                pLace.start()  #lo inicia.
            else:
                print('No item selected')
    global maTrizX
    maTrizX=[[102, 196],[197, 291],[292,385],[386,475],[476,568],[569,663],[664, 757],[758,850],[851,1000]] #coordenadas en x
    maTrizY=[[156,246],[247,336],[337, 431],[432, 523],[524,616],[617,707]]  #coordenadas en y
    
    def place(x,y,iX,jX,iY,jY, MatX,MatY):  #posicionara el rook seleccionado en una coordenada especifica
        global coins
        global maTRooks
        global price
        global item
        global rectann_flag
        a='sand_rook.png'
        b='rock_rook.png'
        c='fire_rook.png'
        d='water_rook.png'
        
            
        l=G_root.find_overlapping(x, y, x+60, y+60)  #obtiene los objetos que estan dentro del cuadrado especificado
        money=coins  #variable por que antes coins era un string pero en realidad no se ocupa pero me dio pereza quitarlo
        if money>=price:  #comprueba si hay suficiente dinero para poner el rook
            if jX==len(MatX) or jY==len(MatY): #condicion de finalizacion en caso de que no se haya seleccionado dentro del tablero
                print('cant place')
                item='' #reinicia el item
                price=0 #reinicia el precio
                G_root.delete('rect')
                rectann_flag=False
                #hacer una lista que guarde el rook y las coordenadas
                
            if x>=MatX[jX][iX] and x<=MatX[jX][iX+1]:  #Compara cada coordenada de X
                if y>=MatY[jY][iY] and y<=MatY[jY][iY+1]: #Compara cada coordenada Y
                    if item==a:
                        hp=12

                    elif item==b:
                        hp=14

                    elif item==c:
                        hp=16

                    elif item==d:
                        hp=16
                    
                    coins-=price
                    it=LoadImg(item)
                    G_root.its=it
                    pos_x=MatX[jX][iX] #setea una variable pos_x para para usarla como el valor en x para posteriormente crearlo en y
                    pos_y=MatY[jY][iY] #lo mismo pero con y
                    tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower') #crea el rook
                    G_root.delete('rect') #borra el outline del rook seleccionado
                    tower=[item,pos_x,pos_y,hp]
                    maTRooks.append(tower)
                    tower_thread(pos_x, pos_y, item,hp) #llama a la funcion que deberia iniciar el proceso de crear los threads para crear los misiles
                    item=''
                    price=0
                    rectann_flag=False
                    #print('Towers= ',maTRooks)
                    Givein(tw)
                    #G_root.update()
                    
                    
                else:
                    place(x,y,iX,jX,0,jY+1,MatX, MatY) #se mueve al siguiente par de coordenadas en Y
            else:
                place(x,y,0,jX+1,iY,jY,MatX, MatY) #se mueve al siguiente par de coordenadas X
        else:
            print('insufficient money')
            G_root.delete('rect')
            rectann_flag=False

    def Givein(obj):
        G_root.move(obj,1,0)
        time.sleep(0.5)
        G_root.move(obj,-1,0)
        time.sleep(6)
        Givein(obj)
    """   
    def place_before(mat, i, j,m):
        if j==m:
            print('placed all')

        elif j<m:
            print('matlll: ',mat[j][i])
            pos_x=mat[j][i+2] 
            pos_y=mat[j][i+3]
            hp=mat[j][i+4]
            item=mat[j][i+1]
            tower_thread(pos_x, pos_y, item,hp)
            return place_before(mat,0,j+1,m)
    """
    def comp(ov,en,i,p,n,d):
        if p==d:
            return False
        elif i==n:
            return comp(ov,en,0,p+1,n,d)
        elif en[i]==ov[p]:
            return True
        else:
            return comp(ov,en,i+1,p,n,d)

    def objects(ov,en,i,p,n,d,res):
        if p==d:
            return res
        if i==n:
            return objects(ov,en,0,p+1,n,d,res)
        elif en[i]==ov[p]:
            return objects(ov,en,i+1,d,n,d,res+en[i])
        else:
            return objects(ov,en,i+1,p,n,d,res)
     
                        
    def move_misil(misil,hp,dmg):
        en_coords=G_root.coords(misil)
        x=en_coords[0]
        y=en_coords[1]
        overlap=G_root.find_overlapping(x, y, x+30,y+30)
        overlap=list(overlap)
        enemys=G_root.find_withtag('enemy')
        enemys=list(enemys)
        misiles=G_root.find_withtag('misil')
        misiles=list(misiles)
        if y<=775:
            if len(overlap)>=3:
                print('overlap= ',overlap)
                print('enemys= ',enemys)
                if comp(overlap,enemys,0,0,len(enemys),len(overlap))==True:
                    objecT=objects(overlap,enemys,0,0,len(enemys),len(overlap),0)
                    print(objecT)
                    print(misil)
                    G_root.delete(objecT)
                    G_root.delete(misil)
            else:
                G_root.move(misil, 0, 10)
                time.sleep(0.7)
                move_misil(misil,hp,dmg)
                
            
            G_root.move(misil, 0, 10)
            time.sleep(0.7)
            move_misil(misil,hp,dmg)
        
    def verify(x,MY):
        if len(G_root.find_overlapping(x,MY[0],x+20,MY[1]))>=2:
            print('verify= ',G_root.find_overlapping(x,MY[0],x+20,MY[1]))
            return True
        else:
            return False
    
    def shooting(objt,x,y,hp): #objt es el rook colocado, x es la equina superior izquierda y y la parte de arriba del cuadrito dentro del tablero
        global maTrizX
        maTborderY=[617,773]
        a='sand_rook.png'
        b='rock_rook.png'
        c='fire_rook.png'
        d='water_rook.png'
        overlap=G_root.find_overlapping(x, y, x+50, y+600)

        if verify(x,maTborderY)==True:
            if objt==a:  #comprueba si el elemento elegido es igual a tal objeto para entonces crear el misil que le corresponde

                misl=LoadImg('sand.png')
                G_root.sndaa=misl
                mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                move_misil(mis,hp,2)
                time.sleep(5)
                shooting(objt,x,y,hp)
                
            elif objt==b:

                misl=LoadImg('rock.png')
                G_root.rocvok=misl
                mis=G_root.create_image(x+25, y+30, anchor=NW,image=misl, tags='misil')
                move_misil(mis,hp,4)
                time.sleep(5)
                shooting(objt,x,y,hp)
            elif objt==c:

                misl=LoadImg('fire.png')
                G_root.fiah=misl
                mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                move_misil(mis,hp,8)
                time.sleep(5)
                shooting(objt,x,y,hp)
                
            elif objt==d:

                misl=LoadImg('water.png')
                G_root.wteer=misl
                mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                move_misil(mis,hp,8)
                time.sleep(5)
                shooting(objt,x,y,hp)
        else:
            time.sleep(3)
            shooting(objt,x,y,hp)


        

    def tower_thread(x,y, objt,hp):
        crte=Thread(target=shooting, args=(objt,x, y,hp))
        crte.start()


#funciones para extraer datos
    def extract(lines):
        print('0')
        

    lines=str(lines)
    print('lines as string= ',lines)
    lines=list(lines)
    print(lines[0][0])
    print(lines)
    if lines[0]==00:
        print('0')
       
    elif lines[0]==10 and str(lines[1])==name:
        print('1')
        print('lines= ',str(lines))

    
        #1 indica que hay partida guardad, por lo que se procedera a leer el nombre para registrarlo y se leera la cantidad de monedas y el nivel en el que se encunetra el jugador


    #Enamy creation
    def enemy():
        muu=Thread(target=crte, args=())
        muu.start()
        
        G_root.after(20000,enemy)
    def crte():
        import random
        from random import randrange
        rand=random.randrange(94,760,95)
        ren=random.randrange(1,5,1)
        if ren==1:
            arq=LoadImg('arquero.png')
            G_root.enemigo=arq
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=arq, tags='enemy')
            movementEnemy(Enemy, 12, 5)

        elif ren==2:
            can=LoadImg('canibal.png')
            G_root.enemigo=can
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=can, tags='enemy')
            movementCanibal(Enemy, 14, 25)

        elif ren==3:
            esq=LoadImg('escudero.png')
            G_root.enemigo=esq
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=esq, tags='enemy')
            movementEnemy(Enemy, 10, 10)


        elif ren==4:
            lena=LoadImg('lenador.png')
            G_root.enemigo=lena
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=lena, tags='enemy')
            movementEnemy(Enemy, 13, 20)

    def movementEnemy(en,t, hp):
        
        G_root.move(en, 0, -20)
        time.sleep(t)
        movementEnemy(en, t, hp)

    def movementCanibal(en,t,hp):
        en_coords=G_root.coords(en)
        x=en_coords[0]
        y=en_coords[1]
        print(x,y)
        ov=G_root.find_overlapping(x+20,y-20,x,y)
        if len(ov)>1:
            hit=LoadImg('canibal_hit.png')
            G_root.huisi=hit
            hitt=G_root.create_image(x,y,anchor=NW,image=hit,tags='hittingC')
            time.sleep(0.2)
            G_root.delete('hittingC')
            can=LoadImg('canibal.png')
            G_root.enemigo=can
            en=G_root.create_image(x, y, anchor=NW, image=can, tags='enemy')
            movementCanibal(en,t,hp)
            
        G_root.move(en, 0, -20)
        time.sleep(t)
        movementEnemy(en, t, hp)

    enemy()

###Bindings
    g_root.bind("<Button-1>", select)
    
    
    



















    def stringear(M,i,j,m,n,res):
        if j==m:
            return res
        elif i==n:
            return stringear(M,0,j+1,m,n,res)
        else:
            return stringear(M,i+1,j,m,n,res+','+str(M[j][i]))
        
    
              


        
    def Return():
        global user
        global coins
        global maTRooks
        rooks=stringear(maTRooks,0,0,len(maTRooks),len(maTRooks),"")
        print('rooks= ',rooks)
        mixer.music.set_volume(0.2)
        mixer.music.stop()
        mixer.music.unload()
        name=str(Name.get())
        money=str(coins)
        if len(money)==3:
            money='0'+money
        elif len(money)==2:
            money='00'+money
        f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w')
        f.write('10'+','+name+','+money+rooks+',')
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
RESET.place(x=850, y=570)


EXIT=Button(C_root, command=Exit, bg='white', fg='black', text='Exit')
EXIT.place(x=30, y=20)


starto=LoadImg('START.png')
START=Button(C_root,image=starto, command=INICIO)
START.place(x=385, y=490)








root.mainloop()
