import json
from .decoder import decode_fn
from .decoder import section
from collections import defaultdict
from .records import VHFNavaid,\
                     NDBNavaid,\
                     Waypoint,\
                     Marker,\
                     Holding,\
                     Airway,\
                     AirwayRestricted,\
                     Runway,\
                     Airport,\
                     Heliport,\
                     HeliportComms,\
                     Mora,\
                     FlightPlanning,\
                     SIDSTARApp,\
                     CruisingTables


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
    code_dict['PG'] = Runway()
    code_dict['PA'] = Airport()
    code_dict['PC'] = Waypoint(False)
    code_dict['PD'] = SIDSTARApp()
    code_dict['PR'] = FlightPlanning()
    code_dict['HA'] = Heliport()
    code_dict['HV'] = HeliportComms()
    code_dict['TC'] = CruisingTables()
    code_dict['AS'] = Mora()

    def __init__(self):
        self.code = ''
        self.raw_string = ''
        self.fields = []

    def read(self, line):
        if line.startswith('S' or 'T') is False:
            return False
        self.raw_string = line
        match line[4]:
            case 'D' | 'E' | 'A' | 'T':
                self.code = line[4:6]
            case 'P' | 'H':
                self.code = line[4] + line[12]
            case _:
                return False
        x = self.code_dict[self.code]
        if x is None:
            return False
        self.fields = x.read(line)
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
