# Modules
import os 
import shutil as s

class FileDeletion:
    def __init__(self):
        pass

    def dele(self):
        self.filePath = os.path.exists("Modules\pandas\projects\project_01_csvfile.csv")
        try:
            if not os.path.exists("Modules\pandas\projects\project_01_csvfile.csv"):
                # make folder 
                # os.mkdir("Modules\pandas\projects\project_01_csvfile.csv")

                # make file directory
                with open("Modules\pandas\projects\project_01_csvfile.csv", "w"):
                    pass
                print("Maded directory Successfully!!!")
            else:
                # remove file path
                os.remove("Modules\pandas\projects\project_01_csvfile.csv")

                # remove folder path
                # os.removedirs("Modules\pandas\projects\project_01_csvfile.csv")
                # 
                print("Removed Directory Successfully!!!")
        except Exception as error:
            print(error)

obj = FileDeletion()

if __name__ == "__main__":
    obj.dele()
