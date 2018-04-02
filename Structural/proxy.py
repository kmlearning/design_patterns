"""
Proxy example implementation

Provides a surrogate/placeholder to provide access to an object
Allows an extra level of indirection to support distributed, 
controlled or conditional access
Adds a wrapper and delegation to protect the real component from 
undue complexity

Usage:
    # Create real subject
    rs = Real_Subject()

    # Create proxy to real subject
    proxy = Proxy(rs)

    # Make request via proxy
    proxy.request()
"""


class Subject_Interface:
    """
    Define the common interface for a Real_Subject and Proxy so that a
    Proxy can be used anywhere a Real_Subject is expected
    """

    def request(self):
        pass


class Proxy(Subject_Interface):
    """
    Maintain a reference that lets the proxy access the real subject
    Provide an interface identical to Subject's
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy may be doing something, like controlling access request")
        self._real_subject.request()


class Real_Subject(Subject_Interface):
    """
    Define the real object that the proxy represents
    """

    def request(self):
        print("The real thing is dealing with the request")
