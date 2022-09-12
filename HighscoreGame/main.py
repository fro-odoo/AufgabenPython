import random
import time
import pickle
import sys
import highscore
import game

while True:
    hs = highscore.Highscore()   
    eingabe = input("Bitte eingeben (0:Ende, 1:Highscores, 2:Spielen)")
    if eingabe == "0":
        sys.exit()
    elif eingabe == "1": 
        ### highscore liste
        print(hs.getStorage())  
    elif eingabe == "2":
        while True:
            name = input("Bitte geben Sie ihren Namen ein (max 10 Zeichen)").title()
            if len(name) <= 10:
                break
        gameObj = game.Game(name)
        result = gameObj.start()
        if result != None:
            nameZeit = result
            hs.write(nameZeit)
            hs.sortStorage(nameZeit)
            
            
            
    
    

