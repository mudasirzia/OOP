
# Modules
import pandas as pd


class StudentData:
    def __init__(self):
        # Students data
        self.StudentData = {
            "Names": ["umer", "ahsan", "abdullah", "ahmed", "ahsaan", "muhammad", "waseem", "naseem", "ashfaak", "malik"],
            "Phy": [35, 45, 48, 50, 60, 10, 15, 92, 81, 71],
            "Chem": [35, 45, 48, 50, 60, 10, 15, 92, 81, 71],
            "Bio": [35, 45, 48, 50, 60, 10, 15, 92, 81, 71],
            "Isi": [35, 25, 29, 30, 35, 38, 41, 45, 48, 49],
            "M.Pak": [35, 25, 29, 30, 35, 38, 41, 45, 48, 49],
            "Maths": [35, 45, 48, 50, 60, 10, 15, 92, 81, 71]
        }

    # DatFrame
    def df(self) -> object:
        self.sdf = pd.DataFrame(self.StudentData)
        return self.sdf

    # save in file
    def save(self):
        self.fileCategory = self.sdf.to_csv(
            "Modules/pandas/projects/project_01_csvfile.csv", index=False)
        return self.fileCategory

    # head()
    def had(self):
        self.h = self.sdf.head(5)
        return self.h

    # tail()
    def tal(self):
        self.t = self.sdf.tail(5)
        return self.t
    
    # describe()
    def desc(self):
        self.d = self.sdf.describe()
        return self.d

obj = StudentData()

if __name__ == "__main__":
    # making data frame
    print("This is your student data")
    p = obj.df()
    print(p)

    # save in csv file dataframe
    print("saving in csv file...")
    p2 = obj.save()

    # head()
    print("this is starting students")
    ph = obj.had()
    print(ph)

    # tail()
    print("This is last 5 students")
    pt = obj.tal()
    print(pt)

    # describe()
    print("This is describe()")
    ppd = obj.desc()
    print(ppd)