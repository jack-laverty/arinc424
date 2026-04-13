import os
import arinc424
from arinc424.record import Record

RECORD = "SUSAP KSEAK1ASEA     110000119Y N47265700W122182910E019900429250SEA K11800018000CU00Y NAS    SEATTLE-TACOMA INTL           045698808"

def test_read_benchmark(benchmark):
    r = Record()
    benchmark(r.read, RECORD)

def test_json_benchmark(benchmark):
    r = Record()
    r.read(RECORD)
    benchmark(r.json, output=False)

def test_decode_benchmark(benchmark):
    r = Record()
    r.read(RECORD)
    benchmark(r.decode, output=True)

def test_read_file_benchmark(benchmark):
    os.chdir(os.path.dirname(__file__))
    path = os.path.join('..', 'data', 'ARINC-424-18', 'airport_communications')
    benchmark(arinc424.read_file, path, output=False)

def test_faacifp_benchmark(benchmark):
    os.chdir(os.path.dirname(__file__))
    path = os.path.join('..', 'data', 'CIFP', 'FAACIFP18_230223')
    benchmark(arinc424.read_file, path, output=False)