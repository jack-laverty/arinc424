import unittest
import arinc424
import os


class TestDecode(unittest.TestCase):

    def test_airport(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'airport'))

    def test_airport_communications(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'airport_communications'))

    def test_cruising_tables(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'cruising_tables'))

    def test_enroute_airway(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_airway'))

    def test_enroute_airway_restricted(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_airway_restricted'))

    def test_enroute_communications(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_communications'))

    def test_enroute_holding(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_holding'))

    def test_enroute_marker(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_marker'))

    def test_enroute_waypoint(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'enroute_waypoint'))

    def test_fir_uir(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'fir_uir'))

    def test_gates(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'gates'))

    def test_heliport(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'heliport'))

    def test_heliport_communications(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'heliport_communications'))

    def test_instrument_approaches(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'instrument_approaches'))

    def test_localizer_glideslope(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'localizer_glideslope'))

    def test_localizer_marker(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'localizer_marker'))

    def test_mls(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'mls'))

    def test_mora(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'mora'))

    def test_msa(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'msa'))

    def test_navaid_ndb(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'navaid_ndb'))

    def test_navaid_vhf(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'navaid_vhf'))

    def test_restrictive_airspace(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'restrictive_airspace'))

    def test_runway(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'runway'))

    def test_sids(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'sids'))

    def test_stars(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'stars'))

    def test_terminal_waypoint(self):
        os.chdir(os.path.dirname(__file__))
        arinc424.read_file(os.path.join('..', 'data', 'ARINC-424-18', 'terminal_waypoint'))


if __name__ == '__main__':
    unittest.main()
