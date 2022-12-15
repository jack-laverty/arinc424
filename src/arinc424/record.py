
from .records import airport
from .records import navaid

import arinc424.sections as sections
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
        for k, v in self.fields.items():
            print("{:<26}: {}".format(k, v))

    def read(self, line):
        if line.startswith('S' or 'T') == False:
            return None
        section = sections.Section()
        section.read(line)
        if section.is_navaid():
            self.fields = navaid.read_fields(section, line)
        elif section.is_airport():
            self.fields = airport.read_fields(section, line)