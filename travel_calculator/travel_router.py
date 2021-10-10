from typing import List
from .coordinate_parser import CoordinateParser
from .travel_calculator import TravelCalculator


class TravelRouter:

    def __init__(self, coordinates_list: List, num_vehicles: int, depot: int) -> None:
        self.coordinates_list = coordinates_list
        self.num_vehicles = num_vehicles
        self.depot = depot

    def calculate_route(self, slack: int = 0, maximum_travel_distance: int = 3000) -> List:
        coordinate_parser = CoordinateParser(self.coordinates_list)
        distance_matrix = coordinate_parser.get_distances()
        data_model = {'distance_matrix': distance_matrix, 'num_vehicles': self.num_vehicles, 'depot': self.depot}
        tc = TravelCalculator(data_model)
        return tc.calculate(slack, maximum_travel_distance)
