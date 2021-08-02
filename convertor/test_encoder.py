import unittest

from encode_convertor import Encoder


class TestEncoder(unittest.TestCase):
    def test_convert_text(self):
        encoder = Encoder('convertor/key')
        self.assertEqual('this is a test task', encoder.convert_text('7#!5 !5 4 7357 745|<'))


if __name__ == '__main__':
    unittest.main()