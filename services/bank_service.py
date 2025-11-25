from DataBase.DataBase import Database
from user_management.user import User
from exceptions import *

class BankService:
    def __init__(self, db: Database):
        self.db = db

    def transfer_money(self, sender: User, receiver: User, amount: float):
        if (sender.balance < amount):
            raise InsufficientFundsError(f"Insuficient funds: {sender.balance}$ < {amount}$")
        
        sender.balance -= amount
        receiver.balance += amount
        self.db.modify_user(sender)
        self.db.modify_user(receiver)

    def withdraw(self, user: User, amount: float):
        if (user.balance < amount):
            raise InsufficientFundsError(f"Insuficient funds: {user.balance}$ < {amount}$")
        
        user.balance -= amount
        self.db.modify_user(user)

    def add_money(self, user: User, amount: float):
        user.balance += amount
        self.db.modify_user(user)

    def add_user(self, user:User):
        try:
            self.db.get_user(user.credentials.username)
            return False
        except AccountNotFoundError:
            self.db.add_user(user)
            return True
        

    