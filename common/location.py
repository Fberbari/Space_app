import requests
import json
import sys

class location:

	def calc_geojson(user_location):

		_data ={

				"key":"LNrUC5ByQxcqqGTVisxpd2wKxMyd97Aj",
				"location":user_location,	
				"thumbMaps":"false"
		} 

		response = requests.post('http://www.mapquestapi.com/geocoding/v1/address', data=_data)

		latlung = response.json()

		latlung = latlung["results"][0]['locations'][0]["latLng"]



		lat = float(latlung["lat"])
		lng = float(latlung["lng"])



		geojson = {
		  "type": "FeatureCollection",
		  "features": [
		    {"type": "Feature","properties": {},"geometry": {"type": "Polygon","coordinates": [
		          [
		            [-1,-1],
		            [-1,-1],
		            [-1,-1],
		            [-1,-1],
		            [-1, -1]
		          ]
		        ]
		      }
		    }
		  ]
		}
		 

		radius = 5

		if (radius == None):
			
			sys.exit("YOU MUST DEFINE THE RADIUS OF THE SQUARE POLYGON!!!!!!!!!!!!!!!!!!")



		geojson["features"][0]["geometry"]["coordinates"][0][0][1] = lng - radius
		geojson["features"][0]["geometry"]["coordinates"][0][0][0] = lat - radius

		geojson["features"][0]["geometry"]["coordinates"][0][1][1] = lng + radius
		geojson["features"][0]["geometry"]["coordinates"][0][1][0] = lat - radius

		geojson["features"][0]["geometry"]["coordinates"][0][2][1] = lng + radius
		geojson["features"][0]["geometry"]["coordinates"][0][2][0] = lng + radius

		geojson["features"][0]["geometry"]["coordinates"][0][3][1] = lng - radius
		geojson["features"][0]["geometry"]["coordinates"][0][3][0] = lng + radius

		geojson["features"][0]["geometry"]["coordinates"][0][4][1] = lng - radius
		geojson["features"][0]["geometry"]["coordinates"][0][4][0] = lat - radius

		return (geojson)

	def calc_latlng(user_location):


		_data ={

				"key":"LNrUC5ByQxcqqGTVisxpd2wKxMyd97Aj",
				"location":user_location,	
				"thumbMaps":"false"
		} 

		response = requests.post('http://www.mapquestapi.com/geocoding/v1/address', data=_data)

		latlng = response.json()

		latlng = latlng["results"][0]['locations'][0]["latLng"]

		return (latlng)
