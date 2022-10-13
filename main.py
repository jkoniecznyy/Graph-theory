import random
from typing import Set, List

# Lista z obrazka
example_list = [[0, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0]]


def createMap() -> List:
    """
    Creates a random map of 0's and 1's (water/land)
    with a random number of rows and columns (both between 3 and 9)

    #TODO Na pewno można ulepszyć jeżeli chcemy

    :return: List
    """
    rows = random.randint(3, 9)
    columns = random.randint(3, 9)
    map = []
    row = []
    for i in range(rows):
        for y in range(columns):
            row.append(random.randint(0, 1))
        map.append(row)
        row = []
    return map


def drawMap(map: List) -> None:
    """
    Draws the map in the console
    ' ' = Water
    'M' = Motherland

    #TODO Zrobić wersję niekonsolową

    :param map:
    :return: None
    """
    for row_nr in range(len(map)):
        print('| ', end='')

        for column_nr in range(len(map[row_nr])):
            if map[row_nr][column_nr]:
                print('M ', end='')
            else:
                print('  ', end='')

        print('|')


def countIslands(map: List) -> int:
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
    for row_nr in range(len(map)):
        row = map[row_nr]
        # print(f'row {row_nr}:  {row}')

        for column_nr in range(len(row)):
            cell = row[column_nr]
            # print(f'cell {row_nr},{column_nr} - value {cell}')
            if explore(map, row_nr, column_nr, visited):
                count += 1

    return count


def explore(map: List, row_nr: int, column_nr: int, visited: Set):
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
    explore(map, row_nr + 1, column_nr, visited)  # down
    explore(map, row_nr, column_nr + 1, visited)  # right
    explore(map, row_nr - 1, column_nr, visited)  # up
    return True


# print(countIslands(example_list))
m1 = createMap()
print('Map preview:')
drawMap(m1)
print()
print('Islands found: ', countIslands(m1))
