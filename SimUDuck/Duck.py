from abc import ABC, abstractmethod

class Duck(ABC):
    
    @abstractmethod
    def display(self):
        ...
    
    def quack(self):
        print('I\'m a dock, quack!!')

    def swim(self):
        print('I\'m swimming!!')

    def fly(self):
        print('I\'m flying')