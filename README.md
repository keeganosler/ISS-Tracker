# ISS-Tracker

This project uses Python3, Turtle Graphics library and an API provided for the International Space Station (ISS) to plot and track the location of the International Space Station (ISS).  The project is hosted as a web app by embedding Trinket.io code into the index HTML file for the webpage.

First, python is connected to the ISS API to find information on the current location of the ISS and plot it on a world map as shown below.

![screenshot](https://github.com/keeganosler/ISS-Tracker/blob/master/readme%20images/currentLocation.JPG)

The app also gives the user the ability to determine when the ISS will next passover a certain area. To do this, it instructs the user to search for the latitude and longitude of a certain location, then enter those values into the terminal.  The program then implements a turtle at that location showing the next date and time the ISS will pass overhead.  An example of this is shown below.

![screenshot](https://github.com/keeganosler/ISS-Tracker/blob/master/readme%20images/passover.JPG)


## Acknowledgements

This project was inspired by the Code Club [Where is the Space Station?](https://codeclubprojects.org/en-GB/python/iss/) project and uses the ISS API by [natronics](https://github.com/natronics).

## Future Work and Extensions

I would like to at some point extend this library to include the ability to search for latitude and longitude itself instead of having to redirect the user to another website to do this.
