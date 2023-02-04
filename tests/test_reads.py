import arinc424.record as a424
import unittest
import os


class TestRead(unittest.TestCase):

    def test_read(self):
        for file in os.scandir('./tests/example_data/'):
            with open(file) as f:
                tmp = 0
                for idx, line in enumerate(f.readlines()):
                    r = a424.Record()
                    if r.read(line):
                        print()
                        print("------------------------------------")
                        print("Record Type:", r.parse_code())
                        print("------------------------------------")
                        r.dump()
                    else:
                        tmp += 1
                print("\n\nUnknown Records:", tmp)


if __name__ == '__main__':
    unittest.main()
