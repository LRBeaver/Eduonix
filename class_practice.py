__author__ = 'lyndsay.beaver'

class vehicle():
    wheels = 4
    def __init__(self):
        print("Vehicle")
    def calcVelocity(self,x):
        return 3*x+10

class Car(vehicle):
    def __init__(self):
        self.speed = 10


exampleCar = Car()

print(exampleCar.speed)
print(exampleCar.calcVelocity(20))
print(exampleCar.wheels)