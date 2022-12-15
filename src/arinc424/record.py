
from .records import airport
from .records import navaid

import arinc424.sections as sec
import json

class Record():

    def __init__(self):
        self.type = 'Unknown'
        self.raw_string = ''
        self.fields = {}
        self.continuation = False

    def dump(self):
        for k, v in self.fields.items():
            print("{:<26}: {}".format(k, v))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record, sort_keys=True, indent=4, separators=(',', ': '))

    def decode(self):
        # TODO: this
        pass

    def read(self, line):

        if line.startswith('S' or 'T') == False: # TODO: dodgy
            return

        section = sec.Section()
        section.read(line)

        match section.code[0]:

            case sec.NAVAID:
                self.fields = navaid.read_fields(section, line)

            case sec.AIRPORT:
                self.fields = airport.read_fields(section, line)

            case _:
                print("invalid section")