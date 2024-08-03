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
        #self.add_background()
        self.add_widgets()

    
    #Adds Widgets
    def add_widgets(self):
        # Frame for Drop down menu
        self.Dpframe = tk.Frame(self, bg='#FFFFFF', relief= RAISED)
        logging.debug("Creating and packing Dpframe")
        self.Dpframe.place(x=825,y=25)
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
        # Frame for weather statistics
        self.Weatherframe= tk.Frame(self, bg='#FFFFFF')
        logging.debug("Creating Weather frame")
        self.Weatherframe.place(x=800, y=400)
        self.Weatherframe.config(height=400, width =350)
        logging.debug(f"Weather frame created with properties= height={self.Weatherframe.winfo_height()}, width={self.Weatherframe.winfo_width()}")

        # Label for weather stats
        self.L1= tk.Label(self.Weatherframe, text= "Temperature", bg='white')
        self.L1.place(x= 25, y=25, in_=self.Weatherframe)
        self.L1.configure(fg="black")
        logging.debug(f"Created Temperature label")
        # Humidity label
        self.L2= tk.Label(self.Weatherframe, text= "Humidity", bg='white')
        self.L2.place(x= 25, y=50, in_=self.Weatherframe)
        self.L2.configure(fg="black")
        logging.debug(f"Created Humidity label")
        # Wind Label
        self.L3= tk.Label(self.Weatherframe, text= "Wind", bg='white')
        self.L3.place(x= 25, y=75, in_=self.Weatherframe)
        self.L3.configure(fg="black")
        logging.debug(f"Created Wind label")
        # Precipitation
        self.L4= tk.Label(self.Weatherframe, text= "Precipitation", bg='white')
        self.L4.place(x= 25, y=100, in_=self.Weatherframe)
        self.L4.configure(fg="black")
        logging.debug(f"Created Precipitation label")
        # Sunrise
        self.L5= tk.Label(self.Weatherframe, text= "Sunrise", bg='white')
        self.L5.place(x= 25, y=125, in_=self.Weatherframe)
        self.L5.configure(fg="black")
        logging.debug(f"Created Sunrise label")
        #Sunset
        self.L6= tk.Label(self.Weatherframe, text= "Sunset", bg='white')
        self.L6.place(x= 25, y=150, in_=self.Weatherframe)
        self.L6.configure(fg="black")
        logging.debug(f"Created Sunset label")
        # Moon Phase
        self.L7= tk.Label(self.Weatherframe, text= "Moon Phase", bg='white')
        self.L7.place(x= 25, y=175, in_=self.Weatherframe)
        self.L7.configure(fg="black")
        logging.debug(f"Created Moob Phase label")
        #Cloud cover
        self.L8= tk.Label(self.Weatherframe, text= "Cloud cover", bg='white')
        self.L8.place(x= 25, y=200, in_=self.Weatherframe)
        self.L8.configure(fg="black")
        logging.debug(f"Created Cloud cover label")
        # Thunderstorms
        self.L9= tk.Label(self.Weatherframe, text= "Thunderstorm probability", bg='white')
        self.L9.place(x= 25, y=225, in_=self.Weatherframe)
        self.L9.configure(fg="black")
        logging.debug(f"Created Thunderstorm label")
        # Air Quality
        self.L10= tk.Label(self.Weatherframe, text= "Air Quality Index", bg='white')
        self.L10.place(x= 25, y=250, in_=self.Weatherframe)
        self.L10.configure(fg="black")
        logging.debug(f"Created Air Quality label")
        # Uv index Label
        self.L11= tk.Label(self.Weatherframe, text= "UV Index", bg='white')
        self.L11.place(x= 25, y=275, in_=self.Weatherframe)
        self.L11.configure(fg="black")
        logging.debug(f"Created Uv Index label")
        # Feels like temp label
        self.L12= tk.Label(self.Weatherframe, text= "Feels like", bg='white')
        self.L12.place(x= 25, y=25, in_=self.Weatherframe)
        self.L12.configure(fg="black")
        logging.debug(f"Created Feels like label")
        # Visibility label
        self.L13= tk.Label(self.Weatherframe, text= "Visibility", bg='white')
        self.L13.place(x= 25, y=25, in_=self.Weatherframe)
        self.L13.configure(fg="black")
        logging.debug(f"Created Visibility label")
        # Air Pressure label
        self.L14= tk.Label(self.Weatherframe, text= "Air pressure", bg='white')
        self.L14.place(x= 25, y=25, in_=self.Weatherframe)
        self.L14.configure(fg="black")
        logging.debug(f"Created Air pressure label")





        
    
    
    
    
    
    
    
    
    
    
    def add_background(self):
        self.bgimage='H:/Python/Weatherapp/Images/Weatherbg.jpg'
        self.image = Image.open(self.bgimage)
        self.background= ImageTk.PhotoImage(self.image)
        self.background_label = tk.Label(self, image=self.background)
        self.background_label.place(x=0, y=0)
        logging.debug("Background image added")
        #Ensures proper updating
        self.update_idletasks()
        
       




if __name__=="__main__":
    try:
        app = Weatherapp()
        app.mainloop()  
    except ValueError as e:
        print("You have this wrong {e}")
    except SyntaxError as e:
        print("Hey this went wrong {e}")





