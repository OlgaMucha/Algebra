from bin_to_dec import binary_to_decimal, decimal_to_binary, hexidecimal_to_decimal, decimal_to_hexidecimal
import unittest


def setUpModule():
    print('Setting up...')

def tearDownModule():
    print('Tearing down...')

class convertion(unittest.TestCase):

    def test_binary_to_dec_value(self):
        self.assertEqual(binary_to_decimal('1111'),15)

    def test_dec_to_binary_value(self):
        self.assertEqual(decimal_to_binary('15'),1111)

    def test_hex_to_dec_value(self):
        self.assertEqual(hexidecimal_to_decimal('b4'),180)

    def test_dec_to_hex_value(self):
        self.assertEqual(hexidecimal_to_decimal('180'),384)

    def test_incorrect_value_raise_error(self):
        self.assertRaises(TypeError, binary_to_decimal(12))
        self.assertRaises(ValueError, decimal_to_binary(gg))
        self.assertRaises(ValueError, hexidecimal_to_decimal(gg))
        self.assertRaises(ValueError, decimal_to_hexidecimal(gg))

