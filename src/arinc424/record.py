from .records import airport
from .records import navaid
import json


class Record():

    def __init__(self):
        self.code = 'Unknown'
        self.raw_string = ''
        self.fields = {}
        self.continuation = False

    def read(self, line):
        if line.startswith('S' or 'T') is False:
            return -1
        self.code += line[4]
        match self.code[0]:
            case 'D':
                self.code += line[5]
                self.fields = navaid.read_fields(self.code, line)
            case 'P':
                self.code += line[12]
                self.fields = airport.read_fields(self.code, line)
            case _:
                print("unsupported section code")
                return 0
        return 0

    def dump(self):
        for k, v in self.fields.items():
            print("{:<26}: {}".format(k, v))

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
