import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import os
import re 
from ui_utils import get_resource_path

class EDMBankProfile:
    def __init__(self, parent_frame, current_user, bank_service, switch_view_callback, ui_helper, app_instance=None):
        self.parent_frame = parent_frame
        self.user = current_user
        self.bank_service = bank_service
        self.switch_view_callback = switch_view_callback
        self.ui = ui_helper
        self.app_instance = app_instance
        
       
        # tkinter variables for input fields
        self.username_var = tk.StringVar(value=self.user.credentials.username)
        self.email_var = tk.StringVar(value=self.user.credentials.email)
        
        # variables for image
        self.profile_image_path = get_resource_path("profile_placeholder.png") 
        self.profile_photo_tk = None 
        
        self._set_styles()
        self.create_profile_view()

    # ------------------------------------------------------------------------------

    def _set_styles(self):
        style = ttk.Style()
        style.configure('Profile.TLabel', background='#cad2c5', foreground='#354f52', font=self.ui.get_font('Tex Gyre Chorus', 20, 'bold'))
        style.configure('Profile.TEntry', font=self.ui.get_font('Courier', 14), fieldbackground='white')
        style.configure('Profile.TButton',background="#9db3a7", foreground='#2f3e46', font=self.ui.get_font('Courier', 16, 'bold'), padding=self.ui.w_pct(0.5))

        # action button (SAVE)
        style.configure('Action.TButton', foreground='white', background='#52796f', font=self.ui.get_font('Courier', 18, 'bold'), padding=self.ui.w_pct(1))
        style.map('Action.TButton', background=[('active', '#84a98c')])
        
        # exit button
        style.configure('Exit.TButton', foreground='white', background='#354f52', font=self.ui.get_font('Courier', 18, 'bold'), padding=self.ui.w_pct(1))
        style.map('Exit.TButton', background=[('active', '#2f3e46')])

    # ------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------

    def create_profile_view(self):
        
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
            
        main_content = tk.Frame(self.parent_frame, bg="#cad2c5", padx=self.ui.w_pct(2), pady=self.ui.h_pct(2))
        main_content.pack(fill='both', expand=True)

        tk.Label(main_content, text="MY PROFILE", font=self.ui.get_font('Arial', 32, 'bold'),
                 bg='#cad2c5', fg='#2f3e46').pack(pady=(self.ui.h_pct(2), self.ui.h_pct(6)))
        
        details_frame = tk.Frame(main_content, bg="#cad2c5")
        details_frame.pack(fill='x', pady=self.ui.h_pct(1))
        
        # configure columns for image (left) and fields (right)
        details_frame.grid_columnconfigure(0, weight=1) 
        details_frame.grid_columnconfigure(1, weight=3) 

        # profile picture section
        img_size = self.ui.get_size(150)
        self.image_canvas = tk.Canvas(details_frame, width=img_size, height=img_size, bg="lightgray", highlightthickness=0, borderwidth=2, relief='groove')
        self.image_canvas.grid(row=0, column=0, padx=self.ui.w_pct(1), pady=self.ui.h_pct(1), sticky='n')
        self.load_profile_image() 
        
        ttk.Button(details_frame, text="Change Picture", command=self.change_profile_picture,
                   style='Profile.TButton').grid(row=1, column=0, padx=self.ui.w_pct(1), pady=self.ui.h_pct(0.5), sticky='n')

        fields_frame = tk.Frame(details_frame, bg="#cad2c5")
        fields_frame.grid(row=0, column=1, rowspan=2, padx=self.ui.w_pct(1), sticky='nsew')
        fields_frame.grid_columnconfigure(1, weight=1)
        
        self.username_entry = self._create_field(fields_frame, "Username:", self.username_var, 0, readonly=True)
        self.username_entry.config(font=self.ui.get_font("Courier", 16))

        # email is read-only
        self._create_field(fields_frame, "Email:", self.email_var, 1, readonly=True).config(font=self.ui.get_font("Courier", 13))
        
        ttk.Button(fields_frame, text="Change Password", command=self.change_password_popup,
                   style='Profile.TButton').grid(row=2, column=0, columnspan=2, pady=self.ui.h_pct(1.5), sticky='ew', padx=self.ui.w_pct(1))

        button_frame = tk.Frame(main_content, bg='#cad2c5')
        button_frame.pack(pady=self.ui.h_pct(2), fill='x')
        
        ttk.Button(button_frame, text="EXIT", command=self.exit_view,
                   style='Exit.TButton').pack(side='right', fill='x', expand=True, padx=self.ui.w_pct(1))
    
    # ------------------------------------------------------------------------------

    def _create_field(self, parent, label_text, textvariable, row, readonly=False):
        ttk.Label(parent, text=label_text, style='Profile.TLabel').grid(row=row, column=0, padx=self.ui.w_pct(1), pady=self.ui.h_pct(0.5), sticky='w')
        entry = ttk.Entry(parent, textvariable=textvariable, style='Profile.TEntry')
        if readonly:
            entry.config(state='readonly')
        entry.grid(row=row, column=1, padx=self.ui.w_pct(1), pady=self.ui.h_pct(0.5), sticky='ew')
        return entry
    
    # ------------------------------------------------------------------------------

    def load_profile_image(self):
        try:
            img_size = self.ui.get_size(150)
            if os.path.exists(self.profile_image_path):
                original_image = Image.open(self.profile_image_path)
            else:
                # placeholder image if file not found
                original_image = Image.new('RGB', (img_size, img_size), color='#52796f') 
                
            resized_image = original_image.resize((img_size, img_size), Image.LANCZOS)
            self.profile_photo_tk = ImageTk.PhotoImage(resized_image)
            self.image_canvas.create_image(img_size//2, img_size//2, image=self.profile_photo_tk, anchor='center')
        except Exception:
            # fallback text if image loading fails
            img_size = self.ui.get_size(150)
            self.image_canvas.create_text(img_size//2, img_size//2, text="No Picture", fill='#2f3e46', font=self.ui.get_font('Arial', 14))

    # ------------------------------------------------------------------------------

    def change_profile_picture(self):
        messagebox.showinfo("Change Picture", 
                            "The profile picture upload functionality is not implemented (it would require a file dialog).", 
                            parent=self.parent_frame)

    # ------------------------------------------------------------------------------

    def change_password_popup(self):
            
        pwd_window = tk.Toplevel(self.parent_frame)
        pwd_window.title("Change Password")
        pwd_window.configure(bg='#cad2c5')
        pwd_window.geometry("350x250")
        pwd_window.transient(self.parent_frame) # keep pop-up on top
        pwd_window.grab_set() # modal behavior
        
        # center the pop-up window over the parent
        self.parent_frame.update_idletasks()
        x = self.parent_frame.winfo_rootx() + (self.parent_frame.winfo_width() // 2) - 175
        y = self.parent_frame.winfo_rooty() + (self.parent_frame.winfo_height() // 2) - 125
        pwd_window.geometry(f"+{x}+{y}")

        frame = tk.Frame(pwd_window, bg='#cad2c5', padx=10, pady=10)
        frame.pack(expand=True, fill='both')
        frame.grid_columnconfigure(1, weight=1)
        
        # helper to create password fields
        def create_pwd_field(parent, label_text, row):
            tk.Label(parent, text=label_text, bg='#cad2c5', fg='#354f52', font=('Arial', 10, 'bold')).grid(row=row, column=0, sticky='w', pady=5)
            entry = tk.Entry(parent, show="*", font=('Arial', 12))
            entry.grid(row=row, column=1, sticky='ew', padx=(5,0), pady=5)
            return entry

        old_pwd_entry = create_pwd_field(frame, "Current Password:", 0)
        new_pwd_entry = create_pwd_field(frame, "New Password:", 1)
        confirm_pwd_entry = create_pwd_field(frame, "Confirm New Password:", 2)
        
        # save password logic
        def save_new_password():
            old_pwd = old_pwd_entry.get()
            new_pwd = new_pwd_entry.get()
            confirm_pwd = confirm_pwd_entry.get()
            
            if not old_pwd or not new_pwd or not confirm_pwd:
                messagebox.showerror("Error", "Please fill in all fields.", parent=pwd_window)
                return

            if new_pwd != confirm_pwd:
                messagebox.showerror("Error", "The new password and confirmation do not match.", parent=pwd_window)
                return
            
            try:
                self.bank_service.change_password(self.user, old_pwd, new_pwd)
                messagebox.showinfo("Success", "Password successfully changed!", parent=self.parent_frame)
                pwd_window.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e), parent=pwd_window)
                old_pwd_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}", parent=pwd_window)

        button_frame = tk.Frame(frame, bg='#cad2c5')
        button_frame.grid(row=3, column=0, columnspan=2, pady=15)
        
        tk.Button(button_frame, text="SAVE", command=save_new_password, bg='#52796f', fg='white', font=('Arial', 10, 'bold')).pack(side='left', padx=10)
        tk.Button(button_frame, text="CANCEL", command=pwd_window.destroy, bg='#354f52', fg='white', font=('Arial', 10)).pack(side='left', padx=10)

    # ------------------------------------------------------------------------------

    def exit_view(self):
        self.switch_view_callback("home")