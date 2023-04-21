import requests


API_URL = "https://europe-west1-windeurope72-private.cloudfunctions.net/elevations-api"


def get_h3_cell_elevations(cells):
    """Get the elevations of the given H3 cells.

    :param iter(int) cells: the integer indexes of the H3 cells to get the elevations of
    :return dict(int, float), list(int)|None, int|None: cell indexes mapped to their elevations in meters, any cell indexes to request again after the wait time, and the estimated wait time
    """
    response = requests.post(API_URL, json={"h3_cells": list(cells)}).json()
    elevations = {int(index): elevation for index, elevation in response["data"]["elevations"].items()}
    later = response["data"].get("later")
    estimated_wait_time = response["data"].get("estimated_wait_time")
    return elevations, later, estimated_wait_time
