from fitness.base_ff_classes.base_ff import base_ff

from utilities.santa_fe.Ant import Ant
from utilities.santa_fe.Grid import Grid

from pathlib import Path


class santa_fe_trail(base_ff):
    """
    A fitness function for the Santa Fe Trail problem.
    """

    base_path = Path(__file__).parents[2]
    grid_def_path = (base_path / "datasets/AntTrails/santa_fe_trail.txt").resolve()

    def __init__(self):
        """
        Initialise the base fitness function class.
        """
        super().__init__()

    def evaluate(self, ind, **kwargs):
        """
        Calculates the fitness of a given individual.

        :param ind: the individual whose fitness should be calculated
        :param kwargs: the keyword arguments, not used
        :return: the calculated fitness
        """
        phenotype = ind.phenotype

        trail = Grid(santa_fe_trail.grid_def_path)
        d = {'ant': Ant(trail, 630)}

        while not d['ant'].finished():
            exec(phenotype, d)

        # the less uneaten food is left on the trail, the better
        uneaten_food = trail.food_pieces - d['ant'].food_eaten
        fitness = uneaten_food

        return fitness
