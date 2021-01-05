from pygame import mixer
from time import sleep
import os
from threading import Thread
import time
import keyboard

def musica_intro_start():
    mixer.init()
    mixer.music.load("C:/Users/Julien/Desktop/Rol/intro.mp3")
    mixer.music.play()
    
def musica_stop():
    mixer.music.stop()

def musica_viaje_start():
    mixer.init()
    mixer.music.load("C:/Users/Julien/Desktop/Rol/viaje.mp3")
    mixer.music.play()

def espaciado():
    print("\n" * 40)


def anim_menu():

    tiempo = round (time.time(),2)
    limite = tiempo
    retiempo = round((tiempo - limite) , 0)
  
    while(tiempo <= (limite + 4) ):
        if (retiempo % 2  == 0):
             with open ("titulo1.txt", "r", encoding="utf8") as file:
                espaciado()
                auto1 = file.read()
                print(auto1)
                sleep(1)

        else:
            with open ("titulo2.txt", "r",encoding="utf8") as file:
                espaciado()
                auto2 = file.read()
                print(auto2)
                sleep(1)
    
        tiempo = round (time.time(),2)
        retiempo = round((tiempo - limite), 0)
               


def introduccion_historia():
    
    espaciado()
    with open ("introhistoria.txt", "r") as file:
        intro = file.read()
        print(intro)

def conversion_atributos():
    
    atributos = creacion_personaje()
    
    nombre = atributos[0]
    edad = int(atributos[1])
    
    if (atributos [2] == "h"):
        sexo = "hombre"
    else:
        sexo = "mujer"
        
    if (atributos[3] == "d"):
        contextura = "delgada"
    elif (atributos[3] == "n"):
        contextura = "normal"
    else:
        contextura = "robusta"
        
    if (atributos[4] == "a"):
        fisico = "atletico"
    elif (atributos[4] == "n"):
        fisico = "normal"
    else:
        fisico = "obeso"
    
    atributos = [nombre, edad, sexo, contextura, fisico]
    
    return(atributos)
        
def creacion_personaje():
    
    print ("\n")
    print("PRIMERO DEBERAS ELEGIR ALGUNOS ATRIBUTOS DE TU PERSONAJE (estoy influiran en el rendimiento de tu personaje. Los mismos podran modificarse mas adelante)")
    print ("\n")
    nombre = input("Cual es tu nombre?: ") 
    edad = input("Cual es tu edad?: ")
    sexo = input ("Es [h]ombre o [m]ujer?: ")
    contextura = input("Su contextura es [d]elgada, [n]ormal o [r]obusta?: ")
    fisico = input("Su fisico es [a]tletico, [n]ormal u [o]beso?: ")
    
    atributos = [nombre, edad, sexo, contextura, fisico]
    
    return(atributos)

def asignacion_atributos_pp():
    
    from objetos import Prota
    from objetos import Stats_iniciales
    atributos = conversion_atributos()  
    stats = asignacion_stats_iniciales(atributos)
    p1 = Prota (atributos[0], atributos[1], atributos[2], atributos[3], atributos[4])
    p2 = Stats_iniciales (stats[0], stats[1], stats[2], stats[3])
    p1.Presentar()
    p2.Mostrar_stat_iniciales()
    explicacion_juego()
    esperar_input()
    
def asignacion_stats_iniciales(atributos):
    #valores default
    
    fuerza = 5
    velocidad = 5
    hambre = 1
    salud = 20
    
    if (atributos[1] <= 18):
        hambre = hambre + 1
    elif (atributos[1] > 18 and atributos[1] <= 35):
        hambre = hambre + 2
        fuerza = fuerza + 1
        salud = salud + 1
    elif (atributos[1] > 35 and atributos[1] <=65):
        hambre = hambre + 1
        fuerza = fuerza - 1
        salud = salud - 2
        
    if (atributos[2] == "h"):
        fuerza = fuerza + 1
        hambre = hambre + 1
    else:
        salud = salud + 2
        
    if (atributos[3] == "d"):
        velocidad = velocidad + 1
        fuerza = fuerza - 1
    elif (atributos[3] == "r"):
        fuerza = fuerza + 1
        hambre = hambre + 1
        velocidad = velocidad - 1
    
    if (atributos[4] == "a"):
        velocidad = velocidad + 2
        fuerza = fuerza + 3
        hambre = hambre + 2
        salud = salud + 5
    elif (atributos [4] == "o"):
        velocidad = velocidad - 1
        fuerza = fuerza + 2
        hambre = hambre + 1
        salud = salud + 3
        
    stats = [fuerza, velocidad, hambre, salud]
    
    return(stats)
                
def explicacion_juego():
    
    with open ("introstats.txt", "r") as file:
        introstats = file.read()
        print("\n")
        print(introstats)

def esperar_input():
    
    while True:  
        try:  
            print ("Apriete `e` para comenzar la supervivencia: ")
            keyboard.wait("e")
            musica_stop()
            break
        except:
            break    
        
def pantalla_carga():
    
    cargas = [1,2]
    numero = 1
    
    while (numero <= 2):
        for x in cargas:
            espaciado()
            with open ("cargando"+ str(x) +".txt", "r") as file:
                carga_anim = file.read()
                print(carga_anim)
                sleep(0.7)
        numero = numero + 1
        
def animacion_viaje():
    
    viajes = [1,2,3,4,5,6,7,8,9,10]
    numero = 0
    musica_viaje_start()
    
    while (numero <= 20):
        for x in viajes:
            espaciado()
            with open ("viaje"+ str(x) +".txt", "r") as file:
                viaje_anim = file.read()
                print(viaje_anim)
                sleep(0.3)
        numero = numero + 1
    
    musica_stop()