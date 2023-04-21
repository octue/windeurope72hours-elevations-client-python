import requests


API_URL = "https://europe-west1-windeurope72-private.cloudfunctions.net/elevations-api"


def get_h3_cell_elevations(cells):
    """Get the elevations of the given H3 cells. The database serving this function is lazily-loaded - an elevation is
    either returned for each cell if it's immediately available or the cell index is returned as part of a list of cell
    indexes to come back for later along with an estimated wait time.

    :param iter(int) cells: the integer indexes of the H3 cells to get the elevations of
    :return dict(int, float), list(int)|None, int|None: cell indexes mapped to their elevations in meters, any cell indexes to request again after the wait time, and the estimated wait time
    """
    response = requests.post(API_URL, json={"h3_cells": list(cells)}).json()
    elevations = {int(index): elevation for index, elevation in response["data"]["elevations"].items()}
    elevations_to_get_later = response["data"].get("later")
    estimated_wait_time = response["data"].get("estimated_wait_time")
    return elevations, elevations_to_get_later, estimated_wait_time
