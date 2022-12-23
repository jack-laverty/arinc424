import arinc424.record as a424
import unittest


class TestVHFNavaid(unittest.TestCase):

    def test_file_read(self):
        with open('./tests/example_data/vhf_navaid.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                if idx in range(6):
                    self.assertEqual(r.read(line), None)
                else:
                    self.assertEqual(r.read(line), 0)
                    # self.assertEqual(r.decode(), 0)

    def test_primary(self):
        line = 'SUSAD        ACV   K2111020VDTA N40585370W124062570    \
N40585370W124062570E0170001910  256NASARCATA                        015638502'
        r = a424.Record()
        self.assertEqual(r.read(line), 0)
        self.assertEqual(r.fields[0][1], 'S')
        self.assertEqual(r.fields[1][1], 'USA')
        self.assertEqual(r.fields[2][1], 'D ')


if __name__ == '__main__':
    unittest.main()
