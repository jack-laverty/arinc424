import unittest
import arinc424.utils as arinc424
import os


class TestDecode(unittest.TestCase):

    def test_a424(self):
        os.chdir(os.path.dirname(__file__))
        for file in os.scandir('../data/ARINC-424-18'):
            arinc424.read_file_and_dec(file)

    def test_cifp(self):
        os.chdir(os.path.dirname(__file__))
        for file in os.scandir('../data/CIFP'):
            arinc424.read_file_and_dec(file)


if __name__ == '__main__':
    unittest.main()
