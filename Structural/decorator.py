"""
Decorator example implementation
Example for creating windows with various features

Attaches additional responsibilities to an object dynamically.
Provides a flexible alternative to subclassing for extended functionality.

Used when subclassing gets overly complex (shared, messy functionality 
across subclasses)

Usage:
    # Create window
    w = window()
    w.build()

    # Add border
    wb = Border_Decorator(w)
    wb.build()

    # Add vertical scroll bar
    wbv = Vertical_SB_Decorator(wb)
    wbv.build()

    # Etc
"""

class Window_Interface:
    def build(self):
        pass


class Abstract_Window_Decorator(Window_Interface):
    """
    Maintain a reference to a Window object and define an interface 
    that conforms to Window's interface.
    """

    def __init__(self, window):
        self._window = window
    
    def build(self):
        pass


class Window(Window_Interface):
    
    def build(self):
        print("Building window")


class Border_Decorator(Abstract_Window_Decorator):

    def add_border(self):
        print("Adding border.")


class Vertical_SB_Decorator(Abstract_Window_Decorator):

    def add_vertical_scroll_bar(self):
        print("Adding vertical scroll bar")

    def build(self):
        self.add_vertical_scroll_bar()
        self._window.build()


class Horizontal_SB_Decorator(Abstract_Window_Decorator):

    def add_horizontal_scroll_bar(self):
        print("Adding horizontal scroll bar")

    def build(self):
        self.add_horizontal_scroll_bar()
        self._window.build()