import time
from time import sleep

def crono():

    tiempo = round (time.time(),2)
    limite = tiempo
    retiempo = round((tiempo - limite) , 0)
   


    while(tiempo < (limite + 25) ):
        if (retiempo % 2  == 0):
            print ("par")
            print(retiempo)
            print(tiempo)
            print(time.time())
            sleep(1)

        else:
            print ("impar")
            print(retiempo)
            print(tiempo)
            print(time.time())
            sleep(1)
    
        tiempo = round (time.time(),2)
        retiempo = round((tiempo - limite), 0)
        
  
crono()