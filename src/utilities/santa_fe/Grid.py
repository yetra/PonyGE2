from utilities.santa_fe.Cell import Cell


class Grid:
    """
    Models a trail of food pellets laid out on a 32 x 32 rectangular grid.
    """

    DIMENSION = 32

    def __init__(self, file_name):
        """
        Constructs a new grid from a given definition file.

        :param file_name: the file describing the grid
        """
        with open(file_name) as file:
            lines = [line.rstrip('\n') for line in file]

        self.food_pieces = 0
        self.grid = []

        for y in range(self.DIMENSION):
            for x in range(self.DIMENSION):
                value = int(lines[y][x])
                self.grid.append(Cell(y, x, value))

                if value == 1:
                    self.food_pieces += 1

    def remove_food_from(self, cell):
        """
        Removes the food pellet from a given cell.

        :param cell: the cell containing the food
        """
        self.grid[cell.x + 32 * cell.y].value = 0

    def has_food_on(self, cell):
        """
        Returns true if a given cell contains a food pellet.

        :param cell: the cell to check
        :return: true if the given cell contains a food pellet
        """
        return self.grid[cell.x + 32 * cell.y].value == 1

    def __str__(self):
        """
        Returns a string representation of this grid.

        Cells containing food pellets are represented with an asterisk (*). Empty cells
        are marked with a dot.

        :return: a string representation of this grid
        """
        grid_string = ""

        for y in range(self.DIMENSION):
            for x in range(self.DIMENSION):
                cell = self.grid[y + 32 * x]

                if self.has_food_on(cell):
                    grid_string += "*"
                else:
                    grid_string += "."

            grid_string += "\n"

        return grid_string
