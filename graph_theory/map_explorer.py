from .models import Coordinates


class MapExplorer:
    """Class for map exploring"""

    MAP_NOT_ISLAND_MARK = 0

    def __init__(self, map: list[list[int]]):
        self._map = map
        self._visited_points: list[list[bool]] = [[False for _ in range(len(row))] for row in map]
        self._island_count = 0

    def _are_coordinates_valid(self, coords: Coordinates) -> bool:
        """
        Checks if the coords.x and coords.y are valid
        :param coords: Coordinates
        :return: True if coordinates are valid
                 False if coordinates are invalid

        """
        if -1 < coords.x < len(self._map) and -1 < coords.y < len(self._map[coords.x]):
            return True
        return False

    def _are_coordinates_visited(self, coords: Coordinates) -> bool:
        """
        Checks if the coords.x and coords.y were already visited
        :param coords: Coordinates
        :return: True if coordinates were visited
                 False if coordinates were not visited

        """
        if (
            self._map[coords.x][coords.y] == self.MAP_NOT_ISLAND_MARK
            or self._visited_points[coords.x][coords.y]
        ):
            return True
        return False

    def _is_fragment_island(self, coords: Coordinates) -> bool:
        """
        Checks if given coordinates are invalid or visited,
        if not calls itself to mark the entire island
        :param coords: Coordinates
        :return: True if marking is completed
                 False if coordinates are invalid, visited or there is no land
        """
        if not self._are_coordinates_valid(coords):
            return False

        if self._are_coordinates_visited(coords):
            return False

        self._visited_points[coords.x][coords.y] = True
        self._are_nearby_lands_connected(coords)

        return True

    def _are_nearby_lands_connected(self, coords: Coordinates) -> None:
        """
        Goes through every land directly connected to given coordinates
        :param coords: Coordinates
        """
        self._is_fragment_island(coords.left())
        self._is_fragment_island(coords.left().down())
        self._is_fragment_island(coords.down())
        self._is_fragment_island(coords.down().right())
        self._is_fragment_island(coords.right())
        self._is_fragment_island(coords.right().up())
        self._is_fragment_island(coords.up())
        self._is_fragment_island(coords.up().left())

    def get_islands_count(self) -> int:
        """
        Returns the islands count
        :return: islands count
        """
        return self._island_count

    def perform_exploring(self) -> None:
        """
        Goes through the map detecting the land
        When the land is detected calls the _is_fragment_island and increments the count
        """
        for x, row in enumerate(self._map):
            for y in range(len(row)):
                if self._is_fragment_island(Coordinates(x, y)):
                    self._island_count += 1
