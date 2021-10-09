from typing import List
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


class TravelCalculator:

    def __init__(self, data: dict):
        self.data = data
        self.manager = None

    def calculate(self) -> List[int]:
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

        # Setting first solution heuristic.
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Solve the problem.
        solution = routing.SolveWithParameters(search_parameters)

        cheapest_path = []
        if solution:
            cheapest_path = self._get_cheapest_path(solution, routing)

        return cheapest_path

    def _distance_callback(self, from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = self.manager.IndexToNode(from_index)
        to_node = self.manager.IndexToNode(to_index)
        return self.data['distance_matrix'][from_node][to_node]

    def _get_cheapest_path(self, routing, solution) -> List[int]:
        index = routing.Start(0)
        path = [index]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            path.append(index)
        path.append(self.manager.IndexToNode(index))
        return path
