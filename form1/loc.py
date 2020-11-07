# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 01:06:33 2020

@author: Hitesh
"""
from geopy.geocoders import Nominatim
import time
from pprint import pprint
app = Nominatim(user_agent="tutorial")


def get_location_by_address(address):
        #time.sleep(1)
        try:
            return app.geocode(address).raw
        except:
            return get_location_by_address(address)


def location_finder(l1):
    #print("working on",l1)   
    location = get_location_by_address(l1)
    latitude = location["lat"]
    longitude = location["lon"]
    return(longitude,latitude)
    
