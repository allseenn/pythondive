# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр, 
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр. 
# Напишите 3-7 тестов unittest для данного класса.
import unittest

class Rectangle:
    def __init__(self, len_rec, width = None):
        self.len_rec = len_rec
        if width is None:
            self.width = len_rec
        else:
            self.width = width
                
    def perimeter(self):
        return 2 * (self.len_rec + self.width)

    def square(self):
        return self.len_rec * self.width
    
    def __add__(self, other):
        return Rectangle(self.len_rec + other.len_rec, self.width + other.width)

    def __sub__(self, other):
        return Rectangle(abs(self.len_rec - other.len_rec), abs(self.width - other.width))
    
    def __eq__(self, other):
        return self.square() == other.square()
    
    def __lt__(self, other):
        return self.square() < other.square()
    
    def __le__(self, other):
        return self.square() <= other.square()
    
    def __ne__(self, other):
        return self.square() != other.square()
    
    def __ge__(self, other):
        return self.square() >= other.square()
    
    def __gt__(self, other):
        return self.square() > other.square()
    
class Test_Rectangle(unittest.TestCase):
    def setUp(self):
        self.rec1 = Rectangle(2,3)
        self.rec2 = Rectangle(2,3)

    def test_perimetr(self):
        self.assertEqual(10, self.rec1.perimeter())

    def test_square(self):
        self.assertEqual(6, self.rec1.square())

    def test_eqal(self):
        self.assertEqual(self.rec1, self.rec2)


        
if __name__ == '__main__':
    unittest.main(verbosity=2)