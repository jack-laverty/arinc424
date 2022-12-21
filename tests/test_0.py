import arinc424.record as a424
import unittest


class TestVHFNavaid(unittest.TestCase):

    def test_read(self):
        with open('./tests/example_data/vhf_navaid.txt') as f:
            for idx, line in enumerate(f.readlines()):
                print("\nLine", idx)
                record = a424.Record()
                self.assertEqual(record.read(line), 0)


if __name__ == '__main__':
    unittest.main()
