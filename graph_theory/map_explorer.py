class MapExplorer:
    """Class for map exploring"""

    MAP_NOT_ISLAND_MARK = 0

    def __init__(self, map: list[list[int]]):
        self._map = map
        self._visited_points: list[list[bool]] = [[False for _ in range(len(row))] for row in map]
        self._island_count = 0

    def _check_row_and_cols_id(self, row_id: int, column_id: int) -> bool:
        """
        Check if the row_id and column_id are valid
        :param row_id: row number
        :param column_id: column number
        :return: True if coordinates are valid
                 False if coordinates are invalid

        """
        if not (-1 < row_id < len(self._map) and -1 < column_id < len(self._map[row_id])):
            return False
        return True

    def _is_fragment_island(self, row_id: int, column_id: int) -> bool:
        """
        Check if given coordinates are invalid or visited,
        if not calls itself to mark the entire island
        :param row_id: row number
        :param column_id: column number
        :return: True if marking is completed
                 False if coordinates are invalid, visited or there is no land
        """
        # 1. Check if coordinates are valid
        if not self._check_row_and_cols_id(row_id, column_id):
            return False

        # 2. Check if coordinates were visited
        if (
            self._map[row_id][column_id] == self.MAP_NOT_ISLAND_MARK
            or self._visited_points[row_id][column_id]
        ):
            return False

        # 3. Mark coordinates as visited
        self._visited_points[row_id][column_id] = True

        # 4. Call itself to go through any land directly connected to the island
        self._is_fragment_island(row_id, column_id - 1)  # left
        self._is_fragment_island(row_id + 1, column_id - 1)  # left down
        self._is_fragment_island(row_id + 1, column_id)  # down
        self._is_fragment_island(row_id + 1, column_id + 1)  # down right
        self._is_fragment_island(row_id, column_id + 1)  # right
        self._is_fragment_island(row_id - 1, column_id + 1)  # right up
        self._is_fragment_island(row_id - 1, column_id)  # up
        self._is_fragment_island(row_id - 1, column_id - 1)  # up left

        # 5. If marking is completed, return True
        return True

    def get_islands_count(self) -> int:
        """
        Return the islands count
        :return: islands count
        """
        return self._island_count

    def perform_exploring(self) -> None:
        """
        Go through the map detecting the land
        When the land is detected call the _is_fragment_island and increment the count
        """
        for row_id, row in enumerate(self._map):
            for column_id in range(len(row)):
                if self._is_fragment_island(row_id, column_id):
                    self._island_count += 1
