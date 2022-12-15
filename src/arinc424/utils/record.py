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