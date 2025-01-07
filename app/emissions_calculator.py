class EmissionsCalculator:
    EMISSION_FACTOR = 2.31  # CO2 emissions in kg per liter of diesel
    FUEL_CONSUMPTION_RATE = 0.3  # Fuel consumption in liters per km

    @staticmethod
    def calculate_emissions(distance_km):
        """Calculate CO2 emissions based on distance and vehicle details."""
        fuel_consumed = distance_km * EmissionsCalculator.FUEL_CONSUMPTION_RATE
        emissions = fuel_consumed * EmissionsCalculator.EMISSION_FACTOR
        return emissions