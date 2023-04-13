import unittest
import arinc424.utils as a424
import os


class TestDecode(unittest.TestCase):

    def test_a424(self):
        for file in os.scandir('./data/ARINC-424-18'):
            a424.read_file_and_dec(file)

    def test_cifp(self):
        for file in os.scandir('./data/CIFP'):
            a424.read_file_and_dec(file)


if __name__ == '__main__':
    unittest.main()
