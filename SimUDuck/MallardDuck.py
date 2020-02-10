from Duck import Duck
from Quack import Quack
from FlyWithWings import FlyWithWings


class MallardDuck(Duck):

    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self):
        print('I\'m a Mallard duck')
