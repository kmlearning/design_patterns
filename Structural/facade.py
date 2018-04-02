"""
Facade example implementation
Example for creating a car

Provides a unified interface to a set of interfaces in a subsystem.
Defines a higher level interface that makes the subsystem easier to use.
Can make a more complicated library easier to use, providing a facade for common tasks,
or provide a well-designed API wrapper around several badly designed APIs

Usage:
    # Create car object
    c = Car()

    # Interact with car object via facade
    c.turn_key()
    c.jump()
"""

class Engine:

    def __init__(self):
        """ Speed of motor in rpm """
        self.rpm = 0

    def start(self, rpm):
        self.rpm = min(rpm, 3000)


class Starter_Moter:

    def __init__(self):
        """ Speed of motor in rpm """
        self.rpm = 0

    def start(self, charge):
        """ If there is enough power, spin quickly """
        if (charge > 50):
            self.rpm = 25000


class Battery:

    def __init__(self):
        """ % charged, started flat """
        self.charge = 0


class Car:
    """ Facade object dealing with the battery, engine and starter motor """

    def __init__(self):
        self.battery = Battery()
        self.starter = Starter_Moter()
        self.engine = Engine()

    def turn_key(self):
        self.starter.start(self.battery.charge)
        self.engine.start(self.starter.rpm)
        if (self.engine.rpm > 0):
            print("Engine started")
        else:
            print("Engine not started")

    def jump(self):
        self.battery.charge = 100
        print("Jumped")