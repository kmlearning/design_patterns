"""
Singleton example implementation
Ensures a class has only one instance, and 
provides a global point of access to it
Used for example in logging

Usage:
    # Create first instance
    x = Singleton(1)

    # Create another instance with "different" value
    y = Singleton(3)

    # Returns 3, since x and y point to same object
    print(x.val)
"""



class Singleton:

    # None value only ever held before first creation
    __instance = None

    # First step of instance creation, called before __init__
    def __new__(cls, val = None):
        """
        Overwrites default creation method
        Ensures only ever one instance exists
        Any subsequent "creation" simply points to same object
        Returns instance of Singleton class
        """
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance