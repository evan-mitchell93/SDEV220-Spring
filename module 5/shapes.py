import unittest

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(2,5)
    
    def test_area(self):
        self.assertEqual(self.rect.get_area(),10)
    
    def test_type(self):
        self.assertIsInstance(self.rect,Rectangle)

unittest.main()