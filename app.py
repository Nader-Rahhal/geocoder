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
        reader = csv.DictReader(file)
        for line in reader:
            print(line)
            #address = line.strip()
            #geocoder.geocode(address)
            #print(results[0]["geometry"])
            
except FileNotFoundError:
    print(f'{addressfile} does not exist.')

# results = geocoder.geocode("3131 12th Avenue, Coralville, IA 52241, United States of America")
# pprint(results[0]["geometry"])
