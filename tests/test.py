import arinc424.record as a424
import unittest


class TestRecordMethods(unittest.TestCase):

    def test_read(self):
        line = 'SSPAD        AA    NZ123480VFU  S51201670E112344910\
    S12016630E174412016E0200120162     FUDAUCKLAND\
                      874487407'
        record = a424.Record()
        self.assertEqual(record.read(line), 0)


if __name__ == '__main__':
    unittest.main()
