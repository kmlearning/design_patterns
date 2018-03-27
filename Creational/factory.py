"""
Factory example implementation
Example for creating 2d and 3d shapes

Factory provides an interface for creating objects, 
abstracting out the details of dependencies etc

Usage:
    # Create factory
    factory = Shape_Factory()
    
    # Create shape object instance
    # E.g. create a square
    factory.get_shape("square")

    # Call method on shape
    factory.get_shape.draw()
"""

# === Abstract shape classes ===
class Shape_Interface:
    def draw(self):
        pass

# === Concrete shape classes ===
class Circle(Shape_Interface):
    """ Circle object """
    def draw(self):
        print("Circle.draw")


class Square(Shape_Interface):
    """ Square object """
    def draw(self):
        print("Square.draw")


class Shape_Factory():
    """
    Factory for requesting shapes
    """
    @staticmethod
    def get_shape(type):
        if type == "circle":
            return Circle()
        elif type == "square":
            return Square()
        else:
            assert 0, "Could not find shape {}".format(type)