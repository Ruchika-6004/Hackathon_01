# Dynamic Route Optimization and Emission Reduction System

This project optimizes vehicle routes using real-time traffic, weather, and vehicle data. It also estimates CO2 emissions for each route.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
---

### **9. Unit Tests**
#### `test_api_client.py`
```python
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