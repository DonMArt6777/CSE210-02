from card import Card

class Director:
    def __init__(self):
        self.card = Card
        self.userGuess = ""
        self.isPlaying = True

    def askToGuess(self):
        self.userGuess = input("Higher or lower? [h/l]: ")

    def startGame(self):
        while self.isPlaying:
            Card.newCard(self)
            self.askToGuess()
            Card.nextCard(self)
            self.earn_points()
            self.getInputs()


    def getInputs(self):
        """Ask the user if they want to roll.
        Args:
            self (Director): An instance of Director.
        """
        playAgain = input("Play again? [y/n]: ")
        if playAgain == "y":
            self.isPlaying 
        elif playAgain =="n":
            print ("Thank you. Good bye!")
            self.isPlaying = False
        else:
            print("wrong command, bye!")
            self.isPlaying = False
            
    def earn_points(self):
        self.score = 300
        if self.userGuess =="h" and self.value > 5:
          self.score+=100
          print(f"Your score is: {self.score}")
        elif self.userGuess == "l" and self.value < 5:
            self.score+=100
            print(f"Your score is: {self.score}")
        elif self.userGuess == "h" and self.value < 5:
            self.score-=75 
            print(f"Your score is: {self.score}")
        elif self.userGuess == "l" and self.value > 5:
            self.score-=75
            print(f"Your score is: {self.score}")
        else:
            print("you have lost!")



