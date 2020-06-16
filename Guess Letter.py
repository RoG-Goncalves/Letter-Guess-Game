class Game:
    
    number_of_attempts = 3
    no_more_attempts = "Game Over"

    def attempt_down(self): #This will work as the counter of remaining lives.
        self.number_of_attempts -= 1
        print('Remaining Lives:',self.number_of_attempts)
    def check_guess(self,letter): 
        """
        Requires
        letter - a letter that has to be guessed
        guess - a input from the user with the guessed letter
        """ 
        while self.number_of_attempts > 0:
            guess = input ("Guess the letter: ")
            if guess.isalpha() == False:
                print("Invalid!")  
            elif guess.lower() < letter:
                self.attempt_down()
                print("Low") 
                print("Try Again!")  
            elif guess.lower() > letter:
                self.attempt_down()
                print("High")  
                print("Try Again!")
            elif guess.lower() == letter:
                print("Correct!")
                return True
                
        print (self.no_more_attempts)
        return False    


game = Game()
"""   
This is used to run the game. 
Just insert the letter that 
has to be guessed.
"""
teste1 = game.check_guess('g')
teste2 = game.check_guess('r')
