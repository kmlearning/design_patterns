"""
Borg example implementation of a dictionary
Lets a class have as many instances as one likes, 
but ensures they all share the same state

Usage:

    # Create two objects of borg
    b = Borg()
    c = Borg()

    # Returns False, since both distinct objects
    b == c

    # Set b value
    b.val = 3

    # Returns 3, since state shared with b
    print(c.val)

"""


class Borg:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state