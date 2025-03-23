import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, _ in kwargs.items():
            self.contents.append(key)

    def draw(self, amount):
        removed_balls = []

        for i in range(amount):
            index = random.randint(0, len(self.contents) - 1)
            removed_balls.append(self.contents.pop(index))

        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == '__main__':
    hat1 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    hat1.draw(1)
