import tkinter as tk
from tkinter import ttk 
import threading
import unittest

#Window
root = tk.Tk()

#Application class
class Weatherapp(tk.Tk):
    def __init__(self, master):
        super().__init__(master)
        self.title("Weatherapp")
        self.geometry("1900x1080")
        self.configure(bg='#5DE2E7')
        self.add_widgets()
    

    def add_widgets(root):
        button = tk.Button(root, text="Click me")
        button.pack()




        









root.configure(bg='cyan')
root.mainloop()