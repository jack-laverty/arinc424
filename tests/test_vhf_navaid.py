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
        self.assertEqual(r.fields[3][1], '    ')
        self.assertEqual(r.fields[4][1], '  ')
        self.assertEqual(r.fields[5][1], 'ACV ')
        self.assertEqual(r.fields[6][1], 'K2')
        self.assertEqual(r.fields[7][1], '1')
        self.assertEqual(r.fields[8][1], '11020')
        self.assertEqual(r.fields[9][1], 'VD')
        self.assertEqual(r.fields[10][1], 'T')
        self.assertEqual(r.fields[11][1], 'A')
        self.assertEqual(r.fields[12][1], ' ')
        self.assertEqual(r.fields[13][1], 'N40585370')
        self.assertEqual(r.fields[14][1], 'W124062570')
        self.assertEqual(r.fields[15][1], '    ')
        self.assertEqual(r.fields[16][1], 'N40585370')
        self.assertEqual(r.fields[17][1], 'W124062570')
        self.assertEqual(r.fields[18][1], 'E0170')
        self.assertEqual(r.fields[19][1], '00191')
        self.assertEqual(r.fields[20][1], '0')
        self.assertEqual(r.fields[21][1], '  ')
        self.assertEqual(r.fields[22][1], '256')
        self.assertEqual(r.fields[23][1], 'NAS')
        self.assertEqual(r.fields[24][1], 'ARCATA                        ')
        self.assertEqual(r.fields[25][1], '01563')
        self.assertEqual(r.fields[26][1], '8502')


if __name__ == '__main__':
    unittest.main()
