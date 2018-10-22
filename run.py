from flask import Flask, render_template, request, session
import json
from common.location import location

'''This app allows the user to input any location in toronto and it will return satellite pictures of the past few years of that location, along with stats that relate to the evolution of the location'''

app = Flask(__name__)
app.secret_key = "secret"



@app.route("/", methods=["POST","GET"])
def Home():



	return render_template("Home.html", abs_lat="????", abs_lng="????")







@app.route("/calculated", methods=["POST","GET"])
def Calculate():

	# get the user data input
	user_location = request.form["location"]

	# produce the geojson data
	geojson = location.calc_geojson(user_location)


	with open('static/data/data_out/polygon.geojson', 'w') as jsonfile:

		json.dump(geojson, jsonfile)

		jsonfile.close()

	# produce the latlng array
	latlng_arr = location.calc_latlng(user_location)

	# extracting lat and long and processing the data into a good sentence
	abs_lat = latlng_arr["lat"]
	abs_lng = latlng_arr["lng"]

	#defaults
	dir_lat = "North"
	dir_lng = "East"

	#adjust if defaults wrong
	if abs_lat < 0:

		dir_lat = "South"
		abs_lat = abs_lat * (-1)

	if abs_lng < 0:

		dir_lng = "West"
		abs_lng = abs_lng * (-1)



	return render_template("Home.html", abs_lat= abs_lat, dir_lat=dir_lat, abs_lng = abs_lng, dir_lng=dir_lng)




if __name__ == "__main__":

	app.run(port=5000, debug=True)






#
#
#
#
#
#
#
#
#