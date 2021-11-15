class ShellSort():
    """ this uses shell sort algorithm."""

    def __init__(self, list1):
        """ Constructor for the ShellSort class. """
        self.list1 = list1

    def shell_sort(self):
        """ define shell short algorithm. """
        size = len(self.list1)
        gap = size//2

        for i in range(size):
            
