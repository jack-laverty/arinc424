import json
from .decoder import decode_fn
from .decoder import section
from collections import defaultdict
from .records import Airport,\
                     Airway,\
                     AirportCommunication,\
                     AirwayRestricted,\
                     ControlledAirspace,\
                     CruisingTables,\
                     EnrouteComms,\
                     FIR_UIR,\
                     FlightPlanning,\
                     Gate,\
                     GLS,\
                     Heliport,\
                     HeliportComms,\
                     HeliportTerminalWaypoint,\
                     Holding,\
                     LocalizerGlideslope,\
                     LocalizerMarker,\
                     Marker,\
                     MLS,\
                     MSA,\
                     MORA,\
                     NDBNavaid,\
                     PathPoint,\
                     RestrictiveAirspace,\
                     Runway,\
                     SIDSTARApp,\
                     Waypoint,\
                     VHFNavaid


class Record():

    def def_val():
        return None

    records = defaultdict(def_val)
    records['D '] = VHFNavaid()
    records['DB'] = NDBNavaid()
    records['EA'] = Waypoint(True)
    records['EM'] = Marker()
    records['EP'] = Holding()
    records['ER'] = Airway()
    records['EU'] = AirwayRestricted()
    records['EV'] = EnrouteComms()
    records['PG'] = Runway()
    records['PA'] = Airport()
    records['PB'] = Gate()
    records['PC'] = Waypoint(False)
    records['PD'] = SIDSTARApp()
    records['PE'] = SIDSTARApp()
    records['PF'] = SIDSTARApp()
    records['HD'] = SIDSTARApp()
    records['HE'] = SIDSTARApp()
    records['HF'] = SIDSTARApp()
    records['PI'] = LocalizerGlideslope()
    records['PL'] = MLS()
    records['PM'] = LocalizerMarker()
    records['PN'] = NDBNavaid()  # terminal
    records['PP'] = PathPoint()
    records['PR'] = FlightPlanning()
    records['PS'] = MSA(False)
    records['PT'] = GLS()
    records['PV'] = AirportCommunication()
    records['HA'] = Heliport()
    records['HC'] = HeliportTerminalWaypoint()
    records['HS'] = MSA(True)
    records['HV'] = HeliportComms()
    records['TC'] = CruisingTables()
    records['AS'] = MORA()
    records['UC'] = ControlledAirspace()
    records['UF'] = FIR_UIR()
    records['UR'] = RestrictiveAirspace()

    def __init__(self):
        self.code = ''
        self.raw = ''
        self.fields = []

    def validate(self, line):
        line = line.strip()
        if line.startswith('S' or 'T') is False:
            return False
        if len(line) != 132:
            return False
        if line[-9:].isnumeric() is False:
            return False
        return True

    def read(self, line):
        self.raw = line
        x1, x2 = line[4:6], line[4] + line[12]
        if x1 in self.records.keys():
            self.code = x1
        elif x2 in self.records.keys():
            self.code = x2
        else:
            return False
        self.fields = self.records[self.code].read(line)
        if self.fields is None:
            return False
        return True

    def parse_code(self):
        return section(self.code)

    def dump(self):
        for i in self.fields:
            print("{:<32}: {}".format(i[0], i[1]))

    def decode(self):
        for i in self.fields:
            print("{:<32}: {}".format(i[0], decode_fn[i[0]](i[1])))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record,
                              sort_keys=True,
                              indent=4,
                              separators=(',', ': '))
