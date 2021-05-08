import unittest
from Equations.set_of_equations import set_of_equations


class TestSetEquat(unittest.TestCase):
    def test_no_solutions(self):
        self.assertEqual(set_of_equations(1, 1, 1, 1, 1, 2), None)

    def test_many_solutions(self):
        self.assertEqual(set_of_equations(1, 1, 1, 2, 2, 2), None)

    def test_one_solution(self):
        self.assertEqual(set_of_equations(1, 1, 2, 2, 1, 3), (1.0, 1.0))

    def test_abcdef_incorrect_type_should_raise_error(self):
        cases = [('one', 2, 3, 4, 5, 6),
                 (1, 'two', 3, 4, 5, 6),
                 (1, 2, 'three', 4, 5, 6),
                 (1, 2, 3, 'four', 5, 6),
                 (1, 2, 3, 4, 'five', 6),
                 (1, 2, 3, 4, 5, 'six')]
        for a, b, c, d, e, f in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, set_of_equations, a, b, c, d, e, f)