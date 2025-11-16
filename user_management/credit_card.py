import random


class Card :
    def __init__(self, number, cvv):
        self.number = number
        self.cvv = cvv

    
    @staticmethod
    def generateCardNumber():
        """
        Generates a random card number for the user.
        It must be validated externally to ensure the card does not already exist in the database.
        """
        number = random.randrange(10**15,10**16-1)
        cvv = random.randrange(10**2,10**3)
        return number, cvv

    