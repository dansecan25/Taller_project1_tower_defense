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
global oll
oll=False

def off():
    global oll
    if oll==False:
        mixer.music.pause()
        oll=True

def on():
    global oll
    if oll==True:
        oll=False
        mixer.music.unpause()

def anima_win():
    W_root=Toplevel() 
    g_root.title('GANASTE') 
    g_root.minsize(200, 200)
    g_root.resizable(width=NO, height=NO)

    w_root=Canvas(W_root, width=200, height=200, bg='light green')
    w_root.place(x=0, y=0)

    w_root.create_text(100,100,font=('Arial', 12), fill='black',text='FELICIDADES! HA GANADO!')
    time.sleep(3)
    g_root.destroy()
    






def anima_loose():
    L_root=Toplevel() 
    L_root.title('DERROTA') 
    L_root.minsize(200, 200)
    L_root.resizable(width=NO, height=NO)

    l_root=Canvas(L_root, width=200, height=200, bg='black')
    l_root.place(x=0, y=0)

    l_root.create_text(100,100,font=('Arial', 12), fill='white',text='Lo sentimos, DERROTADO')
    time.sleep(3)
    L_root.destroy()
    

def v_puntajes():
    global namae
    namae=[]
    global ordenados
    ordenados=[]
    P_root=Toplevel() 
    P_root.title('Puntajes') 
    P_root.minsize(650, 500)
    P_root.resizable(width=NO, height=NO)

    p_root=Canvas(P_root, width=650, height=500, bg='light blue')
    p_root.place(x=0, y=0)

    p=open(user+'/Desktop/proyecto_taller_1/puntajes.txt','r') #abre la lista de puntajes para leerla
    lineas=p.readlines() #guarda el contenido de los puntajes
    p.close()


    def etadpu(M,res):
        return restyo(M,[],0,len(M),res)

    def restyo(N,new,i,n,res):
        return etadpu_aux(N,[],0,len(N),res)

    def etadpu_aux(N,new,i,n,res):
        global namae
        if i==n:

            return 0
        elif N[i][3]==res[3] and N[i][0]==res[0] and N[i][1] == res[1] and N[i][2]==res[2]: #si el nombre es igual al del resultado, y los minutos, horas y segundos concuerdan

            global ordenados
            ordenados.append(N[i]) #se le agrega
            return etadpu_aux(N,new,i+1,n,res)
        
        elif N[i][3]!=res[3] or( N[i][0]!=res[0] and N[i][1] != res[1] and N[i][2]!=res[2]):

            lista=N[i]
            namae.append(lista)

            return etadpu_aux(N,new,i+1,n,res)
            
            
    def prep(M,i,m,res):
        global namae
        return comparsaH(namae,i,len(namae),res)


    def comparsaS(M,i,n,res):
        global namae
        global ordenados
        if len(M)==1:
            ordenados.append(M[0])
            print('Final= ', ordenados)

        elif i==n: #si el contador es igual a n
            namae=[]
            etadpu(M,res)
            return prep(M,0,len(M),[0,0])
        elif M[i][2]>=res[2] and M[i][0]>=res[0] and M[i][1]<res[1]:
            return comparsaS(M,i+1,n,res)

        elif (M[i][2]<res[2] and M[i][0]<res[0] and M[i][1]<res[1] )or(M[i][2]<res[2] and M[i][0]<res[0] and M[i][1]>=res[1]):
            return comparsaS(M,i+1,n,M[i])
        else:
            return comparsaS(M,i+1,n,res)
            

    def comparsaM(M,i,n,res): #M es [hora,minutos, segundos,nombre]
        if M==[]:
            return comparsaS(M,0,n,[0,0,0])
        if i==n:
            comparsaS(M,0,n,res)
        elif M[i][1]>=res[1] and M[i][0]>=res[0]: #si los minutos son mayores al los minutos resultantes pero las horas son iguales o mayores
            return comparsaM(M,i+1,n,res) #no se guarda
        elif M[i][1]<res[1] and M[i][0]<=res[0]: #si es menor los minutos en la matriz y las horas son menores o iguales al resultado
            return comparsaM(M,i+1,n,M[i]) #se guarda
        else:
            return comparsaM(M,i+1,n,res) #de otra forma, se ignora
    
    def comparsaH(M,i,n,res):
        if M==[]:
            return comparsaM(M,0,n,res)
        elif i==n: #si el indice es igual a la longitud de la matriz, finaliza
            comparsaM(M,0,n,res)
        elif M[i][0]==0: #si es 0 las horas, no hay otro menor por lo cual se coloca la lista i en el resultado
            return comparsaH(M,n,n,M[i]) 
        elif M[i][0]>=res[0]: #si las horas son mayores a las guardadas no sirve
            return comparsaH(M,i+1,n,res)
        elif M[i][0]<res[0]: #si las horas son menores que el resultado entonces se guarda
            return comparsaH(M,i+1,n,M[i]) #se actualiza el resultado

        
    def pre_comparsaH(M,i,n,res): #guarda la matriz y el resultado
        return comparsaH(M,i,len(M),[0,0]) #despues de resetear la matriz se manda a evaluar
            
    
    def extraer(L,i,n):
        global namae
        if L[i]=='': #si en 0 el ultimo elemento es '', por lo tanto se llegó al final de la lista
            
            return pre_comparsaH(namae,0,len(namae),[0,0]) #se envía la matriz con un contador i y su n con un resultado 0
        else:
            
            nombre=L[i]  #el elemento 0 es el nombre del jugador
            hora=int(L[i+1])  # el 1 es la hora
            minu=int(L[i+2])  #el 2 es el minuto
            sec=int(L[i+3])    #el 3 es los segundos
            lista=[hora,minu,sec,nombre] #se crea una lista con estos elementos
            namae.append(lista) #se agrega la lista a una lista que contiene listas de cada uno de los puntajes
            return extraer(L[4:],i,n) #se repite eliminando los primeros 4 elementos de la lista
            
        
        

    def veo(lineas):
        return veo_aux(lineas,0,len(lineas))
    
    def veo_aux(L,i,n):
        if i==n:
            return 0
        else:
            global lalala
            lalala=L[i].strip().split(',') #agarra la lista de cada lista del readlines y si hay comma, lo separa creando la lista

    veo(lineas)
    global lalala #[nombre,hora,minuto,segundo,]

    if len(lalala)>0:
        extraer(lalala,0, len(lalala))
        if len(ordenados)>0:
            p_root.create_text(300,100,font=('Arial',12),fill='black',text='Top Tiempos: ')
            if len(ordenados)==1:
                nombre1=ordenados[0][3]
                H1=ordenados[0][0]
                M1=ordenados[0][1]
                S1=ordenados[0][2]
                texto=nombre1+'='+str(H1)+':'+str(M1)+':'+str(S1)+'\n'

                p_root.create_text(300, 200, font=('Arial', 20), fill='black', text=texto)



            elif len(ordenados)==2:
                nombre1=ordenados[0][3]
                N2=ordenados[1][3]
                H1=ordenados[0][0]
                H2=ordenados[1][0]
                M1=ordenados[0][1]
                M2=ordenados[1][1]
                S1=ordenados[0][2]
                S2=ordenados[0][2]
                texto=nombre1+'='+str(H1)+';'+str(M1)+':'+str(S1)+'\n'+N2+'='+str(H2)+';'+str(M2)+':'+str(S2)+'\n'

                
                p_root.create_text(300, 200, font=('Arial', 20), fill='black', text=texto)



            elif len(ordenados)==3:
                nombre1=ordenados[0][3]
                N2=ordenados[1][3]
                N3=ordenados[2][3]
                H1=ordenados[0][0]
                H2=ordenados[1][0]
                H3=ordenados[2][0]
                M1=ordenados[0][1]
                M2=ordenados[1][1]
                M3=ordenados[2][1]
                S1=ordenados[0][2]
                S2=ordenados[0][2]
                S3=ordenados[0][2]



                texto=nombre1+'='+str(H1)+';'+str(M1)+':'+str(S1)+'\n'+N2+'='+str(H2)+':'+str(M2)+':'+str(S2)+'\n'+N3+'='+str(H3)+':'+str(M3)+':'+str(S3)+'\n'

                p_root.create_text(300, 200, font=('Arial', 20), fill='black', text=texto)
                





            elif len(ordenados)==4:
                nombre1=ordenados[0][3]
                N2=ordenados[1][3]
                N3=ordenados[2][3]
                N4=ordenados[3][3]
                H1=ordenados[0][0]
                H2=ordenados[1][0]
                H3=ordenados[2][0]
                H4=ordenados[3][0]
                M1=ordenados[0][1]
                M2=ordenados[1][1]
                M3=ordenados[2][1]
                M4=ordenados[3][1]
                S1=ordenados[0][2]
                S2=ordenados[0][2]
                S3=ordenados[0][2]
                S4=ordenados[0][2]

                texto=nombre1+'='+str(H1)+';'+str(M1)+':'+str(S1)+'\n'+N2+'='+str(H2)+':'+str(M2)+':'+str(S2)+'\n'+N3+'='+str(H3)+':'+str(M3)+':'+str(S3)+'\n'+N4+'='+str(H4)+':'+str(M4)+':'+str(S4)+'\n'

                p_root.create_text(300, 200, font=('Arial', 20), fill='black', text=texto)





            elif len(ordenados)>=5:
                nombre1=ordenados[0][3]
                N2=ordenados[1][3]
                N3=ordenados[2][3]
                N4=ordenados[3][3]
                N5=ordenados[4][3]
                
                H1=ordenados[0][0]
                H2=ordenados[1][0]
                H3=ordenados[2][0]
                H4=ordenados[3][0]
                H5=ordenados[4][0]
                
                M1=ordenados[0][1]
                M2=ordenados[1][1]
                M3=ordenados[2][1]
                M4=ordenados[3][1]
                M5=ordenados[4][1]
                
                S1=ordenados[0][2]
                S2=ordenados[0][2]
                S3=ordenados[0][2]
                S4=ordenados[0][2]
                S5=ordenados[0][2]

                texto=nombre1+'='+str(H1)+';'+str(M1)+':'+str(S1)+'\n'+N2+'='+str(H2)+':'+str(M2)+':'+str(S2)+'\n'+N3+'='+str(H3)+':'+str(M3)+':'+str(S3)+'\n'+N4+'='+str(H4)+':'+str(M4)+':'+str(S4)+'\n'+N5+'='+str(H5)+':'+str(M5)+':'+str(S5)+'\n'

                p_root.create_text(300, 200, font=('Arial', 20), fill='black', text=texto)

        
        print(ordenados)






    
