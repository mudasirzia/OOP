class Calculator:
    def __init__(self):
        pass
    # main
    def main(self):
        

        while (True):
            self.n = int(input("Enter num1:\t"))
            self.op = input("Enter the operator (+, -, *, /):\t")
            self.m = int(input("Enter num2:\t"))
            try:
                if self.op == "+":
                    self.sum()
                    continue

                if self.op == "-":
                    self.sub()
                    continue

                if self.op == "*":
                    self.mul()
                    continue

                if self.op == "/":
                    self.div()
                    continue

            except SyntaxError:
                raise SyntaxError

    # sum
    def sum(self):
        s = self.n + self.m
        print(s)
        return s 

    # subtract
    def sub(self):
        try:
            if self.m < self.n:
                s = self.n - self.m
                print(s)
                return s
            raise ValueError
        except Exception as error:
            print(error)
    
    # multiply
    def mul(self):
        m = self.n * self.m
        print(m)
        return m 

    # divide
    def div(self):
        try:
            if self.n == 0 or self.m == 0:
                return 0
            self.n / self.m
        except ZeroDivisionError:
            raise ZeroDivisionError

obj = Calculator()

if __name__ == "__main__":
    # while (True):
    obj.main()
