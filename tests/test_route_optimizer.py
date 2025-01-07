import unittest
from app.route_optimizer import RouteOptimizer

class TestRouteOptimizer(unittest.TestCase):
    def test_optimize_route(self):
        optimizer = RouteOptimizer()
        route_details = optimizer.optimize_route("New York, NY", "Los Angeles, CA")
        self.assertIn("distance_km", route_details)
        self.assertIn("duration_min", route_details)

if __name__ == "__main__":
    unittest.main()