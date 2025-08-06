# modules
import os
import json


class ToDoList:
    def __init__(self):
        self.STORE = []

    def showOption(self):
        print("< ==== Your Options to choose ==== >")
        self.options = ["Add", "Delete", "Show", "Exit", "save"]
        for i, n in enumerate(self.options, start=1):
            print(f"{i}.{n}")


class TakeInput(ToDoList):
    def __init__(self):
        super().__init__()
        self.chooseOption = " "

    def takeinput(self):
        self.chooseOption = int(input("Enter the option (1/2/3/4):\t"))
        if self.chooseOption:
            return self.chooseOption
        else:
            raise "Invalid option choosen"


class AddItem(TakeInput):
    def __init__(self):
        super().__init__()
        self.addinputitem = ""

    def add(self):
        try:
            if self.chooseOption == 1:
                self.addinputitem = input("Enter the item to add:\t")
                self.STORE.append(self.addinputitem)
                print(f'"{self.addinputitem}" Added Successfully!!!')
            else:
                print("invalid choosen option!!!")
        except Exception as error:
            raise error


class DeleItem(AddItem):
    def __init__(self):
        super().__init__()
        self.reminputitem = ""

    def dele(self):
        try:
            if self.chooseOption == 2:
                self.reminputitem = input("Enter the item to remove:\t")
                self.STORE.remove(self.reminputitem)
                print(f'"{self.reminputitem}" Removed Successfully!!!')
            else:
                raise "option choosen error!!!"
        except Exception as error2:
            raise error2


class ShowItem(DeleItem):
    def __init__(self):
        super().__init__()
        pass

    def show(self):
        try:
            if self.chooseOption == 3:
                print("< ==== Your Items in stored ==== >")
                for j, k in enumerate(self.STORE, start=1):
                    print(f"{j}.{k}")
            else:
                "opotion choosen error!!!"
        except Exception as error3:
            raise error3


class SaveData(ShowItem):
    def __init__(self):
        super().__init__()
        pass
        #

    def load(self):
        try:
            if os.path.exists(f"{self.folderloc}/{self.fileloc}.json"):
                with open(self.fileloc, "r") as f:
                    return json.load(f)
            else:
                if os.path.exists(self.folderloc):
                    with open(f"{self.folderloc}/{self.fileloc}.json","w") as f:
                        json.dump(self.STORE, f)
                print("File location is madded successfully!!!")
        except Exception as error6:
            raise error6

    def save(self):
        try:
            self.folderloc = input("Enter the complete folder name (Auto)\t")
            self.fileloc = input("Enter the complete file name (Auto)\t")

            if os.path.exists(f"{self.fileloc}/{self.fileloc}.json"):
                with open(f"{self.fileloc}/{self.fileloc}.json", "w") as f:
                    json.dump(self.STORE, f)
            else:
                os.mkdir(self.folderloc)
                if os.path.exists(self.folderloc):
                    with open(f"{self.folderloc}/{self.fileloc}.json", "w") as f:
                        json.dump(self.STORE, f)
                    print("File madded successfully!!!")
        except FileExistsError:
            print("file not exist!!!")


o = SaveData()


def main():
    while True:
        o.takeinput()
        try:
            if o.chooseOption == 1:
                o.add()
            elif o.chooseOption == 2:
                o.dele()
            elif o.chooseOption == 3:
                o.show()
            elif o.chooseOption == 5:
                o.save()
                o.load()
            else:
                print("Thanks for comming!!!")
                break
        except Exception as error4:
            raise error4

if __name__ == "__main__":
    o.showOption()
    main()









