class ToDoList:
    def __init__(self):
        self.store = []
        # self.ti = int(
        #     input("Enter your choice (1,2,3)\t"))
        # self.exiting = input('Enter \"q\" to exit:\t').lower()

    # main options for user
    def options(self):
        ol = ["adding", "removing", "view"]
        for index, ul in enumerate(ol, start=1):
            print(f"{index}.{ul}")

    def main(self):

        """ 

        main() ==> method
        Use ==> add,remove,and view ==> in list

        """

        # main.store list
        # apply conditions
        while (True):
            self.ti = int(input("Enter your choice (1,2,3):\t"))
            try:
                if self.ti == 1:
                    self.add()
                    print("Item added successfully!!!")
                elif self.ti == 2:
                    self.rm()
                    print("Item removed!!!")
                elif self.ti == 3:
                    self.view()
                else:
                    raise "Invalid option"
            except Exception as error:
                print(error)

    # take input from user

    def takeInput(self):
        """ 
        takeInput() ==> method
        Use ==> take input ==> exit

        """

    # adding item in list
    def add(self):
        """ 

        add() ==> method
        Use ==> add item in list

        """

        self.a = input("Enter item:\t")
        self.store.append(self.a)
        print(f"item \"{self.a}\" is added successfully!!!")

    # Remove item from list
    def rm(self):
        self.b = int(input("Enter the index to remove:\t"))
        self.store.pop(self.b - 1)
        print(f"Item {self.b} is removed Successfully!!!")

    # View items in list
    def view(self):
        """ 

        view() ==> method
        using loop ==> view all items in list

        """
        print("Your Items is:")
        for self.i , self.j in enumerate(self.store, start=1):
            print(f"{self.i}.{self.j}")


tdl = ToDoList()

if __name__ == "__main__":
    while (True):
        permission = input("Do you want to continue (y/n):\t").lower()
        try:
            if permission == "n":
                break
            else:
                tdl.options()
                tdl.main()
        except Exception as error:
            print(error)
