import unittest
import main

class RunTest(unittest.TestCase):
    def test_create_valid_object(self):
        main_object = main.create_object("Stan")
        self.assertEquals(main_object.name, "Stan")

unittest.main()