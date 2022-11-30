from dataclasses import dataclass


@dataclass
class Coordinates:
    """Model of coordinates"""
    x: int
    y: int

    def up(self) -> 'Coordinates':
        """
        :return: Coordinate with x - 1
        """
        return Coordinates(self.x - 1, self.y)

    def down(self) -> 'Coordinates':
        """
        :return: Coordinate with x + 1
        """
        return Coordinates(self.x + 1, self.y)

    def left(self) -> 'Coordinates':
        """
        :return: Coordinate with y - 1
        """
        return Coordinates(self.x, self.y - 1)

    def right(self) -> 'Coordinates':
        """
        :return: Coordinate with y + 1
        """
        return Coordinates(self.x, self.y + 1)
