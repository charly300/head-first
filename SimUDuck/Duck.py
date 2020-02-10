from abc import ABC, abstractmethod


class Duck(ABC):

    def __init__(self):
        self._flyBehavior = None
        self._quackBehavior = None

    @abstractmethod
    def display(self):
        ...

    @property
    def flyBehavior(self):
        return self._flyBehavior

    @flyBehavior.setter
    def flyBehavior(self, value):
        self._flyBehavior = value

    def perform_quack(self):
        self.quackBehavior.quack()

    def perform_fly(self):
        self.flyBehavior.fly()

    def swim(self):
        print('I\'m swimming!!')


