"""
Builder example implementation
Example uses

Separate construction of a complex object from its representation
so that the same construction process can create different representations
Similar to abstract factory, but useful when a lot of steps are needed
to create an object

Usage:
    # Create director object
    director = Director()

    # Set jeep car recipe
    director.set_builder(Jeep_Builder())

    # Create a jeep
    director.get_car()

    # Get specifications for jeep
    director.get_car().specification()
"""

class Car:

    def __init__(self):
        """ Internal representation of car """
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: {}".format(self.__engine.horsepower))
        print("engine horsepower: {}".format(self.__engine.horsepower))
        print("tire size: {}".format(self.__wheels[0].size))
    

# === Car parts ===
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:
    """ Director object, top level abstraction """
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        """ Process for assembling car """
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1

        return car


class Builder_Interface:
    """ Interface template for builder """
    def get_wheel(self):
        pass
    
    def get_engine(self):
        pass
    
    def get_body(self):
        pass

    
class Jeep_Builder(Builder_Interface):
    """ Create jeep type car """
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


class Nissan_Builder(Builder_Interface):
    """ Create nissan type car """
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def get_body(self):
        body = Body()
        body.shape = "hatchback"
        return body
        