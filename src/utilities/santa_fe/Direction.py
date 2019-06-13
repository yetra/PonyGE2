from enum import Enum


class Direction(Enum):
    """
    An enumeration of all the possible ant orientations.
    """

    # top
    NORTH = "N"

    # bottom
    SOUTH = "S"

    # right
    EAST = "E"

    # left
    WEST = "W"
