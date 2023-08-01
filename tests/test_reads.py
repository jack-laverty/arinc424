import unittest
import arinc424.record as arinc424
import os


class TestRead(unittest.TestCase):

    def test_a424(self):
        os.chdir(os.path.dirname(__file__))
        for file in os.scandir('../data/ARINC-424-18'):
            print('{:17}{}'.format('reading:', file.name))
            with open(file) as f:
                for line in f.readlines():
                    r = arinc424.Record()
                    r.read(line)

    def test_cifp(self):
        os.chdir(os.path.dirname(__file__))
        for file in os.scandir('../data/CIFP'):
            print("reading: {}".format(file.name))
            with open(file) as f:
                for line in f.readlines():
                    r = arinc424.Record()
                    r.read(line)


if __name__ == '__main__':
    unittest.main()
