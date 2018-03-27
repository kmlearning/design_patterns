"""
Abstract Factory example implementation
Example for creating 2d and 3d shapes

Abstract Factory provides an interface for creating families of 
related objects without specifying their concrete classes

Usage:
    # Create abstract factory
    # E.g. 3d shape factory
    ab_factory = Shape_3D_Factory()
    
    # Create shape object instance
    # E.g. create a sphere
    ab_factory.get_shape(1)

    # Call method on shape
    ab_factory.get_shape.draw()
"""


# === Abstract shape classes ===
class Shape_2D_Interface:
    def draw(self):
        pass


class Shape_3D_Interface:
    def draw(self):
        pass


# === Concrete shape classes ===
class Circle(Shape_2D_Interface):
    def draw(self):
        print("Circle.draw")


class Square(Shape_2D_Interface):
    def draw(self):
        print("Square.draw")


class Sphere(Shape_3D_Interface):
    def build(self):
        print("Sphere.build")


class Cube(Shape_3D_Interface):
    def build(self):
        print("Cube.build")


# === Abstract shape factory ===
class Shape_Factory_Interface:
    @staticmethod
    def get_shape(sides):
        pass

# === Concrete shape classes
class Shape_2d_Factory(Shape_Factory_Interface):
    @staticmethod
    def get_shape(sides):
        pass


class Shape_2D_Factory(Shape_Factory_Interface):
    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        elif sides == 4:
            return Square()
        assert 0, "Bad 2d shape creation: shape not defined for {} sides".format(sides)


class Shape_3D_Factory(Shape_Factory_Interface):
    @staticmethod
    def get_shape(sides):
        """ Sides = number of faces """
        if sides == 1:
            return Sphere()
        elif sides == 6:
            return Cube()
        assert 0, "Bad 3D shape creation: shape not defined for {} faces".format(sides)

