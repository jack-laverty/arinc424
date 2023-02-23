import unittest
import arinc424.utils as a424


class TestDecode(unittest.TestCase):

    def test_0(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport')

    def test_1(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport_communications')

    def test_2(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/cruising_tables')


if __name__ == '__main__':
    unittest.main()
