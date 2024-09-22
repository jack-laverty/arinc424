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
from arinc424.definitions.NDBNavaid import NDBNavaid
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


class Record():

  def __init__(self):
    self.code = ''
    self.raw = ''
    self.fields = []

  def validate(self, line):
    line = line.strip()
    if line.startswith(('S', 'T')) is False:
      # print("Error Parsing: record doesn't start with record type")
      return False
    if len(line) != 132:
      # print("Error Parsing: record not 132 characters in length")
      return False
    if line[-9:].isnumeric() is False:
      # print("Error Parsing: record doesn't end in file record and cycle date")
      return False
    return True

  def read(self, line) -> bool:

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
    records['PN'] = NDBNavaid()  # terminal
    records['PP'] = PathPoint()
    records['PR'] = FlightPlanning()
    records['PS'] = MSA(False)
    records['PT'] = GLS()
    records['PV'] = AirportCommunication()
    records['R '] = CompanyRoute()
    records['RA'] = Alternate()
    records['TC'] = CruisingTables()
    records['TG'] = GeoReferenceTable()
    # records['TN'] = RNAV Name Table (OBSELETE)
    records['UC'] = ControlledAirspace()
    records['UF'] = FIRUIR()
    records['UR'] = RestrictiveAirspace()

    if self.validate(line) is False:
      return False

    self.raw = line.strip()
    x1, x2 = line[4:6], line[4] + line[12]
    if x1 in records.keys():
      self.code = x1
    elif x2 in records.keys():
      self.code = x2
    else:
      return False

    self.fields = records[self.code].read(line)
    if not self.fields:
      return False

    return True

  def decode(self):
    table = PrettyTable(field_names=['Field', 'Value', 'Decoded'])
    table.align = 'l'
    for field in self.fields:
      table.add_row([field.name, "'{}'".format(field.value), field.decode(self)])
    print(table)
    return table.get_string()

  def json(self, single_line=True):
    d = {}
    for field in self.fields:
      d.update({field.name: field.value})
    if single_line:
      return json.dumps(d)
    return json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))