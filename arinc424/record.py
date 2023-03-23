import json
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

ERR_NONE = 0
ERR_INVALID = 1
ERR_UNKNOWN = 2

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
        if line.startswith(('S', 'T')) is False:
            return False
        if len(line) != 132:
            return False
        if line[-9:].isnumeric() is False:
            return False
        return True

    def read(self, line):
        if self.validate(line) is False:
            return ERR_INVALID

        self.raw = line
        x1, x2 = line[4:6], line[4] + line[12]
        if x1 in self.records.keys():
            self.code = x1
        elif x2 in self.records.keys():
            self.code = x2
        else:
            return ERR_UNKNOWN

        self.fields = self.records[self.code].read(line)
        if not self.fields:
            return ERR_UNKNOWN

        return ERR_NONE

    def dump(self):
        s = ''
        for f in self.fields:
            q = "{:<32}: {}".format(f.name, f.value)
            print(q)
            s += q + '\n'
        return s

    def decode(self):
        s = ''
        for f in self.fields:
            q = "{:<32}: {}".format(f.name, f.decode(self))
            print(q)
            s += q + '\n'
        return s

    def json(self, single_line=True):
        d = {}
        for i in self.fields:
            d.update({i.name: i.value})
        if single_line:
            return json.dumps(d)
        else:
            return json.dumps(d,
                              sort_keys=True,
                              indent=4,
                              separators=(',', ': '))
