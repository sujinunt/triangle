import unittest
from triangle import is_triangle

class TriangleTest(unittest.TestCase):
    # The list of values for your tests can be defined:
    # - outside the class (global variable)
    # - as a class variable (like this)
    # - as a local variable inside the test method.
    # Use which ever is most readable.
    valid_triangles = [
            (1, 1, 1),
            (3, 4, 5),
            (3, 4, 6),
            (8, 10, 12),
            (100, 101, 200),
            (0.9, 1.0, 1.1)
            ]

    not_triangles = [
        (21, 10, 10),
        (2, 1, 1),
        (6, 10, 4),
        (6, 20, 4),
        (1, 2, 4)
    ]

    invalid_argument = [
        (-1, 2, 2),
        ( 1, 0, 2),
        ( 1, -1, 2),
        ( 1, 2, -1),
        ( 1, 2,  0),
        ( -1, -1, -1),
        ( 0, 0, 0)
    ]

    def test_valid_triangle(self):
        """Test a,b,c is triangle"""
        for a,b,c in self.valid_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertTrue( is_triangle(a, b, c), msg)

    def test_not_triangle(self):
        """Test a,b,c is not triangle"""
        for a,b,c in self.not_triangles:
            with self.subTest():
                msg = f"side lengths ({a},{b},{c})"
                self.assertFalse( is_triangle(a, b, c), msg)

    def test_invalid_argument_raises_exception(self):
        """any non-positive argument should raise ValueError"""
        for a,b,c in self.invalid_argument:
            with self.subTest():
                msg = f"ValueError at side lengths ({a},{b},{c})"
                try:
                    self.assertRaises(ValueError, is_triangle, a, b, c)
                except:
                    #If found error, print msg
                    print(msg)
