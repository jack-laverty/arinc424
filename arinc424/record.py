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
        # print() TODO: Error Handling
        return None

    code_dict = defaultdict(def_val)
    code_dict['D '] = VHFNavaid()
    code_dict['DB'] = NDBNavaid()
    code_dict['EA'] = Waypoint(True)
    code_dict['EM'] = Marker()
    code_dict['EP'] = Holding()
    code_dict['ER'] = Airway()
    code_dict['EU'] = AirwayRestricted()
    code_dict['EV'] = EnrouteComms()
    code_dict['PG'] = Runway()
    code_dict['PA'] = Airport()
    code_dict['PB'] = Gate()
    code_dict['PC'] = Waypoint(False)
    code_dict['PD'] = SIDSTARApp()
    code_dict['PE'] = SIDSTARApp()
    code_dict['PF'] = SIDSTARApp()
    code_dict['PI'] = LocalizerGlideslope()
    code_dict['PL'] = MLS()
    code_dict['PM'] = LocalizerMarker()
    code_dict['PN'] = NDBNavaid()  # terminal
    code_dict['PP'] = PathPoint()
    code_dict['PR'] = FlightPlanning()
    code_dict['PS'] = MSA()
    code_dict['PT'] = GLS()
    code_dict['PV'] = AirportCommunication()
    code_dict['HA'] = Heliport()
    code_dict['HC'] = HeliportTerminalWaypoint()
    code_dict['HV'] = HeliportComms()
    code_dict['TC'] = CruisingTables()
    code_dict['AS'] = MORA()
    code_dict['UC'] = ControlledAirspace()
    code_dict['UF'] = FIR_UIR()
    code_dict['UR'] = RestrictiveAirspace()

    def __init__(self):
        self.code = ''
        self.raw_string = ''
        self.fields = []

    # to quickly discard lines that are not records
    def validate(self, line):
        line = line.strip()
        if line.startswith('S' or 'T') is False:
            # print("Not S or T")
            return False
        if len(line) != 132:
            # print("Not 132")
            return False
        if line[-9:].isnumeric() is False:
            # print("Not last 9 chars numeric")
            return False
        return True

    def read(self, line):
        self.raw_string = line
        match line[4]:
            case 'D' | 'E' | 'A' | 'T' | 'U':
                self.code = line[4:6]
            case 'P' | 'H':
                self.code = line[4] + line[12]
            case _:
                return False

        x = self.code_dict[self.code]
        if x is None:
            return False

        self.fields = x.read(line)
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
