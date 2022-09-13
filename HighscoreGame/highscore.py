import pickle


class Highscore():
    file_URL = "storage.bin"
    file = lambda self,x: open(self.file_URL,f"{x}b")
    
    
    
    def getStorage(self):
        try:
            return pickle.load(self.file("r"))
        except:
            return None
    
  
    def sortStorage(self,newVal):
        if self.getStorage() == None:
            print("hier")
        else: 
            return newVal
        
        
    
    def write(self,val):
        pickle.dump(val,self.file("w"))
      
    