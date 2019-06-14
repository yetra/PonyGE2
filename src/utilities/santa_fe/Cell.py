

class Cell:
    """
    Models a cell in the trail grid.
    """

    def __init__(self, x, y, value=0):
        """
        Constructs a new cell of the given coordinates and value.

        :param x: the x-coordinate of the cell
        :param y: the y-coordinate of the cell
        :param value: the value of the cell
        """
        self.x = x
        self.y = y
        self.value = value

    def __eq__(self, other):
        """
        Returns true if this cell's coordinates match a given other cell.

        :param other: the cell to compare with
        :return: true if this cell's coordinates match a given other cell
        """
        if isinstance(other, Cell):
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __hash__(self):
        """
        Returns the hash value of this cell.

        :return: the hash value of this cell
        """
        return hash((self.x, self.y))
