import unittest
import arinc424
import os
import time

class TestFAACIFP(unittest.TestCase):

    def _run_file(self, path):
        os.chdir(os.path.dirname(__file__))
        start = time.perf_counter()
        arinc424.read_file(path, False)
        elapsed = time.perf_counter() - start
        print(f"\n{os.path.basename(path)}: parsed in {elapsed:.2f}s")

    def test_belgium(self):
        self._run_file(os.path.join('..', 'data', 'ofm', '2603', 'arinc_eb.pc'))

if __name__ == '__main__':
    unittest.main()