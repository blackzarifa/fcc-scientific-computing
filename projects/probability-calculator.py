import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, amount):
        if amount >= len(self.contents):
            return self.contents

        removed_balls = []
        for i in range(amount):
            index = random.randint(0, len(self.contents) - 1)
            removed_balls.append(self.contents.pop(index))
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_experiments == 0:
        return 0

    got_expected = 0
    for experiment in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        drawn_dict = {}
        for i in drawn:
            drawn_dict[i] = drawn_dict.get(i, 0) + 1

        all_met = True
        for color, count in expected_balls.items():
            if drawn_dict.get(color, 0) < count:
                all_met = False
                break

        if all_met:
            got_expected += 1

    return got_expected / num_experiments


if __name__ == '__main__':
    hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    expected_balls = {'red': 2}
    print(experiment(hat1, expected_balls, 5, 500))
