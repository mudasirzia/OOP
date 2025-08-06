import pyttsx3 as p 

class Voice:
    def __init__(self):
        self.txt = input("Enter something..\t")
        self.engineActivate = p.init() # initialize engine


class Taketxt(Voice):
    def __init__(self):
        super().__init__()
        pass 
    
    def makeVoice(self):
        self.voice = self.engineActivate.say(self.txt)
        self.engineActivate.runAndWait()
        return self.voice


if __name__ == "__main__":
    while (True):    
        o = Taketxt()
        o.makeVoice()
    