from MallardDuck import MallardDuck
from ModelDuck import ModelDuck
from FlyRocketPowered import FlyRocketPowered

mallard = MallardDuck()
mallard.display()
mallard.perform_fly()
mallard.perform_quack()

model = ModelDuck()
model.display()
model.perform_fly()
model.perform_quack()
model.flyBehavior = FlyRocketPowered()
model.perform_fly()
