import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from .map_explorer import MapExplorer


def create_random_map(min_length: int = 5, max_length: int = 10) -> list[list[int]]:
    """
    Creates a random map of 0's and 1's (water/land) with a random number of rows and columns

    :param min_length: minimal width and height of the map
    :param max_length: maximal width and height of the map
    :return: a randomly created map
    """
    rows, columns = random.randint(min_length, max_length), random.randint(min_length, max_length)
    return [[random.randint(0, 1) for y in range(columns)] for _ in range(rows)]


def draw_map(map: list[list[int]]) -> None:
    """
    Draws the map in the console
    ' ' - Water
    'M' - Motherland

    :param map: the map to draw
    """
    [print('| ' + ' '.join(['M' if bit else ' ' for bit in row]) + ' |') for row in map]


def plot_map(map: list[list[int]]) -> None:
    """
    Plots the map in a window

    :param map: the map to draw
    """
    plt.matshow(map, cmap=ListedColormap(['blue', 'goldenrod']))
    plt.xticks(range(0, len(map[0])))
    plt.yticks(range(0, len(map)))
    plt.show()


def print_map_as_bits(map: list[list[int]]) -> None:
    """
    Prints map as bits, each row in the next line

    :param map: the map to print
    """
    for row in map:
        print(row)


def present_map(map: list[list[int]]) -> None:
    """
    Prints simple map visualization, counts the islands on the map

    :param map: the map to present
    """
    map_explorer = MapExplorer(map)
    map_explorer.perform_exploring()
    print('Map preview:')
    draw_map(map)
    print('\nIslands found:', map_explorer.get_islands_count())
    plot_map(map)
