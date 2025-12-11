import tkinter as tk
from tkinter import font as tkfont
import os
import sys

def get_resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # In dev, resources are in the same directory as this file (UI folder)
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)

class UIHelper:
    # Reference resolution (design baseline)
    REF_WIDTH = 540
    REF_HEIGHT = 960

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update_dimensions(self, width, height):
        self.width = width
        self.height = height

    def w_pct(self, percentage):
        """Get width as percentage of current window width."""
        return int(self.width * (percentage / 100))

    def h_pct(self, percentage):
        """Get height as percentage of current window height."""
        return int(self.height * (percentage / 100))

    def get_size(self, ref_size, axis='w'):
        """
        Calculate proportional size based on reference size.
        axis: 'w' for width-based scaling, 'h' for height-based, 'min' for min of both.
        """
        if axis == 'w':
            scale = self.width / self.REF_WIDTH
        elif axis == 'h':
            scale = self.height / self.REF_HEIGHT
        else:
            scale = min(self.width / self.REF_WIDTH, self.height / self.REF_HEIGHT)
            
        return int(ref_size * scale)

    def get_font(self, family, size, weight='normal'):
        """
        Get a responsive font size.
        'size' is the desired size at REF_WIDTH.
        """
        # Scale font based on the smaller dimension to avoid it getting too huge on wide screens
        # or too small on tall narrow screens, but generally width is the constraint for text.
        scale_factor = min(self.width / self.REF_WIDTH, self.height / self.REF_HEIGHT)
        
        # Apply a slight dampening to the scaling so it doesn't grow too fast
        # scale_factor = pow(scale_factor, 0.8) 
        
        new_size = int(size * scale_factor)
        if new_size < 10: new_size = 10 # Minimum readable size
        
        # Font fallback logic
        # We can't easily check available families without a root window instance sometimes,
        # but usually tk.Tk() is already created.
        try:
            available_families = tkfont.families()
            if family not in available_families:
                # Fallback chain
                if 'Tex Gyre Chorus' in family and 'Chancery' in available_families:
                     family = 'URW Chancery L' # Common linux alternative
                elif 'Helvetica' in available_families:
                    family = 'Helvetica'
                elif 'Arial' in available_families:
                    family = 'Arial'
                else:
                    family = 'TkDefaultFont'
        except:
            pass # Tk might not be initialized yet, ignore
        
        return (family, new_size, weight)
