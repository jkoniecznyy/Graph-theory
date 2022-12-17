from collections import defaultdict

from .models import Coordinates


class MapExplorer:
    """Class for map exploring"""

    MAP_IS_NOT_LAND_MARK = 0

    def __init__(self, map: list[list[int]]):
        self._map = map
        self._visited_points: list[list[bool]] = [[False for _ in range(len(row))] for row in map]
        self._island_count = 0
        self._graph: dict[Coordinates, set[Coordinates]] = defaultdict(set)

    def _are_coordinates_valid(self, coords: Coordinates) -> bool:
        """
        Checks if the coords.x and coords.y are valid
        :param coords: Coordinates
        :return: True if coordinates are valid
                 False if coordinates are invalid

        """
        return -1 < coords.x < len(self._map) and -1 < coords.y < len(self._map[coords.x])

    def build_graph(self) -> None:
        for x, row in enumerate(self._map):
            for y in range(len(row)):
                self._add_neighbours(Coordinates(x, y))

    def _add_neighbours(self, coords: Coordinates) -> None:
        for current_checking in [
            coords.left(),
            coords.left().down(),
            coords.down(),
            coords.down().right(),
            coords.right(),
            coords.right().up(),
            coords.up(),
            coords.up().left(),
        ]:
            if self._is_land(current_checking):
                self._graph[coords].add(current_checking)

    def _is_land(self, coords: Coordinates) -> bool:
        return (
            self._are_coordinates_valid(coords)
            and not self._map[coords.x][coords.y] == self.MAP_IS_NOT_LAND_MARK
        )

    def _is_visited(self, coords: Coordinates) -> bool:
        return self._are_coordinates_valid(coords) and self._visited_points[coords.x][coords.y]

    def _mark_as_visited(self, coords: Coordinates) -> None:
        self._visited_points[coords.x][coords.y] = True

    def _dfs(self, start_node: Coordinates) -> None:
        stack = [start_node]

        # iterate until the stack is empty
        while stack:
            # get the top node from the stack
            node = stack.pop()

            # if the node has not been visited, mark it as visited
            # and add its neighbors to the stack
            if not self._is_visited(node):
                self._mark_as_visited(node)
                stack.extend(self._graph[node])

    def detect_island_graph(self) -> int:
        detected_islands = 0
        for x, row in enumerate(self._map):
            for y in range(len(row)):
                point = Coordinates(x, y)
                if not self._is_visited(point) and self._is_land(point):
                    self._dfs(point)
                    detected_islands += 1

        return detected_islands
