import json
import arinc424.decoder as decoder
from collections import defaultdict
from arinc424.decoder import Field
from prettytable import PrettyTable

from arinc424.definitions.GridMORA import GridMORA
from arinc424.definitions.VHFNavaid import VHFNavaid
from arinc424.definitions.NDBNavaid import NDBNavaid
from arinc424.definitions.Waypoint import Waypoint
from arinc424.definitions.AirwaysMarker import AirwaysMarker
from arinc424.definitions.HoldingPattern import HoldingPattern
from arinc424.definitions.PreferredRoute import PreferredRoute
from arinc424.definitions.EnrouteAirways import EnrouteAirways
from arinc424.definitions.EnrouteAirwaysRestriction import EnrouteAirwaysRestriction
from arinc424.definitions.EnrouteCommunications import EnrouteCommunications
from arinc424.definitions.Heliport import Heliport
from arinc424.definitions.HeliportTerminalWaypoint import HeliportTerminalWaypoint
from arinc424.definitions.SIDSTARApproach import SIDSTARApproach
from arinc424.definitions.TAA import TAA
from arinc424.definitions.MSA import MSA
from arinc424.definitions.HeliportCommunications import HeliportCommunications
from arinc424.definitions.Airport import Airport
from arinc424.definitions.AirportGate import AirportGate
from arinc424.definitions.Waypoint import Waypoint
from arinc424.definitions.Runway import Runway
from arinc424.definitions.LocalizerGlideslope import LocalizerGlideslope
from arinc424.definitions.LocalizerMarker import LocalizerMarker
from arinc424.definitions.PathPoint import PathPoint
from arinc424.definitions.FlightPlanning import FlightPlanning
from arinc424.definitions.GLS import GLS
from arinc424.definitions.AirportCommunication import AirportCommunication
from arinc424.definitions.CompanyRoute import CompanyRoute
from arinc424.definitions.Alternate import Alternate
from arinc424.definitions.CruisingTables import CruisingTables
from arinc424.definitions.GeoReferenceTable import GeoReferenceTable
from arinc424.definitions.ControlledAirspace import ControlledAirspace
from arinc424.definitions.FIRUIR import FIRUIR
from arinc424.definitions.RestrictiveAirspace import RestrictiveAirspace
from arinc424.definitions.MLS import MLS

def def_val():
  return False
records = defaultdict(def_val)
records['AS'] = GridMORA()
records['D '] = VHFNavaid()
records['DB'] = NDBNavaid()
records['EA'] = Waypoint(True)
records['EM'] = AirwaysMarker()
records['EP'] = HoldingPattern()
records['ER'] = EnrouteAirways()
records['ET'] = PreferredRoute()
records['EU'] = EnrouteAirwaysRestriction()
records['EV'] = EnrouteCommunications()
records['HA'] = Heliport()
records['HC'] = HeliportTerminalWaypoint()
records['HD'] = SIDSTARApproach()
records['HE'] = SIDSTARApproach()
records['HF'] = SIDSTARApproach()
records['HK'] = TAA(True)
records['HS'] = MSA(True)
records['HV'] = HeliportCommunications()
records['PA'] = Airport()
records['PB'] = AirportGate()
records['PC'] = Waypoint(False)
records['PD'] = SIDSTARApproach()
records['PE'] = SIDSTARApproach()
records['PF'] = SIDSTARApproach()
records['PG'] = Runway()
records['PI'] = LocalizerGlideslope()
records['PK'] = TAA()
records['PL'] = MLS()
records['PM'] = LocalizerMarker()
records['PN'] = NDBNavaid()
records['PP'] = PathPoint()
records['PR'] = FlightPlanning()
records['PS'] = MSA(False)
records['PT'] = GLS()
records['PV'] = AirportCommunication()
records['R '] = CompanyRoute()
records['RA'] = Alternate()
records['TC'] = CruisingTables()
records['TG'] = GeoReferenceTable()
records['UC'] = ControlledAirspace()
records['UF'] = FIRUIR()
records['UR'] = RestrictiveAirspace()

class Record():

  def __init__(self):
    self.ident = ''
    self.raw = ''
    self.continuation = ''
    self.fields = []
    self.definition = -1

  def primary(self):
    if self.definition == -1:
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
    
    if identifier_1 in records:
      self.ident = identifier_1
    elif identifier_2 in records:
      self.ident = identifier_2
    else:
      return False
    
    self.definition = records[self.ident]
    
    # validate the continuation record number
    if hasattr(self.definition, 'cont_idx'):
      self.continuation = self.raw[self.definition.cont_idx]
      if self.continuation.isalnum() == False:
        print(f'Unsupported {self.definition.name} Continuation Record Number: "{self.continuation}"')
        print(f'Valid Continuation Record Numbers are 0, 1, 2 (through 9) A, B, C (through Z)')
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
    table = PrettyTable(field_names=['Field', 'Value', 'Decoded'])
    table.align = 'l'
    for field in self.fields:
      table.add_row([field.name, "'{}'".format(field.value), field.decode(self)])
    if output is True:
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