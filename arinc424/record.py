from .records import navaid_vhf
from .records import navaid_ndb
from .records import enroute_marker
from .records import enroute_waypoint
from .records import enroute_holding
from .records import enroute_airway
from .records import runway
from .records import heliport
from .records import heliport_comms
import json


class Record():

    field_idx = 0
    value_idx = 1
    decode_fn_idx = 2

    def __init__(self):
        self.code = ''
        self.raw_string = ''
        self.fields = []

    def read(self, line):
        if line.startswith('S' or 'T') is False:
            return False

        rec = None
        self.code += line[4]
        match self.code[0]:
            case 'D':
                self.code += line[5]
                if self.code == 'D ':
                    rec = navaid_vhf.VHFNavaid()
                elif self.code == 'DB':
                    rec = navaid_ndb.NDBNavaid()
            case 'E':
                self.code += line[5]
                if self.code == 'EA':
                    rec = enroute_waypoint.Waypoint()
                elif self.code == 'EM':
                    rec = enroute_marker.Marker()
                elif self.code == 'EP':
                    rec = enroute_holding.Holding()
                elif self.code == 'ER':
                    rec = enroute_airway.Airway()
                else:
                    # print("unsupported section code",
                    #       "'{}'".format(self.code))
                    return False
            case 'P':
                self.code += line[12]
                if self.code == 'PG':
                    rec = runway.Runway()
                else:
                    # print("unsupported section code",
                    #       "'{}'".format(self.code))
                    return False
            case 'H':
                self.code += line[12]
                if self.code == 'HA':
                    rec = heliport.Heliport()
                elif self.code == 'HV':
                    rec = heliport_comms.HeliportComms()
                else:
                    print("unsupported section code", "'{}'".format(self.code))
                    return False
            case _:
                # print("unsupported section code", "'{}'".format(self.code))
                return False

        self.fields = rec.read(line)
        return True

    def dump(self):
        for i in self.fields:
            print("{:<26}: {}".format(i[self.field_idx], i[self.value_idx]))

    def decode(self):
        for i in self.fields:
            try:
                print("{:<26}: {}".format(i[self.field_idx],
                                          i[self.decode_fn_idx]
                                          (i[self.value_idx])))
            except IndexError:
                return 1
        return 0

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record,
                              sort_keys=True,
                              indent=4,
                              separators=(',', ': '))
