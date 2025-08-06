import random as random
class NumberGuessGame:
    """
    class name ==> NumberGuessGame
     
     """

    def __init__(self):
        """

        __int__ ==> method  
        return ==> None
        give ==> random number between 1,10
        
        """
        self.computer_guess = random.randint(1,10)

    # main 
    def main(self):
        """ 

        main() ==> method
        parameters ==> 1
        take ==> number in (int)
        from ==> user
        
        """

        while (True):
            self.computer_guess = random.randint(1,10)
            self.user_guess = input("Try to guess the number:\t")
            self.user_guess = int(self.user_guess)
            try:
                if self.computer_guess == self.user_guess:
                    print("You Guess the number")
                elif self.computer_guess > self.user_guess:
                    print("Too low guess")
                elif self.computer_guess < self.user_guess:
                    print('Too high guess')
                else:
                    print(SyntaxError)
            except Exception as error:
                print(error)

game = NumberGuessGame()

if __name__ == "__main__":
        game.main()
    