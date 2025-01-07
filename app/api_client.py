import os
import requests
from dotenv import load_dotenv

load_dotenv()

class APIClient:
    @staticmethod
    def get_coordinates(destination):
        """Get latitude and longitude using Google Maps Geocoding API."""
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={destination}&key={os.getenv('GOOGLE_MAPS_API_KEY')}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Geocoding API failed to fetch coordinates.")

    @staticmethod
    def get_traffic_data(start_lat, start_lng, end_lat, end_lng):
        """Fetch real-time traffic data using TomTom API."""
        url = f"https://api.tomtom.com/routing/1/calculateRoute/{start_lat},{start_lng}:{end_lat},{end_lng}/json?key={os.getenv('TOMTOM_API_KEY')}&traffic=true"
        response = requests.get(url)
        data = response.json()
        if "routes" in data:
            return data["routes"][0]["summary"]["travelTimeInSeconds"], data["routes"][0]["summary"]["lengthInMeters"]
        else:
            raise Exception("TomTom API failed to fetch traffic data.")

    @staticmethod
    def get_weather_data(lat, lng):
        """Fetch weather data using AQICN API."""
        url = f"https://api.waqi.info/feed/geo:{lat};{lng}/?token={os.getenv('AQICN_API_KEY')}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "ok":
            return data["data"]["iaqi"]["t"]["v"]  # Temperature in Celsius
        else:
            raise Exception("AQICN API failed to fetch weather data.")

    @staticmethod
    def get_route(start_lat, start_lng, end_lat, end_lng):
        """Generate a route using OSRM API."""
        url = f"http://router.project-osrm.org/route/v1/driving/{start_lng},{start_lat};{end_lng},{end_lat}?overview=full"
        response = requests.get(url)
        data = response.json()
        if "routes" in data:
            return data["routes"][0]["distance"], data["routes"][0]["duration"]
        else:
            raise Exception("OSRM API failed to generate a route.")