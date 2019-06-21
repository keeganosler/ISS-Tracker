#!/bin/python3

import json
import turtle
import urllib.request
import time

## OBTAIN INFO ABOUT THE LOCATION OF THE ISS

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#convert location coordinates to floats
location = result['iss_position']
latitude = float(location['latitude'])
longitude = float(location['longitude'])

##load world map as the background image using turtle graphics library
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

#obtain a little ISS icon to plot current location
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)

#display coordinates of the current location
curr = turtle.Turtle()
curr.color('yellow')
curr.penup()
curr.goto(-170, -65)
curr.hideturtle()
style = ('Arial', 6, 'bold')
curr.write('Current: '+str(longitude)+', '+str(latitude), font=style)


## FIND WHEN THE ISS WILL NEXT BE OVER A CERTAIN LOCATION

#read user input coordinates
latitude = input('Enter latitude here: ')
longitude = input('Enter longitude here: ')

#create turtle to display this info
location = turtle.Turtle()
location.color('yellow')
location.penup()
location.goto(longitude, latitude)
location.dot(5)
location.hideturtle()

#obtain passover time from API
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(latitude) + '&lon=' + str(longitude)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

passover = result['response'][1]['risetime']

#display next passover time at the given location
style = ('Arial', 6, 'bold')
location.write(time.ctime(passover), font=style)


screen.exitonclick()
