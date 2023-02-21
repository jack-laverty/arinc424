import unittest
import arinc424.utils as a424


class TestDecode(unittest.TestCase):

    def test_decode_aiport(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport')

    def test_decode_airport_comms(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport_communications')


if __name__ == '__main__':
    unittest.main()
