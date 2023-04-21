import unittest

from elevations_client.client import get_coordinate_elevations, get_h3_cell_elevations


class TestClient(unittest.TestCase):
    def test_get_h3_cell_elevations(self):
        """Test that elevations can be requested for H3 cells."""
        elevations, later, estimated_wait_time = get_h3_cell_elevations([630949280935159295, 630949280220393983])
        self.assertEqual(elevations, {630949280935159295: 151.216965, 630949280220393983: 180.708115})
        self.assertIsNone(later)
        self.assertIsNone(estimated_wait_time)

    def test_get_coordinate_elevations(self):
        """Test that elevations can be requested for latitude/longitude coordinates."""
        elevations, later, estimated_wait_time = get_coordinate_elevations([[54.53097, 5.96836]], resolution=11)
        self.assertEqual(elevations, {(54.53097, 5.96836): 0.0})
        self.assertIsNone(later)
        self.assertIsNone(estimated_wait_time)
