import random
from datetime import datetime

class Card :
    def __init__(self, number, cvv, expiry_date, IBAN):
        self.number = number
        self.cvv = cvv
        self.expiry_date = expiry_date
        self.IBAN = IBAN

    
    @staticmethod
    def generateCard():
        """
        Generates a random card for the user.
        It must be validated externally to ensure the card does not already exist in the database.
        """
        # Card number (16 digits)
        number = random.randrange(10**15, 10**16)

        # CVV (3 digits)
        cvv = random.randrange(100, 1000)

        # Expiry date
        current_year = datetime.now().year
        rand_year = random.randrange(current_year + 1, current_year + 20)
        rand_month = random.randrange(1, 13)

        expiry_date = f"{rand_month:02d}/{rand_year % 100:02d}"

        # IBAN
        # Generating a 24-character IBAN (RO + 2 check digits + 4 bank code + 16 account digits)
        # Bank Code for EDM Bank: EDMB
        check_digits = f"{random.randrange(10, 99)}"
        account_digits = f"{random.randrange(10**15, 10**16)}" # 16 digits
        IBAN = f"RO{check_digits}EDMB{account_digits}"

        return Card(number, cvv, expiry_date, IBAN)

    