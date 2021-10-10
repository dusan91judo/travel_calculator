from typing import List
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


class TravelCalculator:

    def __init__(self, data: dict):
        self.data = data
        self.manager = None

    def calculate(self, slack: int = 0, maximum_travel_distance: int = 3000) -> List[int]:
        # Create the routing index manager.
        self.manager = pywrapcp.RoutingIndexManager(
            len(self.data['distance_matrix']),
            self.data['num_vehicles'],
            self.data['depot']
        )

        # Create Routing Model.
        routing = pywrapcp.RoutingModel(self.manager)

        transit_callback_index = routing.RegisterTransitCallback(self._distance_callback)

        # Define cost of each arc.
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Add Distance constraint.
        dimension_name = 'Distance'
        routing.AddDimension(
            transit_callback_index,
            slack,
            maximum_travel_distance,
            True,  # start cumul to zero
            dimension_name)
        distance_dimension = routing.GetDimensionOrDie(dimension_name)
        distance_dimension.SetGlobalSpanCostCoefficient(100)

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        cheapest_paths = []
        if solution:
            cheapest_paths = self._get_cheapest_path(routing, solution)

        return cheapest_paths

    def _distance_callback(self, from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = self.manager.IndexToNode(from_index)
        to_node = self.manager.IndexToNode(to_index)
        return self.data['distance_matrix'][from_node][to_node]

    def _get_cheapest_path(self, routing, solution) -> List:
        paths = []
        for vehicle in range(self.data['num_vehicles']):
            vehicle_route = []
            index = routing.Start(vehicle)
            while not routing.IsEnd(index):
                vehicle_route.append(self.manager.IndexToNode(index))
                index = solution.Value(routing.NextVar(index))
            vehicle_route.append(self.manager.IndexToNode(index))
            paths.append(vehicle_route)

        return paths