def ventana_about():
    information= """
    ---------------------------------------------------
    Instituto Tecnologico de Costa Rica
    Ingenieria en Computadores
    Autor: Daniel Serrano Canas
    Profesor: Jeff Schmidt Peralta
    Pais:Costa Rica
    Version de python: 3.8.9
    Biblioteca:Tkinter, pygame, random, os, time, threading
    Entradas:Teclas w, a, s, d y el boton
    derecho del mouse
    Salidas:movimientos y disparos
    ---------------------------------------------------

    """
    root.withdraw()
    About=Toplevel()
    About.title('info')
    About.minsize(800,400)
    About.resizable(width=NO, height=NO)

###Info Canvas
    NA_root=Canvas(About,  width=800, height=400, bg='white')
    NA_root.place(x=0, y=0)

###About text
    about=Label(NA_root, text=information, font=('Arial',15),bg='white',fg='black', justify=LEFT)
    about.place(x=300, y=50)
    def back():
        About.destroy()
        root.deiconify()
###About Image
    autor=LoadImg("imagen_perfil2.png")
    NA_root.img=autor
    NA_root.create_image(50, 70, anchor=NW, image=autor)
###Info Back
    Back1=Button(NA_root, text="Back", command=back, fg='white', bg='blue')
    Back1.place(x=50, y=350)


    
def INICIO():
    global rectann_flag
    rectann_flag=False
    global coins
    coins=250
    global price
    price=0
    global item
    item=''
    global maTRooks #aqui van los rooks que se colocan en el tablero con el orden [id,rook,x,y]
    maTRooks=[]
    global lisPast #aqui van los rooks que se crearon en una partida pasada
    lisPast=[]
    global points
    points=0
    global name  #para usar el nombre del jugador en otras funciones
    name=str(Name.get())
    global maTrizX #matriz con las posiciones en x o inicio y fin de cada columna
    maTrizX=[[102, 196],[197, 291],[292,385],[386,475],[476,568],[569,663],[664, 757],[758,850],[851,1000]] #coordenadas en x
    global maTrizY
    maTrizY=[[156,246],[247,336],[337, 431],[432, 523],[524,616],[617,707]]  #coordenadas en y
    global VidsEn  #en esta matriz se guardan las vidas e id de los enemigos de la forma [id,vida]
    VidsEn=[]
    global lisVidas #lista de vidas de las torres [id,hp]
    lisVidas=[]
    global seconds
    global minute
    global hour
    seconds=0
    minute=0
    hour=0
    global enemigos #lista con los enemigos
    enemigos=[]
    global nuevos #matriz que tendra a los enemigos de la partida guardada
    nuevos=[]
    global pastEnList #lista para convertir a matriz de los enemigos pasados
    pastEnList=[]
    global stringEnes
    stringEnes=''
    global stringRooks
    stringRooks=''
    global monedins
    monedins=[]
    
    mixer.music.unload()
    root.withdraw() #esconde la ventana principal
    g_root=Toplevel() #crea la ventana de juego
    g_root.title('Tower Defense') 
    g_root.minsize(1200, 773) #773
    g_root.resizable(width=NO, height=NO)

    G_root=Canvas(g_root, width=1520, height=800, bg='green')
    G_root.place(x=-10, y=-10)

    GBG=LoadImg('tablero.png')
    G_root.fondo=GBG
    G_root.create_image(10, 7, anchor=NW, image=GBG, tags='fondo')
    
    
    playerName=Label(G_root, text="Jugador: "+name, font=('Arial', 14))
    playerName.place(x=70, y=40)

