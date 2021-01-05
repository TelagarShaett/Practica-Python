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
    
def musica_intro_stop():
    mixer.music.stop()

def espaciado():
    print("\n" * 40)


def anim_menu():

    tiempo = round (time.time(),2)
    limite = tiempo
    retiempo = round((tiempo - limite) , 0)
  
    while(tiempo <= (limite + 15) ):
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
               
        if (retiempo == 15):
            musica_intro_stop()
            
            
musica_intro_start()           
anim_menu()
