import os
import shutil as s


# parent class
class FileHandling:
    def __init__(self):
        print(
            """ 
              ========== Wellcome ==========
              """
        )

        self.options = ["File Making", "File Deletion", "File Renaming", "Exit"]
        for i, o in enumerate(self.options, start=1):
            print(f"{i}.{o}")

        # pass

    # def showdisplay(self):


# take input
class TakeInput(FileHandling):
    def __init__(self) -> int:
        super().__init__()
        self.takeoption = int(input("Enter the option (1/2/3/4):\t"))
        return self.takeoption

    # child class  also parent for below

# file making
class FileMaking(TakeInput):
    def __init__(self):
        super().__init__()
        try:
            if self.takeoption == 1:
                self.foldername = input("Enter the folder name:\t")
                self.filename = input("Enter file name:\t")
        except Exception as error2:
            raise error2

    def filemaking(self):
        try:
            if os.path.exists(self.foldername):
                with open(f"{os.path.join(self.foldername, self.filename)}", "w") as f:
                    f.write("Hello, the file is madded Successfully!!!")
                print("File madedd Successfully!!!")
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            raise FileNotFoundError


#file deletion
class FileDeletion(FileMaking):
    def __init__(self):
        super().__init__()
        try:
            if self.takeoption == 2:
                self.foldername = input(
                    "Enter the folder name to delete in which file:\t"
                )
                self.filename = input(
                    f"Enter the file name in {self.foldername} to delete:\t"
                )
        except FileNotFoundError:
            print("Invalid option choosen!!!")

    def filedeleting(self):
        path = os.path.join(self.foldername, self.filename)
        try:
            if os.path.exists(f"{path}"):
                os.remove(path)
                print("File deleted Successfully!!!")
        except FileNotFoundError:
            print("file path not found!!!")


# file renaming
class FileRenaming(FileDeletion):
    def __init__(self):
        super().__init__()
        try:
            if self.takeoption == 3:
                self.foldername = input("folder name:\t")
                self.oldfilename = input(
                    f"Enter the file name inside {self.foldername}:\t"
                )
                self.newfilename = input(
                    f"Enter the new name for {self.oldfilename}:\t"
                )
        except Exception as error3:
            raise error3

    def filerenaming(self):
        try:
            self.oldpath = os.path.join(self.foldername, self.oldfilename)
            self.newpath = os.path.join(self.foldername, self.newfilename)

            if os.path.exists(self.oldpath):
                os.replace(self.oldpath, self.newpath)
                print(f"From {self.oldpath} to {self.newpath}")
        except FileExistsError:
            raise FileExistsError

# main handler of all methods
def main():
    while True:
        o = FileRenaming()
        try:
            if o.takeoption == 1:
                o.filemaking()
            elif o.takeoption == 2:
                o.filedeleting()
            elif o.takeoption == 3:
                o.filerenaming()
            else:
                print("Thanks for Comming!!!")
                break
        except Exception as error:
            raise error


if __name__ == "__main__":
    main()
