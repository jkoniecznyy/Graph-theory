class MapExplorer:
    """Class for map exploring"""

    MAP_NOT_ISLAND_MARK = 0

    def __init__(self, map: list[list[int]]):
        self._map = map
        self._visited_points: list[list[bool]] = [[False for _ in range(len(row))] for row in map]
        self._island_count = 0

    def _are_coordinates_valid(self, row_id: int, column_id: int) -> bool:
        """
        Checks if the row_id and column_id are valid
        :param row_id: row number
        :param column_id: column number
        :return: True if coordinates are valid
                 False if coordinates are invalid

        """
        if -1 < row_id < len(self._map) and -1 < column_id < len(self._map[row_id]):
            return True
        return False

    def _are_coordinates_visited(self, row_id: int, column_id: int) -> bool:
        """
        Checks if the row_id and column_id were already visited
        :param row_id: row number
        :param column_id: column number
        :return: True if coordinates were visited
                 False if coordinates were not visited

        """
        if (
            self._map[row_id][column_id] == self.MAP_NOT_ISLAND_MARK
            or self._visited_points[row_id][column_id]
        ):
            return True
        return False

    def _is_fragment_island(self, row_id: int, column_id: int) -> bool:
        """
        Checks if given coordinates are invalid or visited,
        if not calls itself to mark the entire island
        :param row_id: row number
        :param column_id: column number
        :return: True if marking is completed
                 False if coordinates are invalid, visited or there is no land
        """
        if not self._are_coordinates_valid(row_id, column_id):
            return False

        if self._are_coordinates_visited(row_id, column_id):
            return False

        self._visited_points[row_id][column_id] = True
        self._are_nearby_lands_connected(row_id, column_id)

        return True

    def _are_nearby_lands_connected(self, row_id: int, column_id: int) -> None:
        """
        Goes through every land directly connected to given coordinates
        :param row_id: row number
        :param column_id: column number
        """
        self._is_fragment_island(row_id, column_id - 1)  # left
        self._is_fragment_island(row_id + 1, column_id - 1)  # left down
        self._is_fragment_island(row_id + 1, column_id)  # down
        self._is_fragment_island(row_id + 1, column_id + 1)  # down right
        self._is_fragment_island(row_id, column_id + 1)  # right
        self._is_fragment_island(row_id - 1, column_id + 1)  # right up
        self._is_fragment_island(row_id - 1, column_id)  # up
        self._is_fragment_island(row_id - 1, column_id - 1)  # up left

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
        for row_id, row in enumerate(self._map):
            for column_id in range(len(row)):
                if self._is_fragment_island(row_id, column_id):
                    self._island_count += 1
