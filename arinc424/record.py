import json
from collections import defaultdict
from .records import Airport,\
                     Airway,\
                     AirportCommunication,\
                     AirwayRestricted,\
                     AlternateRecord,\
                     CompanyRoute,\
                     ControlledAirspace,\
                     CruisingTables,\
                     EnrouteComms,\
                     FIR_UIR,\
                     FlightPlanning,\
                     AirportGate,\
                     GeoReferenceTable,\
                     GLS,\
                     Heliport,\
                     HeliportComms,\
                     HeliportTerminalWaypoint,\
                     Holding,\
                     LocalizerGlideslope,\
                     LocalizerMarker,\
                     AirwaysMarker,\
                     MLS,\
                     MSA,\
                     MORA,\
                     NDBNavaid,\
                     PathPoint,\
                     PreferredRoute,\
                     RestrictiveAirspace,\
                     Runway,\
                     SIDSTARApp,\
                     TAA,\
                     Waypoint,\
                     VHFNavaid

ERR_NONE = 0
ERR_INVALID = 1
ERR_SECTION_CODE = 2
ERR_APPLICATION_TYPE = 3


class Record():

    def def_val():
        return None

    # 5.5 Subsection Code (SUB CODE)
    records = defaultdict(def_val)
    records['AS'] = MORA()

    records['D '] = VHFNavaid()
    records['DB'] = NDBNavaid()

    records['EA'] = Waypoint(True)
    records['EM'] = AirwaysMarker()
    records['EP'] = Holding()
    records['ER'] = Airway()
    records['ET'] = PreferredRoute()
    records['EU'] = AirwayRestricted()
    records['EV'] = EnrouteComms()

    records['HA'] = Heliport()
    records['HC'] = HeliportTerminalWaypoint()
    records['HD'] = SIDSTARApp()
    records['HE'] = SIDSTARApp()
    records['HF'] = SIDSTARApp()
    records['HK'] = TAA(True)
    records['HS'] = MSA(True)
    records['HV'] = HeliportComms()

    records['PA'] = Airport()
    records['PB'] = AirportGate()
    records['PC'] = Waypoint(False)
    records['PD'] = SIDSTARApp()
    records['PE'] = SIDSTARApp()
    records['PF'] = SIDSTARApp()
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
    records['RA'] = AlternateRecord()

    records['TC'] = CruisingTables()
    records['TG'] = GeoReferenceTable()
    # records['TN'] = RNAV Name Table (OBSELETE)

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
            return ERR_SECTION_CODE

        self.fields = self.records[self.code].read(line)
        if not self.fields:
            return ERR_APPLICATION_TYPE

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
