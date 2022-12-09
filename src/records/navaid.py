from collections import defaultdict
import sections
import json

class Navaid:

    record = {}
    def __init__(self):
        return

    def parse_class(self, data):
        def def_value():
            return "<UNKNOWN>"
        facility = defaultdict(def_value)
        power = defaultdict(def_value)
        info = defaultdict(def_value)
        collocation = defaultdict(def_value)
        facility['V'] = 'VOR'
        facility[' '] = ''
        facility['D'] = 'DME'
        facility['T'] = 'TACAN'
        facility['M'] = 'MIL TACAN'
        facility['I'] = 'ILS/DME or ILS/TACAN'
        facility['N'] = 'MLS/DME/N'
        facility['P'] = 'MLS/DME/P'
        power['T'] = 'Terminal'
        power['L'] = 'Low Altitude'
        power['H'] = 'High Altitude'
        power['U'] = 'Undefined'
        power['C'] = 'ILS/TACAN'
        info['D'] = 'Biased ILS/DME or ILS/TACAN'
        info['A'] = 'Automatic Transcribed Weather Broadcast'
        info['B'] = 'Scheduled Weather Broadcast'
        info['W'] = 'No Voice on Frequency'
        info[' '] = 'Voice on Frequency'
        collocation[' '] = 'Collocated Navaids'
        collocation['N'] = 'Non-Collocated Navaids'

        self.record["Navaid Class"] = {
                "Facility":     facility[data[0]] + facility[data[1]],
                "Power":        power[data[2]],
                "Info":         info[data[3]],
                "Collocation":  collocation[data[4]],
        }

    def parse_freq(self, data):
        self.record["VOR Frequency"] = float(data)/100

    def parse_continuation(self, data):
        self.record["Continuation Record No"] = int(data)
        return int(data)

    def parse_record_type(self, data):
        if data == 'S':
            self.record["Record Type"] = 'Standard'
        elif data == 'T':
            self.record["Record Type"] = 'Tailored'
    
    def parse_cycle_date(self, data):
        self.record["Navaid Class"] = {
            "Revision Year": int("20" + data[:2]),
            "Release Cycle": int(data[2:]),
        }

    def parse_dme_elevation(self, data):
        self.record["DME Elevation"] = data.lstrip('0') + " ft"

    def parse_dme_lat(self, data):
        x = len(data)
        self.record["DME Latitude"] = ' '.join([data[1:x-6], data[x-6:x-4], data[x-4:x-2], data[x-2:x], data[0]])

    def parse_dme_long(self, data):
        x = len(data)
        self.record["DME Longitude"] = ' '.join([data[1:x-6], data[x-6:x-4], data[x-4:x-2], data[x-2:x], data[0]])

    def parse_record(self, r):
        self.parse_record_type(r[0])
        self.parse_cycle_date(r[128:132])
        if self.parse_continuation(r[21]) < 2:
            self.record["Customer / Area Code"]    = r[1:4]
            self.record["Section Code"]            = r[4]
            self.record["Subsection Code"]         = r[5]
            self.record["Airport ICAO Identifier"] = r[6:10]
            self.record["ICAO Code"]               = r[10:12]
            self.record["VOR Identifier"]          = r[13:17]
            self.record["ICAO Code"]               = r[19:21]
            self.parse_freq(r[22:27])
            self.parse_class(r[27:32])
            self.record["VOR Latitude"]            = r[32:41]
            self.record["VOR Longitude"]           = r[41:51]
            self.record["DME Ident"]               = r[51:55]
            self.parse_dme_lat(r[55:64])
            self.parse_dme_long(r[64:74])
            self.record["Station Declination"]     = r[74:79]
            self.parse_dme_elevation(r[79:84])
            self.record["Figure of Merit"]         = r[84]
            self.record["ILS/DME Bias"]            = r[85:87]
            self.record["Frequency Protection"]    = r[87:90]
            self.record["Datum Code"]              = r[90:93]
            self.record["VOR Name"]                = r[93:123]
            self.record["File Record No"]         = r[123:128]
        else:
            self.record["Customer / Area Code"]    = r[1:4]
            self.record["Section Code"]            = r[4]
            self.record["Subsection Code"]         = r[5]
            self.record["Airport ICAO Identifier"] = r[6:10]
            self.record["ICAO Code"]               = r[10:12]
            self.record["VOR Identifier"]          = r[13:17]
            self.record["ICAO Code"]               = r[19:21]
            self.record["Application Type"]        = r[22]
            self.record["Notes"]                   = r[23:92]
            self.record["Reserved (Expansion)"]    = r[92:123]
            self.record["File Record No"]         = r[123:128]

    def dump(self):
        for k, v in self.record.items():
            print("{:<26}: {}".format(k, v))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record, sort_keys=True, indent=4, separators=(',', ': '))