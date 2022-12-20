from collections import Counter
import random
import pytest
from graph_theory.map_explorer import MapExplorer, Map
from graph_theory.models import Coordinates


def test_init():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)
    assert isinstance(instance, MapExplorer)

    assert instance._map == map
    assert instance._visited_points == [[False, False], [False, False]]


@pytest.mark.parametrize('map, are_valid, are_not_valid', [
    ([[0, 0], [0, 0]], [Coordinates(0, 0), Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)], []),
    ([[1, 1], [1, 1]], [], [Coordinates(-2, -1), Coordinates(100, 300), Coordinates(3728, -37843)]),
    (
        [[0, 0, 0, 0], [0, 0, 0, 1], [1, 1, 1, 1]],
        [Coordinates(0, 0), Coordinates(2, 3)],
        [Coordinates(2, 4), Coordinates(3, 3), Coordinates(0, 4), Coordinates(-1, 0)])
])
def test_are_coordinates_valid(map: Map, are_valid: list[Coordinates], are_not_valid: list[Coordinates]):
    instance = MapExplorer(map)

    for coord in are_valid:
        assert instance._are_coordinates_valid(coord)
    for coord in are_not_valid:
        assert not instance._are_coordinates_valid(coord)


@pytest.mark.parametrize('map, expected_graph', [
    ([[1, 0], [0, 0]], {}),
    ([[1, 1], [0, 0]], {Coordinates(0, 0): [Coordinates(0, 1)], Coordinates(0, 1): [Coordinates(0, 0)]}),
    ([[1, 1], [1, 0]], {
        Coordinates(0, 0): [Coordinates(0, 1), Coordinates(1, 0)],
        Coordinates(0, 1): [Coordinates(0, 0), Coordinates(1, 0)],
        Coordinates(1, 0): [Coordinates(0, 0), Coordinates(0, 1)],
    }),
    ([[1, 1], [1, 1]], {
        Coordinates(0, 0): [Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)],
        Coordinates(0, 1): [Coordinates(0, 0), Coordinates(1, 0), Coordinates(1, 1)],
        Coordinates(1, 0): [Coordinates(0, 1), Coordinates(0, 0), Coordinates(1, 1)],
        Coordinates(1, 1): [Coordinates(0, 1), Coordinates(1, 0), Coordinates(0, 0)],
    }),
])
def test_build_graph(map: Map, expected_graph: dict[Coordinates, list[Coordinates]]):
    instance = MapExplorer(map)
    instance.build_graph()

    assert (keys := expected_graph.keys()) == instance._graph.keys()
    for key in keys:
        assert Counter(instance._graph.get(key)) == Counter(expected_graph.get(key))


@pytest.mark.parametrize('map, are_lands, are_not_lands', [
    ([[0, 0], [0, 0]], [], [Coordinates(0, 0), Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)]),
    ([[1, 0], [0, 0]], [Coordinates(0, 0)], [Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)]),
    ([[1, 1], [0, 0]], [Coordinates(0, 0), Coordinates(0, 1)], [ Coordinates(1, 0), Coordinates(1, 1)]),
    ([[1, 1], [1, 0]], [Coordinates(0, 0), Coordinates(0, 1), Coordinates(1, 0)], [ Coordinates(1, 1)]),
    ([[1, 1], [1, 1]], [Coordinates(0, 0), Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)], []),
    ([[1, 1], [1, 1]], [], [Coordinates(-2, -1), Coordinates(100, 300), Coordinates(3728, -37843)]),
])
def test_is_land(map: Map, are_lands: list[Coordinates], are_not_lands: list[Coordinates]):
    instance = MapExplorer(map)

    for coord in are_lands:
        assert instance._is_land(coord)
    for coord in are_not_lands:
        assert not instance._is_land(coord)


@pytest.mark.parametrize('map, expected_islands_count', [
    ([[1, 0, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1]], 2),
    ([[1, 0], [0, 0], [1, 1]], 2),
    ([[1, 0], [0, 1], [0, 1]], 1),
])
def test_detect_island_graph(map: Map, expected_islands_count: int):
    instance = MapExplorer(map)
    instance.build_graph()
    assert instance.detect_island_graph() == expected_islands_count
    for x, row in enumerate(map):
            for y in range(len(row)):
                assert (row[y] == 1) == instance._visited_points[x][y]


@pytest.mark.parametrize('map, coord_to_add_neighbours, update', [
    ([[0, 0], [1, 1]], Coordinates(0, 0), None),
    ([[0, 0], [1, 1]], Coordinates(0, 1), None),
    ([[0, 0], [1, 1]], Coordinates(1, 0), [Coordinates(1, 1)]),
    ([[0, 0], [1, 1]], Coordinates(1, 1), [Coordinates(1, 0)]),
    ([[0, 0], [1, 1]], Coordinates(-1, -2), None),
    ([[1, 1], [1, 1]], Coordinates(0, 0), [Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)]),
])
def test_add_neighbours(
    map: Map,
    coord_to_add_neighbours: Coordinates,
    update: list[Coordinates] | None
):
    instance = MapExplorer(map)
    instance._add_neighbours(coord_to_add_neighbours)

    if update is None:
        assert len(instance._graph.keys()) == 0
        return

    assert coord_to_add_neighbours in instance._graph
    assert Counter(instance._graph.get(coord_to_add_neighbours)) == Counter(update)


def test_is_visited():
    instance = MapExplorer([[0, 0], [1, 1]])
    instance._visited_points[1][0] = True
    assert not instance._is_visited(Coordinates(0, 0))
    assert not instance._is_visited(Coordinates(-1, 0))
    assert instance._is_visited(Coordinates(1, 0))
    assert not instance._is_visited(Coordinates(1, 1))


def test_mark_as_visited():
    instance = MapExplorer([[1, 1], [1, 1]])
    to_check = [Coordinates(0, 0), Coordinates(0, 1), Coordinates(1, 0), Coordinates(1, 1)]
    for coords in to_check:
        assert not instance._is_visited(coords)
    for coords in to_check:
        instance._mark_as_visited(coords)
        assert instance._is_visited(coords)
