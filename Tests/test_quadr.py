import unittest
from quadratic import quadratic


class TestQuadratic(unittest.TestCase):
    def test_a_is_0(self):
        self.assertEqual(quadratic(0, 1, 1), -1)

    def test_delta_less_then_0(self):
        self.assertEqual(quadratic(1, 0, 1), None)

    def test_abc_incorrect_type_should_raise_error(self):
        cases = [('one', 2, 3),
                 (1, 'two', 3),
                 (1, 2, 'three')]
        for x, y, z in cases:
            with self.subTest(cases=cases):
                self.assertRaises(TypeError, quadratic, x, y, z)

    def test_delta_is_0(self):
        self.assertEqual(quadratic(1, 2, 1), -1.0)

    def test_delta_is_greater_then_0(self):
        self.assertEqual(quadratic(1, 5, 6), (-3.0, -2.0))

    def test_abc_is_000(self):
        self.assertEqual(quadratic(0, 0, 0), None)

    def test_abc_is_00c(self):
        self.assertEqual(quadratic(0, 0, 5), None)