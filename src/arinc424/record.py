from .records import navaid_vhf
from .records import navaid_ndb
from .records import enroute_marker
from .records import enroute_waypoint
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
            return None

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
                else:
                    print("dunno section:", self.code)
            case _:
                print("unsupported section code", self.code[0])
                return None
        self.fields = rec.read(line)
        return 0

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
