import tkinter as tk
from EDMBank_login import EDMBankLogin
from EDMBank_main import EDMBankApp

def start_main_app(username, login_window):
    # get the position and size of the login window before destroying it
    login_window.update_idletasks()
    # x is the distance from the left edge of the screen
    x = login_window.winfo_x()
    # y is the distance from the top edge of the screen
    y = login_window.winfo_y()
    # width is the width of the login window
    width = login_window.winfo_width()
    # height is the height of the login window
    height = login_window.winfo_height()
    
    # destroy the login window
    login_window.destroy()
    
    # create a new main window in the EXACT same position and size
    main_root = tk.Tk()
    main_root.geometry(f"{width}x{height}+{x}+{y}")
    main_root.minsize(300, 500)
    
    # start the main app
    app = EDMBankApp(main_root)
    # set the logged in user
    app.logged_in_user = username
    # update the card display for the logged in user
    app.update_card_display()
    main_root.mainloop()

# entry point
if __name__ == "__main__":
    root = tk.Tk()
    login_app = EDMBankLogin(root, start_main_app)
    root.mainloop()