import random

from graph_theory.map_explorer import MapExplorer

# lista z obrazka
EXAMPLE_MAP_LIST = [
    [0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
]


def create_random_map(min_length: int = 5, max_length: int = 10) -> list[list[int]]:
    """
    Creates a random map of 0's and 1's (water/land)
    with a random number of rows and columns (both between 3 and 9)

    #TODO Na pewno można ulepszyć jeżeli chcemy

    :return: a randomly created map
    """
    rows, columns = random.randint(min_length, max_length), random.randint(min_length, max_length)
    return [[random.randint(0, 1) for y in range(columns)] for _ in range(rows)]


def draw_map(map: list[list[int]]) -> None:
    """
    Draws the map in the console
    ' ' = Water
    'M' = Motherland

    #TODO Zrobić wersję niekonsolową

    :param map: the map to draw
    """
    [print('| ' + ' '.join(['M' if bit else ' ' for bit in row]) + ' |') for row in map]

def print_map_as_bits(map: list[list[int]]) -> None:
    # [print('| ' ', '.join(['M' if bit else ' ' for bit in row]) + ' |') for row in map]
    # print([row for row in map])
    for row in map:
        print(row)


def present_map(map: list[list[int]]):
    map_explorer = MapExplorer(map)
    map_explorer.perform_exploring()
    print('Map preview:')
    draw_map(map)
    print('\nIslands found: ', map_explorer.get_istlands_count())


def main() -> None:
    for _ in range(3):
        mapa=create_random_map(10, 11)
        present_map(mapa)
        print_map_as_bits(mapa)
        print('-'*20)


    # present_map(EXAMPLE_MAP_LIST)


if __name__ == '__main__':
    main()
