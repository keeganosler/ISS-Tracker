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

##load world map as the background image using turtle graphics library
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)