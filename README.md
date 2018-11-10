# Space_app
MAANS is a web app that allows a user to input a location by address, postal code or city name, uses the radarsat api to get historical 
images of the area of choice, uses a k means clustering algorithm to seperate common features such as urban sprawl or water and returns 
the processed images to the user.


As of right now, the app is not fully integrated, as we had to process and gather data on seperate machines. Also, the gedal python library
has severe problems and has not consistantly functioned. 

While we work on fixes and integration though, we have included some sample images of Toronto that we have clustered. You may find these 
in static/data/data_in.

