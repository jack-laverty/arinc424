import arinc424.record as a424
import unittest
import os


class TestRead(unittest.TestCase):

    def test_read(self):
        for file in os.scandir('./tests/example_data/'):
            with open(file) as f:
                for idx, line in enumerate(f.readlines()):
                    r = a424.Record()
                    if r.read(line):
                        print()
                        print("------------------------------------")
                        print("Record Type:", r.parse_code())
                        print("------------------------------------")
                        r.dump()


if __name__ == '__main__':
    unittest.main()
