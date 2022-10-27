from graph_theory.helpers import create_random_map, draw_map, present_map, print_map_as_bits


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


def test_print_map_as_bits(capsys):
    map = [
        [1, 1],
        [1, 0],
    ]
    print_map_as_bits(map)
    captured = capsys.readouterr()
    assert captured.out == '[1, 1]\n[1, 0]\n'


def test_present_map(capsys):
    map = [
        [1, 1, 0],
        [1, 0, 0],
        [1, 0, 1],
    ]
    present_map(map)
    captured = capsys.readouterr()
    assert 'Islands found: 2' in captured.out
    assert '| M M   |\n| M     |\n| M   M |' in captured.out
