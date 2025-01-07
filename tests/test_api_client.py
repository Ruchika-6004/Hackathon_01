import unittest
from app.api_client import APIClient

class TestAPIClient(unittest.TestCase):
    def test_get_coordinates(self):
        client = APIClient()
        lat, lng = client.get_coordinates("New York, NY")
        self.assertIsInstance(lat, float)
        self.assertIsInstance(lng, float)

if __name__ == "__main__":
    unittest.main()