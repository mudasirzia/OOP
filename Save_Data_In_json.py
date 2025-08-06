import os 
import json

class StudentData:
    def __init__(self):
        self.FileLocation = "!!!!====give file location first then execute it====!!!!"
        self.EmptyList = []

        # check if file not exist 
        try:
            if not os.path.exists("!!!!====give file location first then execute it====!!!!"):
                
                # create new file with empty list in it
                with open("!!!!====give file location first then execute it====!!!!","w") as f:
                    json.dump([],f)
            else:
                raise "File is already exists!!!"
        except FileExistsError:
            raise FileExistsError
                    
    def takedata(self):
        while (True):
            self.studentname = input("Enter the studentname or type(\"q\" to exit):\t")
            if self.studentname.lower() == "q":
                break
            self.fname = input("Enter the father name:\t")
            
            # dictionary 
            studentdata = {
                "Name":self.studentname,
                "Father Name":self.fname
            }
            
            # append
            self.EmptyList.append(studentdata)
            self.savedata()
            print("Data saved successfully!!!")
        
    
    def savedata(self):
        with open(self.FileLocation,"w") as f:
            json.dump(self.EmptyList, f, indent=5)
    

obj = StudentData()


if __name__ == "__main__":
    obj.takedata()

