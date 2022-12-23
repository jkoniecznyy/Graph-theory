import random
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
from matplotlib.image import imread
from sklearn.cluster import KMeans

from .map_explorer import MapExplorer, Map


def create_random_map(min_length: int = 5, max_length: int = 10) -> Map:
    """
    Creates a random map of 0's and 1's (water/land) with a random number of rows and columns

    :param min_length: minimal width and height of the map
    :param max_length: maximal width and height of the map
    :return: a randomly created map
    """
    rows, columns = random.randint(min_length, max_length), random.randint(min_length, max_length)
    return [[random.randint(0, 1) for y in range(columns)] for _ in range(rows)]


def draw_map(map: Map) -> None:
    """
    Draws the map in the console
    ' ' - Water
    'M' - Motherland

    :param map: the map to draw
    """
    [print('| ' + ' '.join(['M' if bit else ' ' for bit in row]) + ' |') for row in map]


def scale(x: int, y: int) -> tuple[float, float]:
    """Scale both x and y to a number between 0 and 10 """
    return x / max(x, y) * 10, y / max(x, y) * 10


def plot_map(map: list[list[int]], islands_count: int) -> None:
    """
    Plots the map in a window

    :param map: the map to draw
    :param islands_count: the number of islands found by the algorithm
    """
    fig, ax = plt.subplots(figsize=(scale(len(map[0]), len(map))))
    ax.matshow(map, cmap=ListedColormap(['blue', 'goldenrod']))
    plt.title(f'Islands found: {islands_count}', pad=15)
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    plt.tight_layout()
    plt.show()


def print_map_as_bits(map: Map) -> None:
    """
    Prints map as bits, each row in the next line

    :param map: the map to print
    """
    for row in map:
        print(row)


def present_map(map: Map) -> None:
    """
    Prints simple map visualization, counts the islands on the map

    :param map: the map to present
    """
    map_explorer = MapExplorer(map)
    map_explorer.build_graph()
    # print('Map preview:')
    # draw_map(map)
    # print('\nIslands found:', map_explorer.detect_island_graph())
    plot_map(map, map_explorer.detect_island_graph())


def process_image(path: Path) -> Map:
    original_image = imread(path.absolute())
    x, y, _ = original_image.shape
    flat_image = np.reshape(original_image, [-1, 3])

    kmeans = KMeans(n_clusters=2, n_init=10)
    print('fit')
    kmeans.fit(flat_image)

    return kmeans.labels_.reshape(x, y).tolist()
