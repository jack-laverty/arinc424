import unittest
import arinc424.utils as a424


class TestRead(unittest.TestCase):

    def test_a424(self):
        a424.scan_folder('./tests/example_data/ARINC-424-18')

    def test_cifp(self):
        a424.scan_folder('./tests/example_data/CIFP')


if __name__ == '__main__':
    unittest.main()
