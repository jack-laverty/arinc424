import json
from prettytable import PrettyTable

from arinc424.definitions.grid_mora import GridMORA
from arinc424.definitions.vhf_navaid import VHFNavaid
from arinc424.definitions.ndb_navaid import NDBNavaid
from arinc424.definitions.waypoint import Waypoint
from arinc424.definitions.airways_marker import AirwaysMarker
from arinc424.definitions.holding_pattern import HoldingPattern
from arinc424.definitions.preferred_route import PreferredRoute
from arinc424.definitions.enroute_airways import EnrouteAirways
from arinc424.definitions.enroute_airways_restricted import EnrouteAirwaysRestriction
from arinc424.definitions.enroute_communications import EnrouteCommunications
from arinc424.definitions.heliport import Heliport
from arinc424.definitions.heliport_terminal_waypoint import HeliportTerminalWaypoint
from arinc424.definitions.sid_star_approach import SIDSTARApproach
from arinc424.definitions.taa import TAA
from arinc424.definitions.msa import MSA
from arinc424.definitions.heliport_communications import HeliportCommunications
from arinc424.definitions.airport import Airport
from arinc424.definitions.airport_gate import AirportGate
from arinc424.definitions.runway import Runway
from arinc424.definitions.localizer_glideslope import LocalizerGlideslope
from arinc424.definitions.localizer_marker import LocalizerMarker
from arinc424.definitions.pathpoint import PathPoint
from arinc424.definitions.flight_planning import FlightPlanning
from arinc424.definitions.gls import GLS
from arinc424.definitions.airport_communication import AirportCommunication
from arinc424.definitions.company_route import CompanyRoute
from arinc424.definitions.alternate import Alternate
from arinc424.definitions.cruising_tables import CruisingTables
from arinc424.definitions.geo_reference_table import GeoReferenceTable
from arinc424.definitions.controlled_airspace import ControlledAirspace
from arinc424.definitions.fir_uir import FIRUIR
from arinc424.definitions.restrictive_airspace import RestrictiveAirspace
from arinc424.definitions.mls import MLS


records = {
  'AS': GridMORA(),
  'D ': VHFNavaid(),
  'DB': NDBNavaid(),
  'EA': Waypoint(True),
  'EM': AirwaysMarker(),
  'EP': HoldingPattern(),
  'ER': EnrouteAirways(),
  'ET': PreferredRoute(),
  'EU': EnrouteAirwaysRestriction(),
  'EV': EnrouteCommunications(),
  'HA': Heliport(),
  'HC': HeliportTerminalWaypoint(),
  'HD': SIDSTARApproach(),
  'HE': SIDSTARApproach(),
  'HF': SIDSTARApproach(),
  'HK': TAA(True),
  'HS': MSA(True),
  'HV': HeliportCommunications(),
  'PA': Airport(),
  'PB': AirportGate(),
  'PC': Waypoint(False),
  'PD': SIDSTARApproach(),
  'PE': SIDSTARApproach(),
  'PF': SIDSTARApproach(),
  'PG': Runway(),
  'PI': LocalizerGlideslope(),
  'PK': TAA(),
  'PL': MLS(),
  'PM': LocalizerMarker(),
  'PN': NDBNavaid(),
  'PP': PathPoint(),
  'PR': FlightPlanning(),
  'PS': MSA(False),
  'PT': GLS(),
  'PV': AirportCommunication(),
  'R ': CompanyRoute(),
  'RA': Alternate(),
  'TC': CruisingTables(),
  'TG': GeoReferenceTable(),
  'UC': ControlledAirspace(),
  'UF': FIRUIR(),
  'UR': RestrictiveAirspace()
}


class Record():

  def reset(self):
      self.ident = ''
      self.raw = ''
      self.continuation = ''
      self.fields = []
      self.definition = None

  def __init__(self):
      self.reset()

  def primary(self):
    if self.definition is None:
      return False
    return self.continuation == '0' or self.continuation == '1'

  def hasCont(self):
    if self.primary() is False:
      return False
    return self.continuation == '1'

  def validate(self, line):
    line = line.strip()
    if line.startswith(('S', 'T')) is False:
      return False
    if len(line) != 132:
      return False
    if line[-9:].isnumeric() is False:
      return False
    return True

  def read(self, line) -> bool:

    if self.validate(line) is False:
      return False

    # remove any surrounding whitespace
    self.raw = line.strip()

    identifier_1 = line[4:6]
    identifier_2 = line[4] + line[12]

    # After
    self.definition = records.get(identifier_1) or records.get(identifier_2)
    if self.definition is None:
        return False
    self.ident = identifier_1 if identifier_1 in records else identifier_2

    # validate the continuation record number
    if hasattr(self.definition, 'cont_idx'):
      self.continuation = self.raw[self.definition.cont_idx]
      if self.continuation.isalnum() is False:
        print(f'Unsupported {self.definition.name} Continuation Record Number: "{self.continuation}"')
        print('Valid Continuation Record Numbers are 0, 1, 2 (through 9) A, B, C (through Z)')
        print(f'Record: {self.raw}')
        return False

      # validate the continuation record type
      if self.primary() is False:
        if hasattr(self.definition, 'app_idx'):
          application_type = self.definition.application_type(self.raw)
          if (application_type not in self.definition.continuations) and not 'J':
            print(f'Unsupported {self.definition.name} Application Type: "{application_type}"')
            print(f'Supported application types for {self.definition.name} are: {self.definition.continuations}')
            print(f'Record: {self.raw}')
            return False
        else:
          raise ValueError("no hasattr(self.definition, 'app_idx')")

    # read the record into a record object based on identifier
    self.fields = self.definition.read(line, self.primary())
    if not self.fields:
      return False

    return True

  def decode(self, output=True):
    if not output:
        return ''
    table = PrettyTable(field_names=['Field', 'Value', 'Decoded'])
    table.align = 'l'
    for field in self.fields:
        table.add_row([field.name, "'{}'".format(field.value), field.decode(self)])
    print(table)
    return table.get_string()

  def json(self, output=True, single_line=True):
    d = {}
    for field in self.fields:
      d.update({field.name: field.value})
    if single_line:
      data = json.dumps(d)
    else:
      data = json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))

    if output is True:
      print(data)

    return data