###Rooks a seleccionar
    #se crean los rooks para elegir ______________________________________________________________________
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

    
###funciones para cargar la musica y leer la partida guardada_________________

    mixer.music.set_volume(0.1)
    mixer.music.load(user+'/Desktop/proyecto_taller_1/music/kokuten.mp3')
    mixer.music.play(loops=-1)
    

    f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'r')
    lines=f.readlines()
    f.close()


    


    ##se crea el tablero de puntage_____________________________________________________________________________________________________________
    G_root.create_text(1100,380,font=('Arial', 12), fill='black', text='Points:')  #crea el texto que va mostrar los puntos
    G_root.create_text(1130,380,font=('Arial', 12), fill='black', text=points, tags='text')  #crea el texto con los puntos
    G_root.create_text(1100,430,font=('Arial', 12), fill='black', text='Coins:') #crea un texto para mostrar las monedas
    G_root.create_text(1140,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext') #mostrara la cantidad de monedas del jugador

    hours=str(hour)+':'
    minutes=str(minute)+':'
    second=str(seconds)

    G_root.create_text(1100,500,font=('Arial', 12),fill='black',text=hours,tags='hours')
    G_root.create_text(1115,500,font=('Arial', 12),fill='black',text=minutes,tags='minutes')
    G_root.create_text(1130,500,font=('Arial', 12),fill='black',text=second,tags='seconds')



    def ingame_time():
        while True:
            global seconds
            global minute
            global hour
            if seconds>=59:
                seconds=0
                minute+=1
                minutes=str(minute)+':'
                second=str(seconds)
                G_root.delete('seconds')
                G_root.delete('minutes')
                G_root.create_text(1115,500,font=('Arial', 12),fill='black',text=minutes,tags='minutes')
                G_root.create_text(1130,500,font=('Arial', 12),fill='black',text=second,tags='seconds')
                time.sleep(1)
            

            elif minute>=59:
                seconds=0
                minute=0
                hour+=1
                hours=str(hour)+':'
                minutes=str(minute)+':'
                second=str(seconds)
                G_root.delete('seconds')
                G_root.delete('minutes')
                G_root.delete('hours')
                G_root.create_text(1100,500,font=('Arial', 12),fill='black',text=hours,tags='hours')
                G_root.create_text(1115,500,font=('Arial', 12),fill='black',text=minutes,tags='minutes')
                G_root.create_text(1130,500,font=('Arial', 12),fill='black',text=second,tags='seconds')
                time.sleep(1)
            
            elif seconds<59:
                seconds+=1
                G_root.delete('seconds')
                second=str(seconds)
                G_root.create_text(1130,500,font=('Arial', 12),fill='black',text=second,tags='seconds')
                time.sleep(1)
                

    Time=Thread(target=ingame_time,args=())
    Time.start()
    


        
        
###actualiza lista de monedas________________________________________________________________________________________________        
    def actual_moneda(M,ID,j,m):
        global monedins
        if j==m:
            return 0
        elif M[j][0]==ID:
            return actual_moneda(M,ID,j+1,m)
        else:
            ids=M[j][0]
            item=M[j][1]
            lista=[ids,item]
            monedins.append(lista)
            actual_moneda(M,ID,j+1,m)
            
    def its_inside(M,ID,i,m): #verifica si la moneda existe
        if i==m:
            return False
        elif M[i][0]==ID:
            return True
        else:
            its_inside(M,ID,i+1,m)

            

    def borrar_monedas(M,ID): #borra la moneda si no se llega a elegir
        if its_inside(M,ID,0,len(M))==True:
            global monedins
            monedins=[]
            G_root.delete(ID)
            actual_moneda(M,ID,0,len(M))
            return 0
        else:
            return 0
    

###Deleting an existing rook______________________________________________________________________________________________________________________________
    def ROOKS(L,M,i,j,n,m): #verifica si se toca a un rook
        if j==m:
            return False
        elif i==n:
            return ROOKS(L,M,0,j+1,n,m)
        elif L[i]==M[j][0]:
            return True
        elif L[i]!=M[j][0]:
            return ROOKS(L,M,i+1,j,n,m)
    def get_rook(L,M,i,j,n,m): #obtiene el rook seleccionado
        if j==m:
            return 0
        elif i==n:
            return get_rook(L,M,0,j+1,n,m)
        elif L[i]==M[j][0]:
            return L[i]
        elif L[i]!=M[j][0]:
            return get_rook(L,M,i+1,j,n,m)

    def updayeLives(ID,L,j,m): #actualiza la lista de vidas de los rooks
        global lisVidas
        if j==m:
            return 0
        elif ID==L[j][0]:
            return updayeLives(ID,L,j+1,m)
        else:
            ids=L[j][0]
            hp=L[j][1]
            lista=[ids,hp]
            lisVidas.append(lista)
            return updayeLives(ID,L,j+1,m)

    def updayeRooks(ID,L,j,m): #actualiza la lista de rooks en canvas
        global maTRooks
        if j==m:
            return 0
        elif ID==L[j][0]:
            return updayeRooks(ID,L,j+1,m)
        else:
            ids=L[j][0]
            item=L[j][1]
            x=L[j][2]
            y=L[j][3]
            lista=[ids,item,x,y]
            maTRooks.append(lista)
            return updayeRooks(ID,L,j+1,m)
    def coinz(O,T,i,j,n,m): #verifica si se toco una moneda
        if j==m:
            return False
        elif i==n:
            return coinz(O,T,0,j+1,n,m)
        elif O[i]==T[j]:
            return True
        else:
            return coinz(O,T,i+1,j,n,m)
    def get_coin(O,T,i,j,n,m): #obtiene el id de la moneda
        if j==m:
            return 0
        elif i==n:
            return get_coin(O,T,0,j+1,n,m)
        elif O[i]==T[j]:
            return O[i]
        else:
            return get_coin(O,T,i+1,j,n,m)
            
            
    def obt_it(mon,M,i,n):
        if i==n:
            return 0
        elif M[i][0]==mon: #si el id concuerda con el id de la moneda en su respectiva lista
            return M[i][1] #se obtiene el valor de la moneda
        else:
            return obt_it(mon,M,i+1,n)



            
    def select_izq(event):
        global maTRooks
        global lisVidas
        global coins
        print('click')
        x=event.x
        y=event.y
        ov=G_root.find_overlapping(x-2,y-2,x+3,y+3)
        ov=list(ov)
        tagss=G_root.find_withtag('coins')
        tagss=list(tagss)
        if len(tagss)>0:
            if coinz(ov,tagss,0,0,len(ov),len(tagss))==True: #si se toca una moneda
                global monedins
                moneda=get_coin(ov,tagss,0,0,len(ov),len(tagss)) #obtiene id de la moneda
                item=obt_it(moneda,monedins,0,len(monedins))
                print('item= ',item)
                if item=='twenty.png':
                    coins+=25
                    G_root.delete('Ctext')
                    G_root.create_text(1140,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext')
                    borrar_monedas(monedins,moneda)
                elif item=='hundreth.png':
                    coins+=100
                    G_root.delete('Ctext')
                    G_root.create_text(1140,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext')
                    borrar_monedas(monedins,moneda)
                elif item=='fifty.png':
                    coins+=50
                    G_root.delete('Ctext')
                    G_root.create_text(1140,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext')
                    borrar_monedas(monedins,moneda)
                    
                
                
                
                
            
        elif len(maTRooks)>0 and len(lisVidas)>0:
            if x<1000:
                
                
                if ROOKS(ov,maTRooks,0,0,len(ov),len(maTRooks))==True: #verifica si se toca a un rook
                    objeto=get_rook(ov,maTRooks,0,0,len(ov),len(maTRooks))
                    matrooks=maTRooks
                    lisvidas=lisVidas
                    lisVidas=[]
                    maTRooks=[]
                    updayeLives(objeto,lisvidas,0,len(lisVidas))
                    updayeRooks(objeto,matrooks,0,len(matrooks))
                    print('objeto= ',objeto)
                    G_root.delete(objeto)
            else:
                print('Fuera de tablero')


                    


####Random coins____________________________________________________________________________________________________________________________________________

        
    def coind():
        global maTrizX
        global maTrizY
        global monedins
        import random
        from random import randrange
        rant=random.randrange(1,25,1)
        rand_MX=random.randrange(1,9,1)
        rand_MY=random.randrange(1,6,1)
        if rant==3:
            coin=LoadImg('twenty.png')
            G_root.jij=coin
            x=maTrizX[int(rand_MX)][0]
            y=maTrizY[int(rand_MY)][0]
            cn=G_root.create_image(x,y,anchor=NW,image=coin,tags='coins')
            item='twenty.png'
            lista=[cn,item]
            monedins.append(lista) #crea una lista para guardar temporalmente las monedas
            time.sleep(5)
            borrar_monedas(monedins,cn)
            coind()
            

        elif rant==6:
            coin=LoadImg('fifty.png')
            G_root.jij=coin
            x=maTrizX[int(rand_MX)][0]
            y=maTrizY[int(rand_MY)][0]
            cn=G_root.create_image(x,y,anchor=NW,image=coin,tags='coins')
            item='fifty.png'
            lista=[cn,item]
            monedins.append(lista)
            time.sleep(5)
            borrar_monedas(monedins,cn)
            coind()
            
            
            

        elif rant==13:
            coin=LoadImg('hundreth.png')
            G_root.jij=coin
            x=maTrizX[int(rand_MX)][0]
            y=maTrizY[int(rand_MY)][0]
            cn=G_root.create_image(x,y,anchor=NW,image=coin,tags='coins')
            item='hundreth.png'
            lista=[cn,item]
            monedins.append(lista)
            time.sleep(5)
            borrar_monedas(monedins,cn)
            coind()

        else:
            time.sleep(2)
            coind()

            
    MONEIDAS=Thread(target=coind,args=())
    MONEIDAS.start()
            
                    

    

###Selecting and placing rooks__________________________________________________________________________________________________________________________
    
    
    def select(event): #funcion para seleccionar el rook
        global price 
        global item
        global rectann_flag
        global enemigos
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
                
###grupo de funciones encargadas de bajar la vida de los enemigos o torres_________________________________________________________________________________

    def hp_reduction(dmg,item,damaged): #empieza a reducir la vida de un objeto
        global lisVidas #se obtienen las listas que tienen los id y vida de los enemigos
        global VidsEn  #----------------------------------------------------------------
        global enemigos

        if damaged=='tower':  #comprueba si la variable damaged es la torre
            print('to reduce tower')
            hp_aux(lisVidas,0,0,len(lisVidas),item,dmg) #manda a llamara la funcion encargada de reducir la vida del rook
            return 0
        elif damaged=='enemy':  #comprueba si la variable damaged es enemy 
            hp_aux_en(VidsEn,0,0,len(VidsEn),item,dmg,enemigos) #se llama a la funcion encargada de reducir la vida del enemigo
            return 0
            
            


    def hp_aux(M,i,j,m,item,dmg):
        if j==m:
            return 0
        elif M[j][i]==item:  #si el item de la matriz es igual al item enviado
            new_hp=(M[j][i+1])-dmg #le resta a la vida el dano hecho por el objeto
            global lisVidas
            lisVidas=[]  #resetea la lista para actualizarla
            print('baja vida a la torre= ',new_hp)
            edit(new_hp,M[j][i],M,0,0,m) #esta funcion actualizara la matriz de vidas de los rooks
            return 0
        else:
            return hp_aux(M,i,j+1,m,item,dmg) #en caso de que el item no concuerde con uno el id, entonces se para a la siguiente lista
    def actualizar_rook(M,ID,i,n):
        if i==n:
            return 0
        elif M[i][0]==ID:
            return actualizar_rook(M,ID,i+1,n)
        elif M[i][0]!=ID:
            global maTRooks
            lista=M[i]
            maTRooks.append(lista)
            return actualizar_rook(M,ID,i+1,n)
        

    def edit(NHP,item,M,i,j,m): #carga la vida reducida, el item, la matriz original, i, j y el largo de la matriz, para actualizar la lista de vidas
        global lisVidas

        if j==m:
            return 0
        elif M[j][i]!=item: #si el id de la matriz original es diferente del item al que se le redujo la vida             
            lista=[M[j][i],M[j][i+1]]  #se crea una lista con el id original y su vida para 
            lisVidas.append(lista) #agregarla a la lista de vidas de las torres
            return edit(NHP,item, M, i, j+1,m) #vuelve a llamar y cambia la posicion de la lista original
        
        elif M[j][i]==item: #si el id de la lista es igual al item, entonces  
            if NHP<=0: #si la vida reducida es menor a 0
                global maTRooks #viene en el ordem [rook,x,y]
                M=maTRooks
                actualizar_rook(M,item,0,len(M))
                G_root.delete(item) #se borra el item
                return edit(NHP,item, M, i,j+1,m)
                
            else:
                lista=[item,NHP] #en caso de que no sea menor a 0, se crea una lista con el id y la vida reducida
                lisVidas.append(lista) #se le agrega a la lista de vidas de torres la sublista con la actualizacion
                return edit(NHP,item, M, i,j+1,m)
        else:
            return edit(NHP,item, M, i,j+1,m) #se vuelve a llamar para evitar errores
        
##reduces enemy hp___________________________________________________________________________________________________________________________________________
    def hp_aux_en(M,i,j,m,item,dmg,E): #hacen lo mismo que para la torre
        if j==m:
            return 0
        elif M[j][i]==item:
            new_hp=(M[j][i+1])-dmg
            global VidsEn #en este caso se llama a la lista de vidas de enemigos
            VidsEn=[] #se resetea 
            edit_en(new_hp,M[j][i],M,0,0,m,E)
            return 0
        else:
            return hp_aux_en(M,i,j+1,m,item,dmg,E)
    def actualizar_en(L,ID,j,m): #actualiza los enemigos existentes
        if j==m:
            return 0
        elif L[j][0]==ID:
            
                
            return actualizar_en(L,ID,j+1,m,)
                
            
        elif L[j][0]!=ID:
            global enemigos
            lista=L[j]
            enemigos.append(lista)
            return actualizar_en(L,ID,j+1,m)
    def f_it(E,i,n,ID):
        if i==n:
            return 0
        elif E[i][0]==ID:
            return E[i][1]
        else:
            return f_it(E,i+1,n,ID)
            

    def edit_en(NHP,item,M,i,j,m,E): 
        global VidsEn 
        global points
        if j==m:
            return 0
        elif M[j][i]!=item:
            lista=[M[j][i],M[j][i+1]]
            VidsEn.append(lista)
            return edit_en(NHP,item, M, i, j+1,m,E)
        
        elif M[j][i]==item:
            global user
            
            A=mixer.Sound(user+'/Desktop/proyecto_taller_1/music/armror.mp3')
            B=mixer.Sound(user+'/Desktop/proyecto_taller_1/music/hit.mp3')
            C=mixer.Sound(user+'/Desktop/proyecto_taller_1/music/slick.mp3')
            if f_it(E,0,len(E),item)=='escudero.png':
                mixer.Sound.set_volume(A,0.3)
                mixer.Sound.play(A)
                

            elif f_it(E,0,len(E),item)=='canibal.png':
                mixer.Sound.set_volume(B,0.3)
                mixer.Sound.play(B)
                

            elif f_it(E,0,len(E),item)=='lenador.png':
                mixer.Sound.set_volume(C,0.3)
                mixer.Sound.play(C)
                

            elif f_it(E,0,len(E),item)=='arquero.png':
                mixer.Sound.set_volume(B,0.3)
                mixer.Sound.play(B)
            
            if NHP<=0:
                global enemigos
                enemigos=[]
                global coins #se llama la variable con la cantidad de monedas
                actualizar_en(E, item, 0,len(E))
                coins+=75  #se suman las monedas por derrotar un enemigo
                G_root.delete(item) #se borra el enemigo
                points+=1 #se suma un punto
                G_root.delete('text') #se borra el texto con los puntos
                G_root.delete('Ctext') #se borra el texto con la cantidad de monedas
                G_root.create_text(1140,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext')  #se crean de nuevo con los valores actualizados
                G_root.create_text(1130,380,font=('Arial', 12), fill='black', text=str(points), tags='text')
                return edit_en(NHP,item, M, i,j+1,m,E)
            else:
                lista=[item,NHP]
                VidsEn.append(lista)
                return edit_en(NHP,item, M, i,j+1,m,E)
        else:
            return edit_en(NHP,item, M, i,j+1,m,E)



        
###funcion para colocar el rook_________________________________________________________________________________________________

    def place(x,y,iX,jX,iY,jY, MatX,MatY):  #posicionara el rook seleccionado en una coordenada especifica
        global coins
        global maTRooks
        global price
        global item
        global rectann_flag
        global lisVidas
        a='sand_rook.png'
        b='rock_rook.png'
        c='fire_rook.png'
        d='water_rook.png'
        
           
        l=G_root.find_overlapping(x, y, x+5, y+5)  #obtiene los objetos que estan dentro del cuadrado especificado
        money=coins  #variable por que antes coins era un string pero en realidad no se ocupa pero me dio pereza quitarlo
        if len(l)<2:
            if money>=price:  #comprueba si hay suficiente dinero para poner el rook
                if jX==len(MatX) or jY==len(MatY): #condicion de finalizacion en caso de que no se haya seleccionado dentro del tablero
                    print('cant place')
                    item='' #reinicia el item
                    price=0 #reinicia el precio
                    G_root.delete('rect')
                    rectann_flag=False
                    
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
                        tower=[tw,item,pos_x,pos_y]
                        hpss=[tw,hp]
                        lisVidas.append(hpss)
                        maTRooks.append(tower)
                        G_root.delete('Ctext')
                        G_root.create_text(1130,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext')
                        tower_thread(pos_x, pos_y, item,tw) #llama a la funcion que deberia iniciar el proceso de crear los threads para crear los misiles
                        item=''
                        price=0
                        rectann_flag=False
                        Givein(tw)

                        
                        
                    else:
                        place(x,y,iX,jX,0,jY+1,MatX, MatY) #se mueve al siguiente par de coordenadas en Y
                else:
                    place(x,y,0,jX+1,iY,jY,MatX, MatY) #se mueve al siguiente par de coordenadas X
            else:
                print('insufficient money')
                G_root.delete('rect')
                rectann_flag=False
        else:
            print('Already in use')
            G_root.delete('rect')
            rectann_flag=False

    def Givein(obj):
        G_root.move(obj,1,0)
        time.sleep(0.1)
        G_root.move(obj,-1,0)
        time.sleep(15)
        Givein(obj)

###comprobar si estan chocando dos objetos
    def comp(ov,en,i,p,n,d):
        if p==d:
            return False
        elif i==n:
            return comp(ov,en,0,p+1,n,d)
        elif en[i]==ov[p]: #analiza si el id concuerda con el que esta haciendo overlap
            return True
        else:
            return comp(ov,en,i+1,p,n,d) #si no hace overlap se mueve al siguiente id del que chocó

    def objects(ov,en,i,p,n,d,res):
        if p==d:
            return res
        if i==n:
            return objects(ov,en,0,p+1,n,d,res)
        elif en[i]==ov[p]:
            return objects(ov,en,i+1,d,n,d,res+en[i])
        else:
            return objects(ov,en,i+1,p,n,d,res)


#Funcion para determinar si el rook que lanza la flecha sigue vivo_________________________________________________________________________________
    def R_alive(en,V,i,n):
        if i==n:
            return False
        elif V[i][0]==en:
            
            return True
        else:
            return R_alive(en,V,i+1,n)


###funcion que mueve el misil_____________________________________________________________________________________________                       
    def move_misil(misil,dmg,obj):
        
        en_coords=G_root.coords(misil)
        x=en_coords[0]
        y=en_coords[1]
        overlap=G_root.find_overlapping(x, y, x+30,y+30) #encuentra los objetos haciendo overlap al misil
        overlap=list(overlap) #los enlista
        enemys=G_root.find_withtag('enemy') #saca los tags enemigos
        enemys=list(enemys)
        if y<=775:
            if len(overlap)>=2: #overlap siempre va a ser el fondo y o la torre, asi que si es mayor o igual a dos, que compruebe si alguno de esos es el misil
                if comp(overlap,enemys,0,0,len(enemys),len(overlap))==True: #si el id del enemigo se encuentra haciendo overlap con el misil
                    objecT=objects(overlap,enemys,0,0,len(enemys),len(overlap),0) #obtiene el id del enemigo haciendo overlap
                    hp_reduction(dmg,objecT,'enemy') #manda a llamar la funcion que reduce la vida con el dano producido, el id del objeto(numero entero)y enemy como indicador
                    G_root.delete(misil) #borra el misil al impactar
                else:
                    G_root.move(misil, 0, 5) #en caso de que no sea un enemigo el que hace overlap, se mueve el misil
                    time.sleep(0.02)
                    move_misil(misil,dmg,obj)
            else:
                G_root.move(misil, 0, 10) #en caso de que no hayan dos objetos haciendo overlap, se mueve el misil
                time.sleep(0.02)
                move_misil(misil,dmg,obj)
                
        else:
            G_root.delete(misil) #en caso de que se salga del tablero, se elimina el misil




###Funcion que verifica si hay un enemigo al final de la columna donde esta el rook______________________________________________________________________________               
    def verify(x,MY):
        global enemigos
        if len(G_root.find_overlapping(x,MY[0],x+20,MY[1]))>=2:
            L=G_root.find_overlapping(x,MY[0],x+20,MY[1])
            if ver(enemigos,list(L),0,0,len(L),len(enemigos))==True:
                return True
        else:
            return False

    def ver(En,L,i,j,n,m):
        if j==m:
            return False
        elif i==n:
            return ver(En, L, 0,j+1,n,m)
        elif  L[i]== En[j][0]:
            return True
        else:
            return ver(En,L,i+1,j,n,m)

        
        

###Funcion que crea el misil_____________________________________________________________________________________________________________________________________
        
    def shooting(objt,x,y,torre): #objt es el rook colocado, x es la equina superior izquierda y y la parte de arriba del cuadrito dentro del tablero
        global maTrizX #llama la funcion con el inicio y final de cada columna
        global lisVidas
        maTborderY=[156,773]
        a='sand_rook.png'
        b='rock_rook.png'
        c='fire_rook.png'
        d='water_rook.png'
        if R_alive(torre,lisVidas,0,len(lisVidas))==True:
            print('Lista de vidas: ',lisVidas,' objeto= ',torre)
            if verify(x,maTborderY)==True:
                if objt==a:  #comprueba si el elemento elegido es igual a tal objeto para entonces crear el misil que le corresponde

                    misl=LoadImg('sand.png')
                    G_root.sndaa=misl
                    mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                    move_misil(mis,2,torre) #se llama a mover el misil con el id del objeto y la cantidad de daño que produce el misil
                    time.sleep(5)
                    shooting(objt,x,y,torre)
                    
                elif objt==b:

                    misl=LoadImg('rock.png')
                    G_root.rocvok=misl
                    mis=G_root.create_image(x+25, y+30, anchor=NW,image=misl, tags='misil')
                    move_misil(mis,4,torre)
                    time.sleep(5)
                    shooting(objt,x,y,torre)
                    
                elif objt==c:

                    misl=LoadImg('fire.png')
                    G_root.fiah=misl
                    mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                    move_misil(mis,8,torre)
                    time.sleep(5)
                    shooting(objt,x,y,torre)
                    
                elif objt==d:

                    misl=LoadImg('water.png')
                    G_root.wteer=misl
                    mis=G_root.create_image(x+25, y+30, anchor=NW, image=misl, tags='misil')
                    move_misil(mis,8,torre)
                    time.sleep(5)
                    shooting(objt,x,y,torre)
                    
            else:
                time.sleep(3)
                shooting(objt,x,y,torre)


        

    def tower_thread(x,y, objt,torre): #objt es el str de la torre, torre es el id
        crte=Thread(target=shooting, args=(objt,x, y,torre))
        crte.start()


#funciones para extraer datos______________________________________________________________
    def past():  #se encargara de poner los rooks guardados del pasado
        global lisPast #obtiene la lista con los rooks pasados
        place_past(lisPast,0,len(lisPast))

    def place_past(L,i,n): #colocara los rooks, las listas vienen 
        global lisVidas
        global maTRooks
        if i==n:
            print('done')
        else:
            a='sand_rook.png'
            b='rock_rook.png'
            c='fire_rook.png'
            d='water_rook.png'

            item=L[i][0]
            if item==a:
                hp=12

            elif item==b:
                hp=14

            elif item==c:
                hp=16

            elif item==d:
                hp=16
            it=LoadImg(item)
            G_root.its=it
            pos_x=L[i][1]
            pos_y=L[i][2]
            tw=G_root.create_image(pos_x, pos_y, anchor=NW, image=it, tag='tower')
            tower=[tw,item,pos_x,pos_y]
            hpss=[tw,hp]
            lisVidas.append(hpss)
            maTRooks.append(tower)
            tower_thread(pos_x, pos_y, item,tw)            
            place_past(L,i+1,n)
            Givein(tw)

#Funcion que colocara cada enemigo de la partida pasada___________________________________________________________________
    def pasEnes(): #va a llamar a la funcion que coloca cada enemigo
        global nuevos
        pas_aux(nuevos,0,len(nuevos))
        
    def pas_aux(L,j,m):
        if j==m:
            print('done')
        else:
            global VidsEn
            global enemigos
            a='arquero.png'
            b='canibal.png'
            c='escudero.png'
            d='lenador.png'
            item=L[j][0]
        
            if item==a:
                arq=LoadImg('arquero.png')
                G_root.enemigo=arq
                x=L[j][1]
                y=L[j][2]
                Enemy=G_root.create_image(x, y, anchor=NW, image=arq, tags='enemy')
                hp=5
                Bakemono=[Enemy,hp]
                VidsEn.append(Bakemono)
                bakemono=[Enemy,a,x,y]
                enemigos.append(bakemono)
                M=Thread(target=movementArquero,args=(Enemy, 12,2))
                M.start()
                pas_aux(L,j+1,m)

            elif item==b:
                can=LoadImg('canibal.png')
                G_root.enemigo=can
                x=L[j][1]
                y=L[j][2]
                Enemy=G_root.create_image(x, y, anchor=NW, image=can, tags='enemy')
                hp=25
                Bakemono=[Enemy,hp]
                VidsEn.append(Bakemono)
                bakemono=[Enemy,b,x,y]
                enemigos.append(bakemono)
                N=Thread(target=movementCanibal,args=(Enemy, 14,12))
                N.start()
                pas_aux(L,j+1,m)

            elif item==c:
                esq=LoadImg('escudero.png')
                G_root.enemigo=esq
                x=L[j][1]
                y=L[j][2]
                Enemy=G_root.create_image(x, y, anchor=NW, image=esq, tags='enemy')
                hp=10
                Bakemono=[Enemy,hp]
                VidsEn.append(Bakemono)
                bakemono=[Enemy,c,x,y]
                enemigos.append(bakemono)
                O=Thread(target=movementEscuas,args=(Enemy, 10, 3))
                O.start()
                pas_aux(L,j+1,m)


            elif item==d:
                lena=LoadImg('lenador.png')
                G_root.enemigo=lena
                x=L[j][1]
                y=L[j][2]
                Enemy=G_root.create_image(x, y, anchor=NW, image=lena, tags='enemy')
                hp=20
                Bakemono=[Enemy,hp]
                VidsEn.append(Bakemono)
                bakemono=[Enemy,d,x,y]
                enemigos.append(bakemono)
                P=Thread(target=movementLena,args=(Enemy, 13, 9))
                P.start()
                pas_aux(L,j+1,m)
            
            


    def staticE(status):
        if status=='succes':
            D=Thread(target=pasEnes)
            D.start()



    def create_matEn(L,status):
        global nuevos
        if L==[] or status=='Error':
            staticE(status)#funcion que empieza el thread para crear los enemigos
        else:
            if len(L)>=4: #si aun hay 4 elementos en la lista
                item=L[1] #no se toma en cuenta el 0 por que es un id que ya no vale nada
                x=L[2]    
                y=L[3]
                lista=[item,x,y]
                nuevos.append(lista)
                print('La matriz poco a poco= ',nuevos)
                create_matEn(L[4:],'succes')
            else:
                create_matEn(L,'Error')
            

    def staticD():
        G=Thread(target=past)
        G.start()
        global pastEnList
        create_matEn(pastEnList,'') #llama a la funcion para crear la matriz de la partida guardada, los enemigos
        
            
            




            
    def extract(lista): #extrae los datos de la lista y se los da las globales
        global coins
        global points
        global hour
        global minute
        global seconds
        lista=lista[2:] #se elimina el 1 y el nombre ya que no se ocupan, la lista queda [monedas,puntos,rook,x,y,rook,...]
        coins=int(lista[0]) #se registran la cantidad de monedas de la partida
        G_root.delete('Ctext')
        G_root.create_text(1130,430,font=('Arial', 12), fill='black', text=coins, tags='Ctext') #se actualiza el texto con la cantidad de monedas
        lista=lista[1:] #la lista queda [puntos, rook, x,y,rooks,x,y,...]
        seconds=int(lista[0])
        lista=lista[1:]
        minute=int(lista[0])
        lista=lista[1:]
        hour=int(lista[0])
        lista=lista[1:]
        points=int(lista[0]) #se sacan los puntos de la partida pasada
        G_root.delete('text')
        G_root.create_text(1130,380,font=('Arial', 12), fill='black', text=points, tags='text') #se actualizan los puntos
        lista=lista[1:] #la lista queda con los rooks
        create_mat(lista) #creara la matriz para colocar los rooks
        

    def compruebelo(lis):
        if lis=='arquero.png' or lis=='canibal.png' or lis=='lenador.png' or lis=='escudero.png':
            return True
        else:
            return False
        
#Crea la matriz de rooks______________________________________________________________________________________________________________
    def create_mat(lista):
        global lisPast
        if lista==[]:
            
            staticD()  #llama la funcion que empieza el hilo que crea los rooks guardados
        elif lista[1]=='arquero.png' or lista[1]=='canibal.png' or lista[1]=='lenador.png' or lista[1]=='escudero.png': #si el elemento que le sigue al elemnto 0 es uno de los enemigos
            global pastEnList             
            pastEnList=lista            #se le asigna a pastEnList lo que sobro de la lista
            create_mat([])

        else:
            item=lista[1]
            pos_x=int(lista[2])
            pos_y=int(lista[3])
            lisT=[item,pos_x,pos_y] #crea una lista con los items del rook
            lisPast.append(lisT) #se le agrega a la lista de rooks pasados la sublista con la informacion de cada rook
            create_mat(lista[4:]) #se cortan 3 elementos de la lista
            

    #se encarga de convertir el readlines en una lista legible a como se quiere
    def ver_r(lines):
        return ver_aux(lines,0,len(lines))
    
    def ver_aux(L,i,n):
        if i==n:
            print('done')
        else:
            global merman
            merman=L[i].strip().split(',') #agarra la lista de cada lista del readlines y si hay comma, lo separa creando la lista
            
    ver_r(lines)

    global merman

    #si hay un 0 al inicio del documento es que no hay partida guardada_______________________________
    if merman[0]=='0':
        print('0')
       
    elif merman[0]=='1' and merman[1]==name: #si hay un uno, entonces si hay partida guardada y se procede a leer si el nombre guardado coincide con el nombre ingresado
        
        extract(merman) #se llama a la funcion que extraera los datos de la lista
    def destroy_allR(j,m):
        global maTRooks
        if j==m:
            global lisVidas
            lisVidas=[] 
            return 0
        else:
            rook=maTRooks[j][0]
            G_root.delete(rook)
            return destroy_allR(j+1,m)

    def destroy_allE(j,m):
        global enemigos
        if j==m:
            global VidsEn
            VidsEn=[]
            return 0
        else:
            ene=enemigos[j][0]
            G_root.delete(ene)
            return destroy_allE(j+1,m)
        

    def win():
        global user
        global seconds
        global minute
        global hour
        global name
        global maTRooks
        global enemigos
        
        s=str(seconds)
        h=str(hour)
        m=str(minute)
        destroy_allR(0,len(maTRooks))
        destroy_allE(0,len(enemigos))
        anima_win()

        p=open(user+'/Desktop/proyecto_taller_1/puntajes.txt','a')
        p.write(name+','+h+','+m+','+s+',')
        p.close()
        f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w')
        f.write('0')
        f.close()
        g_root.destroy()
        root.deiconify()
        mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
        mixer.music.play(loops=-1)
        
        
    
        
#Funcion para crear enemigos___________________________________________________________________________________
    def enemy():
        global maTRooks
        global enemigos
        global points
        velo=15000 
        if points>=10 and points<=19: #estos if definen la velocidad de aparacion enemiga dependiendo del nivel
            if points==10:
                
                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))
                G_root.create_text(100,600,fill='black', text='NIVEL 2, adquiera 20 puntos para nivel 3', font=('Arial',14))
                time.sleep(3)
                L.destroy()
                velo=int(velo-(velo*0.30))
                muu=Thread(target=crte, args=())
                muu.start()
                G_root.after(velo,enemy)
            else:    
                velo=int(velo-(velo*0.30))
                muu=Thread(target=crte, args=())
                muu.start()
                G_root.after(velo,enemy)
                
        elif points>=20 and points<=59:
            if points==20:
                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))
                G_root.create_text(100,600,fill='black', text='NIVEL 3, adquiera 60 puntos para ganar', font=('Arial',14))
                time.sleep(3)
                L.destroy()
                velo=int(velo-(velo*0.60))
                muu=Thread(target=crte, args=())
                muu.start()
                G_root.after(velo,enemy)
            else:
                velo=int(velo-(velo*0.60))
                muu=Thread(target=crte, args=())
                muu.start()
                G_root.after(velo,enemy)
        elif points>=60:
            win()
        else:
            muu=Thread(target=crte, args=())
            muu.start()
            G_root.after(velo,enemy)
            
    def crte():
        global VidsEn
        global enemigos
        import random
        from random import randrange
        rand=random.randrange(94,760,95)
        ren=random.randrange(1,5,1)
        if ren==1:
            arq=LoadImg('arquero.png')
            G_root.enemigo=arq
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=arq, tags='enemy')
            hp=5
            Bakemono=[Enemy,hp]
            VidsEn.append(Bakemono)
            an='arquero.png'
            x=rand
            y=780
            bakemono=[Enemy,an,x,y]
            enemigos.append(bakemono)
            movementArquero(Enemy, 12,2)

        elif ren==2:
            can=LoadImg('canibal.png')
            G_root.enemigo=can
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=can, tags='enemy')
            hp=25
            Bakemono=[Enemy,hp]
            VidsEn.append(Bakemono)
            an='canibal.png'
            x=rand
            y=780
            bakemono=[Enemy,an,x,y]
            enemigos.append(bakemono)
            movementCanibal(Enemy, 14,12)

        elif ren==3:
            esq=LoadImg('escudero.png')
            G_root.enemigo=esq
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=esq, tags='enemy')
            hp=10
            Bakemono=[Enemy,hp]
            VidsEn.append(Bakemono)
            an='escudero.png'
            x=rand
            y=780
            bakemono=[Enemy,an,x,y]
            enemigos.append(bakemono)
            movementEscuas(Enemy, 10, 3)


        elif ren==4:
            lena=LoadImg('lenador.png')
            G_root.enemigo=lena
            Enemy=G_root.create_image(rand, 780, anchor=NW, image=lena, tags='enemy')
            hp=20
            Bakemono=[Enemy,hp]
            VidsEn.append(Bakemono)
            an='lenador.png'
            x=rand
            y=780
            bakemono=[Enemy,an,x,y]
            enemigos.append(bakemono)
            print('enemigos apenas se pone= ',enemigos)
            movementLena(Enemy, 13, 9)

