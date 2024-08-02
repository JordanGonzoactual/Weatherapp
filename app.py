import tkinter as tk
from tkinter import ttk 
import threading
import unittest




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
        
        self.button = tk.Button(self, text="Click me", command=self )
        self.button.pack()
        
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





