from utilities.santa_fe.Ant import Ant
from utilities.santa_fe.Grid import Grid

from pathlib import Path

base_path = Path(__file__).parents[3]
file_path = (base_path / "datasets/AntTrails/santa_fe_trail.txt").resolve()


def main():
    """
    Displays the results of an evolved Santa Fe Trail solution on a specified trail.
    """
    trail = Grid(file_path)

    # original trail
    print(str(trail))

    d = {'ant': Ant(trail, 600)}

    while not d['ant'].finished():
        exec('''if ant.food_ahead():
  ant.move()
else:
  ant.turn_right()
  if ant.food_ahead():
    ant.turn_left()
  else:
    ant.turn_right()
    ant.turn_right()
  if ant.food_ahead():
    ant.move()
    ant.move()
  else:
    ant.turn_right()
    ant.move()
''', d)

    # uneaten food left on the trail
    uneaten_food = trail.food_pieces - d['ant'].food_eaten
    print("Uneaten food: {}".format(uneaten_food))
    print(str(trail))

    # path taken by the ant
    print(str(d['ant']))


if __name__ == '__main__':
    main()
