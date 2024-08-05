import json
import requests
from datetime import datetime
from config import Weather_API_key 
from dataclasses import dataclass, asdict
from typing import Optional
from shared import get_selected_day
import tkinter as tk
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')



baseurl = "http://api.weatherapi.com/v1/current.json"
key = Weather_API_key 




# Creates URL based on paramaters
def construct_url(location, units, days, key):
    logging.debug("Constructing url")
    str(location)
    str(units)
    str(days)
    str(key)
    
    # Combines base url with paramters
    full_url = f"{baseurl}?key={key}&q={location}&units={units}&days={days}"
    logging.debug(f"Constructed url: {full_url}")
    return full_url
   
    
# Fetches Weather data
def fetch_weather_data():
    result = construct_url('miami','metric', 'days', key)
    logging.debug("Attemptng to fetch data")
    response = requests.get(result)
    print(response.json())
    logging.debug("Weather Data fetched")


def main():
    construct_url('miami','metric', 'days','key')
    fetch_weather_data()
    

  
      
    

if __name__== "__main__":
    main()






