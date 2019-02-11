#!/bin/python3

import json
import turtle
import urllib.request

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

##look up and display the number of people in space
print('# of people currently in space: ', result['number'])

##look up and list the people currently in space
people = result['people']
print('List of people currently in space: ')
for person in people:
  print(person['name'])