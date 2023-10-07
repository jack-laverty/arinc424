import unittest
import arinc424
import os


class TestDecode(unittest.TestCase):

    def test_a424(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_folder(os.path.join('..', 'data', 'ARINC-424-18'))

    def test_cifp(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_folder(os.path.join('..', 'data', 'CIFP'))


if __name__ == '__main__':
    unittest.main()
