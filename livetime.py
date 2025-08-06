# Modules
from datetime import datetime as dt
import time as t 

class LiveTime:
    def __init__(self):
        pass

    def main(self):
        self.today = dt.now()
        self.livetime = self.today.strftime("%I:%M:%S %p")
        print(f"\rCurrent Time: {self.livetime}",flush=True,end=" ")

obj = LiveTime()

if __name__ == "__main__":
    while (True):
        obj.main()
        t.sleep(1)
        