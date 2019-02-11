#!/bin/python3

import json
import turtle
import urllib.request
import time

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
latitude = float(location['latitude'])
longitude = float(location['longitude'])

print('Latitude: ', latitude)
print('Longitude: ', longitude)

##load world map as the background image using turtle graphics library
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)



## FIND WHEN THE ISS WILL NEXT BE OVER A CERTAIN LOCATION
## to practice we will do this for Calgary, AB

latitude = 51.048615
longitude = -114.070847

location = turtle.Turtle()
location.color('yellow')
location.penup()
location.goto(longitude, latitude)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(latitude) + '&lon=' + str(longitude)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

passover = result['response'][1]['risetime']

style = ('Arial', 6, 'bold')
location.write(time.ctime(passover), font=style)

screen.exitonclick()