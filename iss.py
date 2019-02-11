#!/bin/python3

import json
import turtle
import urllib.request

## PRINT OUT STATS ABOUT THE ASTRONAUTS CURRENTLY IN SPACE

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

##look up and display the number of people in space
print('# of people currently in space: ', result['number'])

##look up and list the people currently in space, print out their name and the craft they are in
people = result['people']
print('List of people currently in space: ')
for person in people:
  print(person['name']+': '+person['craft'])



## INFO ABOUT THE LOCATION OF THE ISS

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']

print('Latitude: ', latitude)
print('Longitude: ', longitude)