import arinc424.record as a424
import unittest
import os


class TestRead(unittest.TestCase):

    def test_read(self):
        k, u = 0, 0
        for file in os.scandir('./tests/example_data/'):
            with open(file) as f:
                for idx, line in enumerate(f.readlines()):
                    r = a424.Record()
                    if r.validate(line):
                        if r.read(line):
                            print()
                            print("------------------------------------")
                            print("Record Type:", r.parse_code())
                            print("------------------------------------")
                            r.dump()
                            k += 1
                        else:
                            u += 1
                    else:
                        print(line)
        print('\n{:9}{}\n{:9}{}'.format('Parsed:', k,
                                        'Unknown:', u))


if __name__ == '__main__':
    unittest.main()
