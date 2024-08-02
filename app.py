import tkinter as tk
from tkinter import ttk 
import threading
import unittest
from tkinter import *
from PIL import Image, ImageTk
import logging




#Application class
class Weatherapp(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Weatherapp")
        self.geometry("1900x1080")
        self.add_background()
        self.add_widgets()

    
    #Adds Widgets
    def add_widgets(self):
        # Frame for Drop down menu
        self.Dpframe = tk.Frame(self, bg='#FFFFFF', height=150, width=125, relief= RAISED)
        self.Dpframe.pack(padx=30, pady=30, fill= 'both', expand= True)
        
        #Drop down Menu
        options = ["Monday"," Tuesday", "Wednesday", "Thursday","Friday","Saturday","Wednesday"]
        clicked = tk.StringVar()
        clicked.set("Monday")
        self.dropdown = tk.OptionMenu(self.Dpframe, clicked, *options)
        self.dropdown.config(relief= RAISED, width=50, bg='#E4080A')
        self.dropdown.pack(padx=30, pady=30, fill='both', expand=True)
    
    def add_background(self):
        self.bgimage='H:/Python/Weatherapp/Images/Weatherbg.jpg'
        print(f"Icon path: {self.bgimage}")
        self.image = Image.open(self.bgimage)
        self.background= ImageTk.PhotoImage(self.image)
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.pack(fill='both',expand=True)
        
       




if __name__=="__main__":
    try:
        app = Weatherapp()
        app.mainloop()  
    except ValueError as e:
        print("You have this wrong {e}")
    except SyntaxError as e:
        print("Hey this went wrong {e}")





