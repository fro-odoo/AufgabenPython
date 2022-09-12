import pickle


class Highscore():
    file_URL = "storage.bin"
    file = lambda self,x: open(self.file_URL,f"{x}b")
    
    
    
    def getStorage(self):
        try:
            return pickle.load(self.file("r"))
        except EOFError:
            return None
    
  
    def sortStorage(self,newVal):
        finalList = []
        print(f"SPLIT: {self.val}")
        
    
    def write(self,val):
        try:
            pickle.dump(" ".join(self.val) + str(val),self.file("w"))
        except EOFError:
            print("ERRORRR")
        except AttributeError:
            print("hier")
            pickle.dump(f"{val}",self.file("w"))
        
    