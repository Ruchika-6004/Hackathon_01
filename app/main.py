from app.route_optimizer import RouteOptimizer
from app.emissions_calculator import EmissionsCalculator

def main():
    print("Welcome to the Dynamic Route Optimization and Emission Reduction System!")
    
    # User inputs
    start_location = input("Enter the starting location (e.g., 'New York, NY'): ")
    end_location = input("Enter the destination (e.g., 'Los Angeles, CA'): ")

    # Optimize route
    optimizer = RouteOptimizer()
    route_details = optimizer.optimize_route(start_location, end_location)

    # Calculate emissions
    emissions = EmissionsCalculator.calculate_emissions(route_details["distance_km"])

    # Display results
    print("\n--- Route Details ---")
    print(f"Start Location: {route_details['start_location']}")
    print(f"Destination: {route_details['end_location']}")
    print(f"Distance: {route_details['distance_km']:.2f} km")
    print(f"Estimated Travel Time: {route_details['duration_min']:.2f} minutes")
    print(f"Temperature at Destination: {route_details['temperature_c']}°C")
    print(f"Estimated CO2 Emissions: {emissions:.2f} kg")

if __name__ == "__main__":
    main()