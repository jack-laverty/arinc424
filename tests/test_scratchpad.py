import unittest
import arinc424.record as a424


class TestRead(unittest.TestCase):

    def test_read(self):
        # with open('./data/CIFP/FAACIFP18_230126') as f:
        with open('./data/ARINC-424-18/airport') as f:
            for line in f.readlines():
                r = a424.Record()
                if r.read(line):
                    print()
                    r.decode()


if __name__ == '__main__':
    unittest.main()
