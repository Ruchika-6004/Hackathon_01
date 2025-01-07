from app.api_client import APIClient

class RouteOptimizer:
    def __init__(self):
        self.api_client = APIClient()

    def optimize_route(self, start_location, end_location):
        """Optimize the route based on real-time data."""
        start_lat, start_lng = self.api_client.get_coordinates(start_location)
        end_lat, end_lng = self.api_client.get_coordinates(end_location)

        travel_time, distance = self.api_client.get_traffic_data(start_lat, start_lng, end_lat, end_lng)
        temperature = self.api_client.get_weather_data(end_lat, end_lng)
        route_distance, route_duration = self.api_client.get_route(start_lat, start_lng, end_lat, end_lng)

        return {
            "start_location": start_location,
            "end_location": end_location,
            "distance_km": route_distance / 1000,
            "duration_min": route_duration / 60,
            "temperature_c": temperature,
        }