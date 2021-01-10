import logging

from Entities.Animal import Animal
import random


class Sheep(Animal):
    sheep_move_dist = 0.5

    def __init__(self, name="Sheep"):
        logging.debug(str(type(self)) + '.__init__(name=' + name + ')')
        super().__init__(name)

    def move(self):
        logging.debug(str(type(self)) + self.name + '.move()')
        old_position = self.position()
        directions = ['n', 's', 'w', 'e']
        direct = random.choice(directions)
        if direct == 'n':
            self.y += self.sheep_move_dist
        if direct == 's':
            self.y -= self.sheep_move_dist
        if direct == 'w':
            self.x -= self.sheep_move_dist
        if direct == 'e':
            self.x += self.sheep_move_dist
        logging.info(self.name + ' Moved from: ' + str(old_position) + ' to ' + str(self.position()))
