from main import create_random_map


def test_create_random_map():
    for _ in range(2000):
        min, max = 8, 16
        map = create_random_map(min, max)
        assert min <= len(map) <= max
        assert min <= len(map[0]) <= max



