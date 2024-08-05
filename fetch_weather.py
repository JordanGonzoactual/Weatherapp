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
    json_data = response.json()
    logging.debug("Weather Data fetched")
    return json_data
    

#Parses json data
def parse_weather_data(json_data):
    #Parses the json data
    weather_stats = {"location": json_data['location']['name'],
    "temperature" : json_data['current']['temp_f'],
    "wind" : json_data['current']['wind_mph'],
    "humidity" : json_data['current']['humidity'],
    "rain" : json_data['current']['precip_in'],
    "Uvindex" : json_data['current']['uv'],
    "feelslike" : json_data['current']['feelslike_f'],
    "cloud" : json_data['current']['cloud'],
    "windchill" : json_data['current']['windchill_f'],
    "visibility" : json_data['current']['vis_miles'],
    "lastupdated" : json_data['current']['last_updated']}
    
    return weather_stats
    

def main():
    construct_url('miami','metric', 'days','key')
    json_data = fetch_weather_data()
    parse_weather_data(json_data)
    print(json_data)
    

  
      
    

if __name__== "__main__":
    main()






