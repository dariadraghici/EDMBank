import random


class Card :
    def __init__(self):
        self.number, self.cvv = Card.generateCardNumber()

    
    @staticmethod
    def generateCardNumber():
        """
        Generate a random card for user. Need to 
        be checked externally if the card doesn't
        exist yet in database.
        """
        number = random.randrange(10**15,10**16-1)
        cvv = random.randrange(10**2,10**3)
        return number, cvv

    