import random

# lista z obrazka
example_list = [[0, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]]


def create_map() -> list:
    """
    Creates a random map of 0's and 1's (water/land)
    with a random number of rows and columns (both between 3 and 9)

    #TODO Na pewno można ulepszyć jeżeli chcemy

    :return: list
    """
    rows, columns = random.randint(3, 9), random.randint(3, 9)
    return [[random.randint(0, 1) for y in range(columns)] for _ in range(rows)]


def draw_map(map: list) -> None:
    """
    Draws the map in the console
    ' ' = Water
    'M' = Motherland

    #TODO Zrobić wersję niekonsolową

    :param map:
    :return: None
    """
    [print('| ' + ' '.join(['M' if bit else ' ' for bit in row]) + ' |') for row in map]


def count_islands(map: list) -> int:
    """
    Goes through the map detecting the land
    When the land is detected calls the function explore
    and increments the count

    #TODO Czy powinno liczyć też po skosie?.

    :param map:
    :return: number of islands found
    """
    visited = set()
    count = 0
    for row_nr, row in enumerate(map):
        for column_nr in range(len(row)):
            if explore(map, row_nr, column_nr, visited):
                count += 1

    return count


def explore(map: list, row_nr: int, column_nr: int, visited: set):
    """
    Explores the island to mark all of its land

    :param map:
    :param row_nr:
    :param column_nr:
    :param visited:
    :return:
    """
    position = f'{row_nr},{column_nr}'
    # print('explore positon: '+ position)

    try:
        if map[row_nr][column_nr] == 0:
            return False
    except IndexError:
        return False

    if position in visited:
        return False
    else:
        visited.add(position)

    explore(map, row_nr, column_nr - 1, visited)  # left
    explore(map, row_nr + 1, column_nr - 1, visited)  # left down
    explore(map, row_nr + 1, column_nr, visited)  # down
    explore(map, row_nr + 1, column_nr + 1, visited)  # down right
    explore(map, row_nr, column_nr + 1, visited)  # right
    explore(map, row_nr - 1, column_nr + 1, visited)  # right up
    explore(map, row_nr - 1, column_nr, visited)  # up
    explore(map, row_nr - 1, column_nr - 1, visited)  # up left
    return True


# print(count_islands(example_list))
m1 = create_map()
print('Map preview:')
draw_map(m1)
print()
print('Islands found: ', count_islands(m1))

print('Map preview:')
draw_map(example_list)
print()
print('Islands found: ', count_islands(example_list))
