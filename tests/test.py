import arinc424.record as a424
import unittest


class TestVHFNavaid(unittest.TestCase):

    def test_read(self):
        with open('./example_data/vhf_navaid.txt') as f:
            for idx, line in enumerate(f.readlines()):
                record = a424.Record()
                self.assertEqual(record.read(line), 0)
                print("\nLine", idx)
                record.dump()


if __name__ == '__main__':
    unittest.main()
