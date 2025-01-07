import unittest
from app.emissions_calculator import EmissionsCalculator

class TestEmissionsCalculator(unittest.TestCase):
    def test_calculate_emissions(self):
        emissions = EmissionsCalculator.calculate_emissions(100)  # 100 km
        self.assertAlmostEqual(emissions, 69.3, places=1)  # 100 * 0.3 * 2.31 = 69.3 kg

if __name__ == "__main__":
    unittest.main()