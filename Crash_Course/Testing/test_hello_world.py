import unittest
from hello_world import HelloWorld

class TestHelloWorld(unittest.TestCase):
    """ To test HelloWorld class """
    def test_hello_world(self):
        obj1 = HelloWorld()
        # call method
        result = obj1.hello_world()

        self.assertEqual("Hello World", result)

unittest.main()