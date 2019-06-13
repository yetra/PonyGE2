from santa_fe.Ant import Ant
from santa_fe.Trail import Trail



def main():
    """
    Displays the results of an evolved Santa Fe Trail solution on a specified trail.
    """
    trail = Grid('/Users/boftherebellion/PycharmProjects/PonyGE2/datasets/AntTrails/santa_fe_trail.txt')

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

    print(str(trail))
    print(str(d['ant']))


if __name__ == '__main__':
    main()
