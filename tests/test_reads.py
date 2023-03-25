import unittest
import arinc424.record as a424
import os


class TestRead(unittest.TestCase):

    def test_a424(self):
        s = './data/ARINC-424-18'
        f2 = open('./UNKNOWN_' + s.rsplit('/', 1)[-1], 'w')
        for file in os.scandir(s):
            t, k, u = 0, 0, 0
            print('\n{:17}{}'.format('reading:', file.name))
            with open(file) as f:
                for line in f.readlines():
                    t += 1
                    r = a424.Record()
                    q = r.read(line)
                    if q != a424.ERR_INVALID:
                        k += 1
                        if q == a424.ERR_SECTION_CODE or q == a424.ERR_APPLICATION_TYPE:
                            u += 1
                            f2.write(r.code + '\n')
                            f2.write(line)
            print('{:17}{}'.format('lines:', t))
            print('{:17}{}'.format('records:', k))
            print('{:17}{}'.format('unknown:', u))
        f2.close()

    def test_cifp(self):
        s = './data/CIFP'
        f2 = open('./UNKNOWN_' + s.rsplit('/', 1)[-1], 'w')
        for file in os.scandir(s):
            t, k, u = 0, 0, 0
            print("\nreading: {}".format(file.name))
            with open(file) as f:
                for line in f.readlines():
                    t += 1
                    r = a424.Record()
                    q = r.read(line)
                    if q != a424.ERR_INVALID:
                        k += 1
                        if q == a424.ERR_SECTION_CODE or q == a424.ERR_APPLICATION_TYPE:
                            u += 1
                            f2.write(r.code + '\n')
                            f2.write(line)
            print('{:17}{}'.format('lines:', t))
            print('{:17}{}'.format('records:', k))
            print('{:17}{}'.format('unknown:', u))
        f2.close()


if __name__ == '__main__':
    unittest.main()
