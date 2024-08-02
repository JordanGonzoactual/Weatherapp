import tkinter as tk
from tkinter import ttk 
import threading
import unittest
from tkinter import *




#Application class
class Weatherapp(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Weatherapp")
        self.geometry("1900x1080")
        self.configure(bg='#5DE2E7')
        self.add_widgets()
    

    def add_widgets(self):
        options = ["Monday"," Tuesday", "Wednesday", "Thursday","Friday","Saturday","Wednesday"]
        clicked = tk.StringVar()
        clicked.set("Monday")
        self.dropdown = tk.OptionMenu(self, clicked, *options )
        self.dropdown.pack(padx=30, pady=50)
        
       
       
    
        
    def button_click():
        print("I got clicked")




if __name__=="__main__":
    try:
        app = Weatherapp()
        app.configure(bg='cyan')
        app.mainloop()  
    except ValueError as e:
        print("You have this wrong {e}")
    except SyntaxError as e:
        print("Hey this went wrong {e}")





