import unittest
from unittest.mock import patch

from h3 import H3CellError

from elevations_client.client import (
    get_coordinate_elevations,
    get_h3_cell_elevations,
    get_h3_cell_elevations_in_polygon,
)


class TestClient(unittest.TestCase):
    def test_error_raised_if_invalid_h3_cells_given(self):
        """Test that an error is raised and no requests are made to the API if any of the cells are invalid."""
        with patch("elevations_client.client.requests.post") as mock_post:
            with self.assertRaises(H3CellError):
                get_h3_cell_elevations([630949280935159295, 1])

        mock_post.assert_not_called()

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

    def test_get_h3_cell_elevations_in_polygon(self):
        """Test that elevations can be requested for a polygon."""
        elevations, later, estimated_wait_time = get_h3_cell_elevations_in_polygon(
            polygon=[[54.53097, 5.96836], [54.53075, 5.96435], [54.52926, 5.96432], [54.52903, 5.96888]],
            resolution=10,
        )

        self.assertEqual(
            elevations,
            {622045820847718399: 0.0, 622045820847849471: 0.0, 622045848952471551: 0.0, 622045848952602623: 0.0},
        )

        self.assertIsNone(later)
        self.assertIsNone(estimated_wait_time)
