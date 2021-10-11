from travel_calculator.travel_calculator import TravelCalculator


def test_calculate_success():
    data_model = {'distance_matrix': [[0, 1], [1, 0]], 'num_vehicles': 1, 'depot': 0}
    travel_calculator = TravelCalculator(data_model)
    res = travel_calculator.calculate()

    assert res == [[0, 1, 0]]
