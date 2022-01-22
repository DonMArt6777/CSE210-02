
import random

class Card:

    """display the cards randomly way.
    
    Atributes:
    value (int): the number guess
    points (int): the number points to track."""
    

    def __init__(self):
        self.newNum=True
        self.value=0
        

    
    def newCard(self):
        """Generates a new number"""
        self.value = random.randint(1, 13)
        print(f"The card is: {self.value}")
    
    def nextCard(self):
        self.value = random.randint(1, 13)
        print(f"Next card was:{self.value}")