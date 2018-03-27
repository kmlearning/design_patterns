"""
Protype pattern example implementation using a point
Real use would be something costly to set up

Specifies the kinds of objects to use a prototypical instance, 
and create new objects by copying this protoype (though changes allowed)
Useful when object creation is costly, e.g. heavy config setup required

Usage:
    # Original point
    p0 = point(0,0)

    # Create cloned point at different point in plane
    p1 = p0.clone
"""

from copy import deepcopy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print("({}, {})".format(self.x, self.y))

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj