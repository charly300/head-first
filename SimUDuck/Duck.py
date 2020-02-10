from abc import ABC, abstractmethod


class Duck(ABC):

    def __init__(self):
        self.flyBehavior = None
        self.quackBehavior = None

    @abstractmethod
    def display(self):
        ...

    def perform_quack(self):
        self.quackBehavior.quack()

    def perform_fly(self):
        self.flyBehavior.fly()

    def swim(self):
        print('I\'m swimming!!')


