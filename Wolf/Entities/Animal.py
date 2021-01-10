import logging
from math import sqrt
import random


def distance(x1, x2, y1, y2):
    logging.debug('distance(x1=' + str(x1) + ', x2=' + str(x2) + ', y1=' + str(y1) + ', y2=' + str(y2) + ')')
    logging.debug('returns ' + str(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))))
    return sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))


class Animal:
    init_pos_limit = 10

    def __init__(self, name):
        logging.debug(str(type(self)) + '.__init__(name=' + name + ')')
        self.x = random.uniform(-self.init_pos_limit, self.init_pos_limit)
        self.y = random.uniform(-self.init_pos_limit, self.init_pos_limit)
        self.lives = True
        self.name = name
        logging.info(self.name + ' Created in position: ' + str(self.position()))

    def __str__(self):
        logging.debug(str(type(self)) + '.__str__()')
        logging.debug('returns ' + self.name + ' [{},{}]'.format(f'{self.x:.3f}', f'{self.y:.3f}'))
        return self.name + ' [{},{}]'.format(f'{self.x:.3f}', f'{self.y:.3f}')

    def position(self):
        logging.debug(str(type(self)) + '.position()')
        logging.debug('returns ' + str(tuple({self.x, self.y})))
        return tuple({self.x, self.y})
