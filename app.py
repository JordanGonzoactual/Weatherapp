import tkinter as tk
from tkinter import ttk 
import threading
import unittest
from tkinter import *
from PIL import Image, ImageTk
import logging

# Logging processes
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

#Application class
class Weatherapp(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Weatherapp")
        self.geometry("1920x1080")
        self.add_background()
        self.add_widgets()

    
    #Adds Widgets
    def add_widgets(self):
        # Frame for Drop down menu
        self.Dpframe = tk.Frame(self, bg='#FFFFFF', relief= RAISED)
        logging.debug("Creating and packing Dpframe")
        self.Dpframe.place(x=750,y=25)
        self.Dpframe.config(height=25.5, width=297)
        self.Dpframe.winfo_height()
        self.Dpframe.winfo_width()
        logging.debug(f"Frame packed with properties: bg={self.Dpframe.cget('bg')}, \
                      width={self.Dpframe.winfo_width()}, height={self.Dpframe.winfo_height()}")
        #Ensures proper updating
        self.update_idletasks()
        #Drop down Menu
        logging.debug("Creating and packing Dropdown")
        options = ["Monday"," Tuesday", "Wednesday", "Thursday","Friday","Saturday","Wednesday"]
        clicked = tk.StringVar()
        clicked.set("Monday")
        self.dropdown = tk.OptionMenu(self.Dpframe, clicked, *options)
        self.dropdown.place(height= self.Dpframe.winfo_height(),width = self.Dpframe.winfo_width(),in_=self.Dpframe, )
        self.dropdown.config(bg='#E4080A', relief= RAISED,)
        logging.debug(f"Dropdown created with properties: bg={self.dropdown.cget('bg')}, \
                      width={self.dropdown.winfo_width()}")
        # Ensures proper updating
        self.update_idletasks()

    def add_background(self):
        self.bgimage='H:/Python/Weatherapp/Images/Weatherbg.jpg'
        logging.debug(f"Image path: {self.bgimage}")
        self.image = Image.open(self.bgimage)
        self.background= ImageTk.PhotoImage(self.image)
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0)
        logging.debug("Background image added")
        # Ensures proper updating
        self.update_idletasks()
        
       




if __name__=="__main__":
    try:
        app = Weatherapp()
        app.mainloop()  
    except ValueError as e:
        print("You have this wrong {e}")
    except SyntaxError as e:
        print("Hey this went wrong {e}")





