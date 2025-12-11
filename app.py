import sys
import os
import tkinter as tk


current_dir = os.path.dirname(os.path.abspath(__file__))
ui_dir = os.path.join(current_dir, 'UI')
sys.path.append(ui_dir)

from DataBase.DataBase import Database
from services.bank_service import BankService
from UI.EDMBank_launcher import run_login_app

if __name__ == "__main__":
    db = Database()
    bank_service = BankService(db)
    
    root = tk.Tk()
    
    run_login_app(root, bank_service)
    
    root.mainloop()
