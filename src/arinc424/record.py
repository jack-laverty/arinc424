from .records import airport
from .records import navaid
import json


class Record():

    def __init__(self):
        self.code = ''
        self.raw_string = ''
        self.fields = []

    def read(self, line):
        if line.startswith('S' or 'T') is False:
            print("no record found")
            return 0

        self.code += line[4]
        match self.code[0]:
            case 'D':
                vhf = navaid.VHFNavaid()
                self.code += line[5]
                if self.code == 'D ':
                    self.fields = vhf.read(line)
                    self.dump()
                # elif self.code == 'DB':
                #     ndb = navaid.NDBNavaid()
                #     print(ndb.find_type(line)
            case 'P':
                self.code += line[12]
                self.fields = airport.read_fields(self.code, line)
            case _:
                print("unsupported section code", self.code[0])
                return 0
        return 0

    def dump(self):
        for i in self.fields:
            print("{:<26}: {}".format(i[0], i[1]))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record,
                              sort_keys=True,
                              indent=4,
                              separators=(',', ': '))

    def decode(self):
        # TODO: the actual useful thing that this software needs to do
        # for k, v in self.fields.items():
        #     print("{:<26}: {}".format(k, decode(v, v.data_type)))
        pass
