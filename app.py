from opencage.geocoder import OpenCageGeocode
from pprint import pprint
import os
from dotenv import load_dotenv, find_dotenv
import csv

load_dotenv()

addressfile = 'sample.csv'

key = os.getenv('OPENCAGE')
geocoder = OpenCageGeocode(key)

try:
    with open(addressfile, 'r') as file:
        reader = csv.reader(file)
        for line in reader:
            address = line[0].strip()
            result = geocoder.geocode(address)
            print(result[0]["geometry"])
            
except FileNotFoundError:
    print(f'{addressfile} does not exist.')

