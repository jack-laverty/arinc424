import arinc424.record as a424
import unittest


class TestRead(unittest.TestCase):

    def test_airway(self):
        with open('./tests/example_data/enroute_airway.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_holding(self):
        with open('./tests/example_data/enroute_holding.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_marker(self):
        with open('./tests/example_data/enroute_marker.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_navaid_ndb(self):
        with open('./tests/example_data/navaid_ndb.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_navaid_vhf(self):
        with open('./tests/example_data/navaid_vhf.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_runway(self):
        with open('./tests/example_data/runway.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_waypoint(self):
        with open('./tests/example_data/enroute_waypoint.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_heliport(self):
        with open('./tests/example_data/heliport.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_heliport_comms(self):
        with open('./tests/example_data/heliport_communications.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)

    def test_airport(self):
        with open('./tests/example_data/airport.txt') as f:
            for idx, line in enumerate(f.readlines()):
                r = a424.Record()
                r.read(line)


if __name__ == '__main__':
    unittest.main()
