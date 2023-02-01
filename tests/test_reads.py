import arinc424.record as a424
import unittest
import os


class TestRead(unittest.TestCase):

    def test_read(self):
        for file in os.scandir('./tests/example_data/'):
            with open(file) as f:
                print(file.name)
                for idx, line in enumerate(f.readlines()):
                    r = a424.Record()
                    r.read(line)


if __name__ == '__main__':
    unittest.main()
