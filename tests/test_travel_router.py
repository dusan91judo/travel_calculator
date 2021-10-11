from travel_calculator.travel_router import TravelRouter


def test_calculate_route_success():
    travel_router = TravelRouter(coordinates_list=[[10.1, 11.1], [12.1, 15.1]], num_vehicles=1, depot=0)
    res = travel_router.calculate_route()
    assert res == [[0, 1, 0]]
