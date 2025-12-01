import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import os

class EDMBankSettings:
    def __init__(self, parent_frame, logged_in_user, logged_in_email, switch_view_callback, ui_helper):
        self.parent_frame = parent_frame
        self.logged_in_user = logged_in_user.upper() 
        self.logged_in_email = logged_in_email 
        self.switch_view_callback = switch_view_callback
        self.ui = ui_helper
        
        # initial data
        self.last_name, self.first_name = self._split_name(self.logged_in_user)
        # placeholder for the account creation date as requested
        self.account_creation_date = "2025-11-15" 
        
        # variables for image (to maintain the profile picture on the left)
        self.profile_image_path = "profile_placeholder.png" 
        self.profile_photo_tk = None 
        
        self._set_styles()
        self.create_settings_view()

    # ------------------------------------------------------------------------------

    def _set_styles(self):
        style = ttk.Style()
        style.configure('SettingsTitle.TLabel', background='#cad2c5', foreground='#354f52', font=self.ui.get_font('Tex Gyre Chorus', 25, 'bold'))
        style.configure('SettingsData.TLabel', background='#cad2c5', foreground='#2f3e46', font=self.ui.get_font('Courier', 20))

        # RED DELETE button style for account deletion
        style.configure('Delete.TButton', foreground='white', background='#a90000', font=self.ui.get_font('Courier', 20, 'bold'), padding=self.ui.w_pct(2))
        style.map('Delete.TButton', background=[('active', '#ff6666')])
        
        # exit button
        style.configure('Exit.TButton', foreground='white', background='#354f52', font=self.ui.get_font('Courier', 20, 'bold'), padding=self.ui.w_pct(2))
        style.map('Exit.TButton', background=[('active', '#2f3e46')])

    # ------------------------------------------------------------------------------

    def _split_name(self, full_name):
        parts = full_name.split()
        if len(parts) >= 2:
            last_name = parts[0]
            first_name = " ".join(parts[1:])
            return last_name, first_name
        return full_name, "" 

    # ------------------------------------------------------------------------------
    
    def _create_info_field(self, parent, label_text, info_text, row):
        # using the new fixed style names
        label = ttk.Label(parent, text=label_text, style='SettingsTitle.TLabel')
        label.grid(row=row, column=0, sticky='w', padx=5, pady=10)
        
        info_label = ttk.Label(parent, text=info_text, style='SettingsData.TLabel')
        info_label.grid(row=row, column=1, sticky='w', padx=10, pady=10)
        
        # add separator line
        ttk.Separator(parent, orient=tk.HORIZONTAL).grid(row=row+1, column=0, columnspan=2, sticky='ew')


    def load_profile_image(self, canvas, size_px):
        try:
            # load and resize the image
            original_image = Image.open(self.profile_image_path)
            size = (size_px, size_px)
            resized_image = original_image.resize(size, Image.LANCZOS)
            self.profile_photo_tk = ImageTk.PhotoImage(resized_image)
            
            # draw the image on the canvas
            canvas.create_image(size_px//2, size_px//2, image=self.profile_photo_tk, anchor='center')
        except Exception:
            # fallback text if image not found
            canvas.create_text(size_px//2, size_px//2, text="Profile\nPic", font=self.ui.get_font('Arial', 16), fill='black', justify=tk.CENTER)

    # ------------------------------------------------------------------------------

    def create_settings_view(self):
        
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
            
        main_content = tk.Frame(self.parent_frame, bg="#cad2c5", padx=self.ui.w_pct(4), pady=self.ui.h_pct(2))
        main_content.pack(fill='both', expand=True)

        tk.Label(main_content, text="ACCOUNT SETTINGS", font=self.ui.get_font('Arial', 40, 'bold'),
                 bg='#cad2c5', fg='#2f3e46').pack(pady=(self.ui.h_pct(2), self.ui.h_pct(6)))
        
        details_frame = tk.Frame(main_content, bg="#cad2c5")
        details_frame.pack(fill='x', pady=self.ui.h_pct(1))
        
        # configure columns for image (left) and fields (right)
        details_frame.grid_columnconfigure(0, weight=1) 
        details_frame.grid_columnconfigure(1, weight=3) 

        # profile picture section (mimics profile page visually)
        img_size = self.ui.get_size(150)
        image_canvas = tk.Canvas(details_frame, width=img_size, height=img_size, bg="lightgray", highlightthickness=0, borderwidth=2, relief='groove')
        image_canvas.grid(row=0, column=0, padx=self.ui.w_pct(2), pady=self.ui.h_pct(1), sticky='n', rowspan=4)
        self.load_profile_image(image_canvas, img_size)

        # fields frame (read-only info)
        fields_frame = tk.Frame(details_frame, bg="#cad2c5")
        fields_frame.grid(row=0, column=1, sticky='ew')
        fields_frame.grid_columnconfigure(1, weight=1) 

        # first name
        self._create_info_field(fields_frame, "First Name:", self.first_name, 0)
        
        # last name
        self._create_info_field(fields_frame, "Last Name:", self.last_name, 2)
        
        # email
        self._create_info_field(fields_frame, "Email:", self.logged_in_email, 4)
        
        # account creation date
        self._create_info_field(fields_frame, "Account Created:", self.account_creation_date, 6)
        
        action_frame = tk.Frame(main_content, bg='#cad2c5')
        action_frame.pack(fill='x', pady=self.ui.h_pct(4))
        action_frame.grid_columnconfigure(0, weight=1)
        action_frame.grid_columnconfigure(1, weight=1)
        
        # delete account button
        delete_btn = ttk.Button(action_frame, text="DELETE ACCOUNT", command=self.delete_account, style='Delete.TButton')
        delete_btn.grid(row=0, column=0, padx=self.ui.w_pct(2), sticky='ew')
        
        # exit button
        exit_btn = ttk.Button(action_frame, text="EXIT", command=self.exit_view, style='Exit.TButton')
        exit_btn.grid(row=0, column=1, padx=self.ui.w_pct(2), sticky='ew')


    # ------------------------------------------------------------------------------
    
    def delete_account(self):
        # confirm deletion
        confirm = messagebox.askyesno("Confirm Deletion", 
                                      "WARNING: Are you sure you want to permanently delete your account? This action cannot be undone.",
                                      parent=self.parent_frame)
        
        if confirm:
            # show the required message
            messagebox.showinfo("Account Deleted", "Your account has been deleted.", parent=self.parent_frame)
            
            # send back to login (using the same mechanism as logout)
            self.switch_view_callback("logout_relaunch")

    # ------------------------------------------------------------------------------

    def exit_view(self):
        self.switch_view_callback("home")