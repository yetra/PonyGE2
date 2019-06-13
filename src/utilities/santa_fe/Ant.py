from santa_fe.Direction import Direction
from santa_fe.Cell import Cell


class Ant:
    """
    Models an ant that can traverse a given trail.

    Starting with a certain amount of energy, it moves around the grid using three action
    methods - move, turn_left, turn_right - and consumes the food it finds on its path.
    """

    DEFAULT_ENERGY = 600

    def __init__(self, grid, total_energy=DEFAULT_ENERGY):
        """
        Creates a new ant of a specified total energy to traverse a given trail.

        :param grid: the grid to traverse
        :param total_energy: the amount of energy that the ant initially has
        """

        # the trail to traverse
        self.grid = grid

        # the number of food pieces this ant has eaten
        self.food_eaten = 0

        # the amount of energy this ant has consumed
        self.energy_consumed = 0

        # the total amount of energy this ant has
        self.total_energy = total_energy

        # the current position of this ant
        self.position = Cell(0, 0)

        # the current orientation of this ant
        self.direction = Direction.EAST

        # a collection of all the cells that this ant visited
        self.ant_path = {self.position}

    def move(self):
        """
        Moves this ant to the cell that is directly in front of it. If there is a food
        pellet on that cell, this ant will eat it.
        """
        if not self.finished():
            self.energy_consumed += 1

            facing_cell = self.get_facing_cell()

            if self.grid.has_food_on(facing_cell):
                self.grid.remove_food_from(facing_cell)
                self.food_eaten += 1

            self.position = facing_cell
            self.ant_path.add(self.position)

    def turn_left(self):
        """
        Turns this ant to the left based on its current direction.
        """
        if not self.finished():
            self.energy_consumed += 1

            if self.direction == Direction.NORTH:
                self.direction = Direction.WEST

            elif self.direction == Direction.SOUTH:
                self.direction = Direction.EAST

            elif self.direction == Direction.EAST:
                self.direction = Direction.NORTH

            else:
                self.direction = Direction.SOUTH

    def turn_right(self):
        """
        Turns this ant to the right based on its current direction.
        """
        if not self.finished():
            self.energy_consumed += 1

            if self.direction == Direction.NORTH:
                self.direction = Direction.EAST

            elif self.direction == Direction.SOUTH:
                self.direction = Direction.WEST

            elif self.direction == Direction.EAST:
                self.direction = Direction.SOUTH

            else:
                self.direction = Direction.NORTH

    def food_ahead(self):
        """
        Returns true if food is on the cell directly in front of this ant.

        :return: true if food is on the cell directly in front of this ant
        """
        facing_cell = self.get_facing_cell()

        return self.grid.has_food_on(facing_cell)

    def get_facing_cell(self):
        """
        Returns the cell that is directly in front of this ant.

        :return: the cell that is directly in front of this ant
        """
        x = self.position.x
        y = self.position.y

        if self.direction == Direction.NORTH:
            y -= 1
            if y < 0:
                y = self.grid.DIMENSION - 1

        elif self.direction == Direction.SOUTH:
            y += 1
            if y > self.grid.DIMENSION - 1:
                y = 0

        elif self.direction == Direction.EAST:
            x += 1
            if x > self.grid.DIMENSION - 1:
                x = 0

        else:
            x -= 1
            if x < 0:
                x = self.grid.DIMENSION - 1

        return Cell(x, y)

    def finished(self):
        """
        Returns true if this ant has finished traversing the given grid i.e. if it has
        used up all of its energy or eaten all the food pellets on the trail.

        :return: true if this ant has finished traversing the given grid
        """
        return self.energy_consumed == self.total_energy or \
               self.food_eaten == self.grid.food_pieces

    def __str__(self):
        """
        Returns a string representation of this ant showing the amount of energy and food
        it consumed, and the path that it took to traverse the grid.

        Visited cells are represented with the letter A, empty cells are shown as dots.

        :return: a string representation of this ant
        """
        ant_string = "Energy consumed: {}\n".format(self.energy_consumed)
        ant_string += "Food eaten: {}\n".format(self.food_eaten)
        ant_string += "Path taken:\n"

        for y in range(self.grid.DIMENSION):
            for x in range(self.grid.DIMENSION):

                if Cell(x, y) in self.ant_path:
                    ant_string += "A"
                else:
                    ant_string += "."

            ant_string += "\n"

        return ant_string
