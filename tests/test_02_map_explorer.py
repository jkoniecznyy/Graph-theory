from graph_theory.map_explorer import MapExplorer


def test_init():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)
    assert isinstance(instance, MapExplorer)

    assert instance._map == map
    assert instance._island_count == 0
    assert instance._visited_points == [[0, 0], [0, 0]]


def test_get_islands_count():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)

    assert instance.get_islands_count() == 0
    instance._island_count = 9
    assert instance.get_islands_count() == 9


def test_check_row_and_cols_id():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)
    assert instance._check_row_and_cols_id(0, 0)
    assert instance._check_row_and_cols_id(1, 1)
    assert not instance._check_row_and_cols_id(-1, 1)
    assert not instance._check_row_and_cols_id(1, -1)
    assert not instance._check_row_and_cols_id(2, 0)
    assert not instance._check_row_and_cols_id(1, 2)
    assert not instance._check_row_and_cols_id(5, -2)


def test_is_fragment_island_rows_and_cols_invalid():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)
    assert not instance._is_fragment_island(-1, 1)
    assert not instance._is_fragment_island(1, -1)
    assert not instance._is_fragment_island(2, 0)
    assert not instance._is_fragment_island(1, 2)
    assert not instance._is_fragment_island(5, -2)


def test_is_fragment_island_is_not_land():
    map = [[1, 0], [0, 0]]
    instance = MapExplorer(map)
    assert not instance._is_fragment_island(0, 1)
    assert not instance._is_fragment_island(1, 0)
    assert not instance._is_fragment_island(1, 1)


def test_is_fragment_island_is_visited():
    map = [[1, 0], [1, 0]]
    instance = MapExplorer(map)
    instance._visited_points[0][0] = True
    instance._visited_points[1][0] = True
    assert not instance._is_fragment_island(0, 0)
    assert not instance._is_fragment_island(1, 0)


def test_is_fragment_island_set_visited():
    map = [[1, 0], [1, 0]]
    instance = MapExplorer(map)
    instance._is_fragment_island(0, 0)
    assert instance._visited_points == [[True, False], [True, False]]


def test_is_fragment_island_call_recursive():
    map = [[1, 0, 1], [1, 0, 1], [1, 0, 0]]
    instance = MapExplorer(map)
    instance._is_fragment_island(0, 0)
    assert instance._visited_points == [[True, False, False], [True, False, False], [True, False, False]]


def test_perform_exploring():
    map = [[1, 0, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1]]
    instance = MapExplorer(map)
    instance.perform_exploring()
    assert instance._visited_points == [
        [True, False, True, True], [True, False, True, False], [True, False, False, True]
    ]
    assert instance._island_count == 2
