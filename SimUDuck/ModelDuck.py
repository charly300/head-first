from Duck import Duck
from Quack import Quack
from FlyNoWay import FlyNoWay


class ModelDuck(Duck):

    def __init__(self):
        self.quackBehavior = Quack()
        self.flyBehavior = FlyNoWay()

    def display(self):
        print('I\'m a model duck!')