##Funcion para terminar el juego al perder y se borran los datos de guardado________________________________________________________

    def loose():
        global enemigos
        global maTRooks
        f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w')
        f.write('0')
        f.close
        destroy_allR(0,len(maTRooks))
        destroy_allE(0,len(enemigos))
        mixer.music.set_volume(0.2)
        mixer.music.stop()
        mixer.music.unload()
        g_root.destroy()
        root.deiconify()
        anima_loose()
        mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
        mixer.music.play(loops=-1)



#Funcion para determinar si el avatar que lanza la flecha sigue vivo_________________________________________________________________________________
    def alive(en,V,i,n): #verifica si el avatar aun vive
        if i==n:
            return False
        elif V[i][0]==en:
            return True
        else:
            return alive(en,V,i+1,n)


    def update(obj,N,E,j,m): #actualiza la lista de enemigos
        global enemigos
        enemigos=[]
        up_aux(obj,N,E,j,m) 
        


    def up_aux(obj,N,E,j,m):
        global enemigos
        if j==m:
            print('done')
        elif E[j][0]==obj:
            lista=[obj,E[j][1],int(N[0]),int(N[1])]
            enemigos.append(lista)
            return up_aux(obj,N,E,j+1,m)
        else:
            lista=E[j]
            enemigos.append(lista)
            return up_aux(obj,N,E,j+1,m)
            
        
