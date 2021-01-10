import logging

from Entities.Animal import Animal, distance


class Wolf(Animal):
    wolf_move_dist = 1.0

    def __init__(self, x=0, y=0, name="Wolf"):
        logging.debug(str(type(self)) + '.__init__(x=' + str(x) + ', y=' + str(y) + ', name=' + name + ')')
        super().__init__(name)
        self.x = 0
        self.y = 0

    # def __str__(self):
    #     return self.name + " " + super().__str__()

    def move(self, x, y):
        logging.debug(str(type(self)) + self.name + '.move()')
        old_position = self.position()
        dist = distance(x, self.x, y, self.y)
        if dist < self.wolf_move_dist:
            self.x = x
            self.y = y
            logging.info(self.name + ' Moved from: ' + str(old_position) + ' to ' + str(self.position()))
            logging.debug('returns True')
            return True
        else:
            a_value = abs(y - self.y)
            b_value = abs(x - self.x)
            a_diff = a_value * self.wolf_move_dist / dist
            b_diff = b_value * self.wolf_move_dist / dist
            if self.y > y:
                self.y -= a_diff
            else:
                self.y += a_diff
            if self.x > x:
                self.x -= b_diff
            else:
                self.x += b_diff
            logging.info(self.name + ' Moved from: ' + str(old_position) + ' to ' + str(self.position()))
