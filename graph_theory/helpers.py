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


def plot_map(map: Map) -> None:
    """
    Plots the map in a window

    :param map: the map to draw
    """
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.matshow(map, cmap=ListedColormap(['blue', 'goldenrod']))
    ax.set_xticks(range(0, len(map[0])))
    ax.set_yticks(range(0, len(map)))
    # ax.xaxis.set_minor_locator(MultipleLocator(200))
    # ax.yaxis.set_minor_locator(MultipleLocator(200))
    ax.grid(which='minor', color='gray', linewidth=1)
    ax.tick_params(which='major', top=False, bottom=False, left=False, right=False)
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
    print('Map preview:')
    draw_map(map)
    print('\nIslands found:', map_explorer.detect_island_graph())
    plot_map(map)


def proccess_image(path: Path) -> Map:

    original_image = imread(path.absolute())
    x, y, _ = original_image.shape
    flat_image = np.reshape(original_image, [-1, 3])

    kmeans = KMeans(n_clusters=2, n_init=10)
    print('fit')
    kmeans.fit(flat_image)

    return kmeans.labels_.reshape(x, y).tolist()
