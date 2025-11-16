from .user_credentials import UserCredentials
from .payment_details import PaymentsHistory
from.credit_card import Card

class User:
    def __init__(self, credentials: UserCredentials, balance: int, payment_history: PaymentsHistory, card: Card):
        self.credentials = credentials
        self.balance = balance
        self.payment_history = payment_history
        self.card = card
        