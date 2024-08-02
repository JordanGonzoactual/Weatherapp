import tkinter as tk
from tkinter import ttk 
import threading
import unittest


#Application class
class Weatherapp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weatherapp")
        self.geometry("1900x1080")


        












#Window
root = tk.Tk()
myLabel = tk.Label(root, text= "Hello World")
myLabel.pack

root.mainloop()