##Funcion para mover los enemigo__________________________________________________________________________________________________

    def movementLena(en,t, dmg):
        global VidsEn
        global enemigos
        if alive(en,VidsEn,0,len(VidsEn))==True:
            en_coords=G_root.coords(en)
            x=en_coords[0]
            y=en_coords[1]
            ov=G_root.find_overlapping(x+10,y-10,x,y)
            ov=list(ov)
            rooks=G_root.find_withtag('tower')
            rooks=list(rooks)
            if y>=150:
                if len(ov)>=2:
                    if comp(ov,rooks,0,0,len(rooks),len(ov))==True:
                        objecT=objects(ov,rooks,0,0,len(rooks),len(ov),0)
                        het=LoadImg('lena_hit.png')
                        G_root.huisi=het
                        hitt=G_root.create_image(x,y,anchor=NW,image=het,tags='hittingL')
                        time.sleep(1)
                        G_root.delete('hittingL')
                        hp_reduction(dmg,objecT,'tower')
                        time.sleep(5)
                        movementLena(en,t,dmg)
                else:    
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    en_coords=G_root.coords(en)
                    x=en_coords[0]
                    y=en_coords[1]
                    time.sleep(t)
                    new=[x,y]
                    update(en, new,enemigos,0,len(enemigos))
                    movementLena(en, t,dmg)
            else:
                loose()
                

