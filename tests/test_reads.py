import unittest
import arinc424.record as a424
import os


class TestRead(unittest.TestCase):

    def test_a424(self):
        s = './data/ARINC-424-18'
        for file in os.scandir(s):
            print('\n{:17}{}'.format('reading:', file.name))
            with open(file) as f:
                for line in f.readlines():
                    r = a424.Record()
                    r.read(line)

    def test_cifp(self):
        s = './data/CIFP'
        for file in os.scandir(s):
            print("\nreading: {}".format(file.name))
            with open(file) as f:
                for line in f.readlines():
                    r = a424.Record()
                    r.read(line)


if __name__ == '__main__':
    unittest.main()
