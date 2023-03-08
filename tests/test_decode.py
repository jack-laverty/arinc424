import unittest
import arinc424.utils as a424


class TestDecode(unittest.TestCase):

    def test_0(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport')

    def test_1(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/airport_communications')

    def test_2(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/cruising_tables')

    def test_3(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_airway')

    def test_4(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_airway_restricted')

    def test_5(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_holding')

    def test_6(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_marker')

    def test_7(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/enroute_waypoint')

    def test_8(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/fir_uir')

    def test_9(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/gates')

    def test_10(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/heliport')

    def test_11(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/heliport_communications')

    def test_12(self):
        a424.scan_file_and_dec('./data/ARINC-424-18/instrument_approaches')


if __name__ == '__main__':
    unittest.main()