#Funcion que mueve la flecha del arquero______________________________________________________________________________
        
    def shoot_arq(x,y,dmg,obj):
        en_coords=G_root.coords(obj)
        x=en_coords[0]
        y=en_coords[1]
        ov=G_root.find_overlapping(x+10,y-5,x,y)
        ov=list(ov)
        rooks=G_root.find_withtag('tower')
        rooks=list(rooks)
        if y>=10:
            if len(ov)>=2:
                if comp(ov,rooks,0,0,len(rooks),len(ov))==True:
                    objecT=objects(ov,rooks,0,0,len(rooks),len(ov),0)
                    hp_reduction(dmg,objecT,'tower')
                    G_root.delete(obj)
                else:
                    G_root.move(obj, 0, -5)
                    time.sleep(0.03)
                    shoot_arq(x,y,dmg,obj)
            else:
                G_root.move(obj, 0, -5)
                time.sleep(0.03)
                shoot_arq(x,y,dmg,obj)
                
        else:
           G_root.delete(obj)
           

    

        
                
        
#Funcion que crea la flecha______________________________________________________________________________________________________________________________
    def crear_arrow(x,y,dmg,en):
        global VidsEn
        if alive(en,VidsEn,0,len(VidsEn))==True:
            arro=LoadImg('arrow.png')
            G_root.als=arro
            a=G_root.create_image(x,y,anchor=NW,image=arro,tags='arrow')
            shoot_arq(x,y,dmg,a)
            time.sleep(10)
            crear_arrow(x,y,dmg,en)

            
        
