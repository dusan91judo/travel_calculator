import pytest
from unittest import mock
from travel_calculator.coordinate_parser import CoordinateParser
from travel_calculator.exceptions import InvalidParams


def test_get_distances_success():
    miami = [0.1, 0.1]
    budapest = [0.1, 0.1]

    coordinate_parser = CoordinateParser([miami, budapest])
    coordinate_parser._formula = mock.MagicMock(return_value=10)
    coordinate_parser._validate_input = mock.MagicMock()
    res = coordinate_parser.get_distances()

    assert coordinate_parser._formula.call_count == 1
    assert coordinate_parser._validate_input.call_count == 2
    assert res == [[0, 10], [10, 0]]


def test__formula_success():
    coordinate_parser = CoordinateParser([[]])
    res = coordinate_parser._formula([25.7658958, -80.1929967], [47.4813602, 18.9902208])
    assert res == 101.53261558612569


@mock.patch.object(CoordinateParser, '_validate_input')
def test__validate_input_failed(_validate_input):
    _validate_input = mock.MagicMock(side_effect=InvalidParams('invalid_params'))

    with pytest.raises(InvalidParams) as e:
        _validate_input(['A', 33])

    assert e.value.message == 'invalid_params'
