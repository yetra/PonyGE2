from fitness.base_ff_classes.base_ff import base_ff

from santa_fe.Ant import Ant
from santa_fe.Trail import Trail


class santa_fe_trail(base_ff):
    """
    A fitness function for the Santa Fe Trail problem.
    """

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

        trail = Trail('/Users/boftherebellion/Desktop/seminar/PonyGE2/datasets/AntTrails/santa_fe_trail.txt')
        d = {'ant': Ant(trail, 630)}

        while not d['ant'].finished():
            exec(phenotype, d)

        # the less uneaten food is left on the trail, the better
        uneaten_food = trail.food_pieces - d['ant'].food_eaten
        fitness = uneaten_food

        return fitness
