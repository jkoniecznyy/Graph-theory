from graph_theory.models import Coordinates


def test_coordinates_to_str():
    assert str(Coordinates(0, 0)) == '0, 0'
    assert str(Coordinates(-110, 89)) == '-110, 89'