#Funcion que mueve al arquero__________________________________________________________________________________________________________________________
    def movementArquero(en,t,dmg):
        global VidsEn
        global enemigos
        if alive(en,VidsEn,0,len(VidsEn))==True:
            en_coords=G_root.coords(en)
            x=en_coords[0]
            y=en_coords[1]
            ov=G_root.find_overlapping(x+10,y-700,x,y)
            ov=list(ov)
            rooks=G_root.find_withtag('tower')
            rooks=list(rooks)
            if y>=150:
                if len(ov)>=2:
                    if comp(ov,rooks,0,0,len(rooks),len(ov))==True:
                        alta=Thread(target=crear_arrow,args=(x+15,y+10,dmg,en))
                        alta.start()
                    
                        #objecT=objects(ov,rooks,0,0,len(rooks),len(ov),0)
                        hut=LoadImg('arquero_shoot.png')
                        G_root.huisi=hut
                        hitt=G_root.create_image(x,y,anchor=NW,image=hut,tags='hittingA')
                        time.sleep(0.3)
                        G_root.delete('hittingA')
                    
                        G_root.move(en, 0, -10)
                        time.sleep(0.1)
                        G_root.move(en, 0, -10)
                        time.sleep(0.1)
                        G_root.move(en, 0, -10)
                        time.sleep(0.1)
                        G_root.move(en, 0, -10)
                        time.sleep(0.1)
                        G_root.move(en, 0, -10)
                        time.sleep(0.1)
                        G_root.move(en, 0, -10)
                        en_coords=G_root.coords(en)
                        x=en_coords[0]
                        y=en_coords[1]
                        time.sleep(t)
                        new=[x,y]
                        update(en, new,enemigos,0,len(enemigos))
                        time.sleep(t)
                        movementArquero(en,t,dmg)
                else:
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    en_coords=G_root.coords(en)
                    x=en_coords[0]
                    y=en_coords[1]
                    time.sleep(t)
                    new=[x,y]
                    update(en, new,enemigos,0,len(enemigos))
                    time.sleep(t)
                    movementArquero(en, t, dmg)
            else:
                G_root.delete(en)
                loose()

            
