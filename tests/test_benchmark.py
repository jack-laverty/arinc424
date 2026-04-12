import os
import arinc424
from arinc424.record import Record

def test_decode_airport_benchmark(benchmark):
    r = Record()
    r.read("SUSAP KSEAK1ASEA     110000119Y N47265700W122182910E019900429250SEA K11800018000CU00Y NAS    SEATTLE-TACOMA INTL           045698808")
    benchmark(r.decode, output=False)

def test_read_file_benchmark(benchmark):
    os.chdir(os.path.dirname(__file__))
    path = os.path.join('..', 'data', 'ARINC-424-18', 'airport_communications')
    benchmark(arinc424.read_file, path, output=False)