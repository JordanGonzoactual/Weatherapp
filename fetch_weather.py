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
    location = json_data['location']['name']
    temperature = json_data['current']['temp_f']
    wind = json_data['current']['wind_mph']
    humidity = json_data['current']['humidity']
    Precipitation = json_data['current']['precip_in']
    Uvindex = json_data['current']['uv']
    feelslike = json_data['current']['feelslike_f']
    cloud = json_data['current']['cloud']
    windchill = json_data['current']['windchill_f']
    visibility = json_data['current']['vis_miles']
    weathercondition = json_data['condition']['text']
    lastupdated = json_data['current']['last_updated']

    #prints stats
    print(f"Location : {location}")
    print(f"Temperature : {temperature}")
    print (f"Wind: {wind}")
    print(f"Humidity: {humidity}")
    print(f"Precipitation: {Precipitation}")
    print(f"UV index: {Uvindex}")
    print(f"Feels like: {feelslike}")
    print(f"Cloud percentage: {cloud}")
    print(f"Windchill: {windchill}")
    print(f"Visbility : {visibility}")
    print(f"Weather Condition: {weathercondition}")
    print(f"Time last updated: {lastupdated}")





def main():
    construct_url('miami','metric', 'days','key')
    json_data = fetch_weather_data()
    parse_weather_data(json_data)
    print(json_data)
    

  
      
    

if __name__== "__main__":
    main()






