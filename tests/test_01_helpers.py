from pathlib import Path
import pytest
from pytest_mock import MockerFixture
from graph_theory.helpers import create_random_map, draw_map, present_map, print_map_as_bits, process_image, scale

@pytest.fixture(scope='function')
def mock_show(mocker: MockerFixture):
    mocker.patch('matplotlib.pyplot.show', return_value=None)


def test_create_random_map_sizes():
    for _ in range(2000):
        min, max = 8, 16
        map = create_random_map(min, max)
        assert min <= len(map) <= max
        assert min <= len(map[0]) <= max


def test_draw_map(capsys):
    map = [
        [0, 1],
        [1, 0],
    ]
    draw_map(map)
    captured = capsys.readouterr()
    assert captured.out == '|   M |\n| M   |\n'

@pytest.mark.parametrize("x, y, expected", [
    (100, 120, (8.333333333333334, 10.0)),
    (148, 222, (6.666666666666666,10.0)),
    (590, 369, (10.0, 6.254237288135593))
])
def test_scale(x: int, y: int, expected: tuple[float, float]):
    result = scale(x, y)
    assert isinstance(result, tuple)
    assert result == expected

def test_print_map_as_bits(capsys):
    map = [
        [1, 1],
        [1, 0],
    ]
    print_map_as_bits(map)
    captured = capsys.readouterr()
    assert captured.out == '[1, 1]\n[1, 0]\n'


def test_present_map(mock_show):
    map = [
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
    ]
    present_map(map)
    assert mock_show == None


def test_proccess_image():
    result = process_image(Path(__file__).parent / 'test_images' / 'map.jpg')

    for row in result:
        for i in row:
            assert i in [0, 1]
