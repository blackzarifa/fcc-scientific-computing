import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        for key, _ in kwargs.items():
            self.contents.append(key)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


if __name__ == '__main__':
    hat1 = Hat(red=5, orange=4)
