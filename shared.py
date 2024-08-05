# shared.py
import tkinter as tk
# Initialize Tkinter variables
day_var = None
def initialize_vars(master):
    global day_var
    from shared import day_var
    day_var = tk.StringVar(master)
    day_var.set("Monday") # sets default day





# Function to get the selected day
def get_selected_day():
    day_mapping = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7}
    selected_day = day_var.get("")
    return day_mapping.get(selected_day, None)
