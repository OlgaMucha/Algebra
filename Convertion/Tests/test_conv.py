from bin_to_dec import binary_to_decimal, decimal_to_binary, hexadecimal_to_decimal, decimal_to_hexadecimal
import unittest


def setUpModule():
    print('Setting up...')

def tearDownModule():
    print('Tearing down...')

class convertion(unittest.TestCase):

    def test_binary_to_dec_value(self):
        self.assertEqual(binary_to_decimal('1111'),15)
        self.assertEqual(binary_to_decimal('0'), 0)

    def test_dec_to_binary_value(self):
        self.assertEqual(decimal_to_binary('15'),1111)
        self.assertEqual(decimal_to_binary('0'), 0)

    def test_hex_to_dec_value(self):
        self.assertEqual(hexadecimal_to_decimal('b4'),180)
        self.assertEqual(hexadecimal_to_decimal('0'), 0)

    def test_dec_to_hex_value(self):
        self.assertEqual(hexadecimal_to_decimal('180'),384)
        self.assertEqual(hexadecimal_to_decimal('1'), 1)

    def test_incorrect_value_returns_none(self):
        self.assertEqual(binary_to_decimal('12'), None)
        self.assertEqual(decimal_to_binary('gg'), None)
        self.assertEqual(hexadecimal_to_decimal('gg'), None)
        self.assertEqual(decimal_to_hexadecimal('gg'), None)

