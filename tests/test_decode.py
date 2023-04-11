import unittest
import arinc424.utils as a424
import os


class TestDecode(unittest.TestCase):

    def test_a424(self):
        s = './data/ARINC-424-18'
        for file in os.scandir(s):
            a424.read_file_and_dec(file)

    def test_cifp(self):
        s = './data/CIFP'
        for file in os.scandir(s):
            a424.read_file_and_dec(file)


if __name__ == '__main__':
    unittest.main()