#Funcion para mover al escudero___________________________________________________________________________________________________________
            
    def movementEscuas(en,t,dmg):
        global VidsEn
        global enemigos
        if alive(en,VidsEn,0,len(VidsEn))==True:
            en_coords=G_root.coords(en)
            x=en_coords[0]
            y=en_coords[1]
            ov=G_root.find_overlapping(x+10,y-10,x,y)
            ov=list(ov)
            rooks=G_root.find_withtag('tower')
            rooks=list(rooks)
            if y>=150:
                if len(ov)>=2:
                    if comp(ov,rooks,0,0,len(rooks),len(ov))==True:
                        objecT=objects(ov,rooks,0,0,len(rooks),len(ov),0)
                        het=LoadImg('escuas_hit.png')
                        G_root.huisi=het
                        hitt=G_root.create_image(x,y,anchor=NW,image=het,tags='hittingE')
                        G_root.delete('hittingE')
                        hp_reduction(dmg,objecT,'tower')
                        time.sleep(15)
                        movementEscuas(en,t,dmg)
                else:    
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    en_coords=G_root.coords(en)
                    x=en_coords[0]
                    y=en_coords[1]
                    time.sleep(t)
                    new=[x,y]
                    update(en, new,enemigos,0,len(enemigos))
                    time.sleep(t)
                    movementEscuas(en, t,dmg)
            else:
                loose()
        


    def movementCanibal(en,t,dmg):
        global VidsEn
        global enemigos
        if alive(en,VidsEn,0,len(VidsEn))==True:
            en_coords=G_root.coords(en)
            x=en_coords[0]
            y=en_coords[1]
            ov=G_root.find_overlapping(x+10,y-10,x,y)
            ov=list(ov)
            rooks=G_root.find_withtag('tower')
            rooks=list(rooks)
            if y>=150:
                if len(ov)>=2:
                    if comp(ov,rooks,0,0,len(rooks),len(ov))==True:
                        objecT=objects(ov,rooks,0,0,len(rooks),len(ov),0)
                        hit=LoadImg('canibal_hit.png')
                        G_root.huisi=hit
                        hitt=G_root.create_image(x,y,anchor=NW,image=hit,tags='hittingC')
                        G_root.delete('hittingC')
                        hp_reduction(dmg,objecT,'tower')
                        time.sleep(3)
                        movementCanibal(en,t,dmg)
                
                else:    
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    time.sleep(0.1)
                    G_root.move(en, 0, -10)
                    en_coords=G_root.coords(en)
                    x=en_coords[0]
                    y=en_coords[1]
                    time.sleep(t)
                    new=[x,y]
                    update(en, new,enemigos,0,len(enemigos))
                    time.sleep(t)
                    movementCanibal(en, t,dmg)
                    
            else:
                loose()
    Enemigo=Thread(target=enemy,args=())
    Enemigo.start()
    #enemy()

###Bindings
    g_root.bind("<Button-1>", select)
    g_root.bind("<Button-3>", select_izq)






    def stringear_En(M,i,j,m,n):
        global stringEnes
        if j==m:
            return 0
        elif i==n:
            return stringear_En(M,0,j+1,m,n)
        else:
            stringEnes+=','
            stringEnes+=str(M[j][i])
            return stringear_En(M,i+1,j,m,n)#agrega una comma entre cada elemento de la matriz
    
    
    


    def stringear(M,i,j,m,n):
        global stringRooks
        if j==m:
            return 0
        elif i==n:
            return stringear(M,0,j+1,m,n)
        else:
            stringRooks+=','
            stringRooks+=str(M[j][i])
            return stringear(M,i+1,j,m,n)#agrega una comma entre cada elemento de la matriz
        
    
              
#Funcion para cerrar el juego y guardar los datos_________________________________________________________________________________________________________

        
    def Return():
        global user #para la direccion no da problema
        global coins #la cantidad de monedas
        global maTRooks #la lista con los rooks y sus coordenadas y vida
        global points
        global enemigos
        global stringRooks#los rooks en string
        global stringEnes
        global seconds
        global minute
        global hour
        print('rooks= ',maTRooks)
        print('enemigos= ',enemigos)
        points=str(points)
        s=str(seconds)
        h=str(hour)
        m=str(minute)
        if len(maTRooks)>0 and len(maTRooks[0])==4:
            if len(enemigos)>0:
                stringear_En(enemigos,0,0,len(enemigos),len(enemigos[0]))
                stringear(maTRooks,0,0,len(maTRooks),len(maTRooks[0])) #convierte en string todos los valores de la matriz
                enes=stringEnes
                rooks=stringRooks
                mixer.music.set_volume(0.2)
                mixer.music.stop()
                mixer.music.unload()
                name=str(Name.get()) #para obtener el nombre del jugador
                money=str(coins)    #para el int en un string
                
                f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w') #abre el documento para reescribirlo
                f.write('1'+','+name+','+money+','+s+','+m+','+h+','+points+rooks+enes) #agrega un 1 que va a indicar luego si hay o no una partida guardada
                                                       
                f.close()
                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))
                g_root.destroy()
                root.deiconify()
                mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
                mixer.music.play(loops=-1)
            else:
                stringear(maTRooks,0,0,len(maTRooks),len(maTRooks)) #convierte en string todos los valores de la matriz
                rooks=stringRooks
                mixer.music.set_volume(0.2)
                mixer.music.stop()
                mixer.music.unload()
                name=str(Name.get()) #para obtener el nombre del jugador
                money=str(coins)    #para el int en un string
                f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w') #abre el documento para reescribirlo
                f.write('1'+','+name+','+money+','+s+','+m+','+h+','+points+rooks) #agrega un 1 que va a indicar luego si hay o no una partida guardada
                                                       
                f.close()
                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))
                g_root.destroy()
                root.deiconify()
                mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
                mixer.music.play(loops=-1)
                
        else:
            if len(enemigos)>0:
                stringear_En(enemigos,0,0,len(enemigos),len(enemigos))
                enes=stringEnes
                mixer.music.set_volume(0.2)
                mixer.music.stop()
                mixer.music.unload()
                name=str(Name.get()) #para obtener el nombre del jugador
                money=str(coins)    #para el int en un string
                f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w') #abre el documento para reescribirlo
                f.write('1'+','+name+','+money+','+s+','+m+','+h+','+points+enes) #agrega un 10 que me va a indicar luego si hay o no una partida guardada, cuando solucione el problema de hacerlo lista ese
                f.close()
                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))
                g_root.destroy()
                root.deiconify()
                mixer.music.load(user+'/Desktop/proyecto_taller_1/music/lobby.mp3')
                mixer.music.play(loops=-1)
            else:
                mixer.music.set_volume(0.2)
                mixer.music.stop()
                mixer.music.unload()
                name=str(Name.get()) #para obtener el nombre del jugador
                money=str(coins)    #para el int en un string
                f=open(user+'/Desktop/proyecto_taller_1/SAVEGAME.txt', 'w') #abre el documento para reescribirlo
                f.write('1'+','+name+','+money+','+s+','+m+','+h+','+points) #agrega un 10 que me va a indicar luego si hay o no una partida guardada, cuando solucione el problema de hacerlo lista ese
                f.close()

                destroy_allR(0,len(maTRooks))
                destroy_allE(0,len(enemigos))

                
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
    f.write('0')
    f.close()
    
#Button
rests=LoadImg('restart.png')
C_root.botn=rests

RESET=Button(C_root, command=reset, image=rests)
RESET.place(x=850, y=570)

about=Button(C_root, command=ventana_about,bg='light blue',fg='black',text='Creditos')
about.place(x=30, y=150)
Ayuda="""
    AYUDA:
    Click izquierdo para seleccionar
    y colocar un rook
    Click derecho para borrar un
    rook o recolectar una moneda
    Se debera defender exitosamente
    de 60 avatars para ganar
    Si un avatar llega al final del
    tablero, usted pierde
    Use las monedas sabiamente"""
C_root.create_text(150,400,font=('Arial', 12),fill='black',text=Ayuda)

EXIT=Button(C_root, command=Exit, bg='white', fg='black', text='Exit')
EXIT.place(x=30, y=20)
def off():
    global oll
    if oll==False:
        mixer.music.pause()
        oll=True

def on():
    global oll
    if oll==True:
        oll=False
        mixer.music.unpause()

Mute=Button(C_root,command=off,bg='white',fg='black',text='Mute')
Mute.place(x=950,y=50)
UnMute=Button(C_root,command=on,bg='white',fg='black',text='Unmute')
UnMute.place(x=950,y=100)


Punts=Button(C_root, command=v_puntajes, bg='yellow',fg='black',text='puntaje')
Punts.place(x=30, y=250)


starto=LoadImg('START.png')
START=Button(C_root,image=starto, command=INICIO)
START.place(x=385, y=490)








root.mainloop()
