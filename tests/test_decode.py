import unittest
import arinc424.utils as a424


class TestDecode(unittest.TestCase):

    # def test_0(self):
    #     a424.scan_file_and_dec('./data/ARINC-424-18/airport')

    # def test_1(self):
    #     a424.scan_file_and_dec('./data/ARINC-424-18/airport_communications')

    # def test_2(self):
    #     a424.scan_file_and_dec('./data/ARINC-424-18/cruising_tables')

    # def test_3(self):
    #     a424.scan_file_and_dec('./data/ARINC-424-18/enroute_airway')

    # def test_4(self):
    #     a424.scan_file_and_dec('./data/ARINC-424-18/enroute_airway_restricted')

    def test_5(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_holding')


if __name__ == '__main__':
    unittest.main()
