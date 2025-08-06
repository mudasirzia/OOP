import os


class Data:
    def __init__(self):
        self._name = input("Enter the name:\t")
        self._fatherName = input("Enter the father name:\t")
        self._cnicNumber = int(input("Enter the CNIC number:\t"))

    def make_file(self):
        try:
            if not os.path.exists("Modules/os/raf/new_folder.py"):
                os.mkdir("Modules/os/raf/new_folder.py")
                print("File is maded Successfully!!!")
            else:
                raise "File is Already exists!!!"
        except Exception as error:
            raise error

    def save_data(self):
        pass




obj = Data()


if __name__ == "__main__":
    obj.make_file()
