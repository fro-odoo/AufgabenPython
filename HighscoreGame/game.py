import time
import random

class Game:
    def __init__(self,name):
        self.name = name
    
    def start(self):
        pre = time.time()
        
        solved = 0
        ziel = 1
        
        
        while solved < ziel:
            op = random.choice(["+","-"])
            summand1 = random.randint(1,50)
            summand2 = random.randint(1,50)
            expr = str(summand1) + op + str(summand2) 
            print(expr)
            eingabe = input()
            try:
                if int(eingabe) == int(eval(expr)):
                    print("***RICHTIG***")
                    solved += 1
                    print(f"Gelöst: {solved}/{ziel} (exit zum verlassen)")
                else:
                    print("***FALSCH***")
            except ValueError:
                if eingabe == "exit":
                    break
                print("Ungültige Eingabe")
                continue
        
        if solved == ziel:
            return f"{self.name} {round(time.time() - pre,3)}"
        return None