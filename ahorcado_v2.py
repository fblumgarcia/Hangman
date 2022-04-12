from encodings import utf_8
from os import system
from secrets import choice
import time
import random

def readData():
    words = [] 
    with open("./archivos/data.txt", "r", encoding="utf_8") as f: #Abre el archivo como lectura
        for word in f:
            words.append(str(word)) #Se añade a una lista
    return choice(words) # escoje una palabra aleatoria

def play():
    word = readData().upper() #llama la función leer 
    print(word)
    downG = ["_" for i in range(len(word)-1)] #imprime todos los _ con la cantidad de letras
    full=0
    while(full != 5):
        time.sleep(2)
        system("cls")  
        print(" ".join(downG)) #Une los _ para verse más estético
        wordUser = input("Ingrese una letra: ").upper()
        if wordUser.isalpha() and len(wordUser)==1: #es alfabeto y tiene un elemento
            if wordUser in word: #Comprueba que la letra este dentro de la palabra
                count = word.count(wordUser) #Cuantas veces esta dentro de la palabra
                print("La letra " + wordUser + " esta "+ str(count) + " veces.")
                j = 0 # Un contador para ubicar la letra donde es
                for i in word: # ciclo que ubica como es
                    print(j)
                    if i == wordUser:
                        downG[j] = wordUser                        
                    j = j + 1
            else:
                print("No esta la letra " + wordUser)
        else:
            print("Ingrese una sóla letra")
            
        
        
        
        

def menu():
    print("¡¡¡Bienvenido!!! al juego del ahorcado por fblumgarcia".center(60, " "))
    option = 9
    while(option != 2): #Para hacer que el menú corra indefinidamente
        time.sleep(2) #Tiempo de espera de 2 s
        system("cls") # Borra lo de la pantalla
        print("\n 1. Jugar \n 2. Salir \n")
        try: # Esto sirve para restringir la entrada de sólo números 
            option = int(input("Seleccione una opción: "))
            if option == 1:
                play() #Abre la función jugar
            elif option == 2:
                option = 2
            else:
                print("Ingrese una opción correcta")
        except ValueError:
            print("Ingrese sólo números")        
    print("¡¡¡Espero te haya gustado el juego!!!".center(60, " ")) 

def main():
    menu()

if __name__ == "__main__":
    main()