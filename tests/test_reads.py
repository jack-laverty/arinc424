import unittest
import arinc424.utils as a424


class TestRead(unittest.TestCase):

    # def test_a424(self):
    #     a424.scan_file('./data/ARINC-424-18/airport')

    def test_a424(self):
        a424.scan_folder('./data/ARINC-424-18')

#     def test_cifp(self):
#         a424.scan_folder('./data/CIFP')


if __name__ == '__main__':
    unittest.main()
