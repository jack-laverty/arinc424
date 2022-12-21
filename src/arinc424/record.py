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
                self.code += line[5]
                if self.code == 'D ':
                    vhf = navaid.VHFNavaid()
                    self.fields = vhf.read(line)
                    # self.dump()
                    self.decode()
                # elif self.code == 'DB':
                #     ndb = navaid.NDBNavaid()
                #     print(ndb.find_type(line)
            case _:
                print("unsupported section code", self.code[0])
                return 0
        return 0

    def dump(self):
        for i in self.fields:
            print("{:<26}: {}".format(i[0], i[1]))

    def decode(self):
        for i in self.fields:
            print("{:<26}: {}".format(i[0], i[2](i[1])))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record,
                              sort_keys=True,
                              indent=4,
                              separators=(',', ': '))
