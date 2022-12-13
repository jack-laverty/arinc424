import sections
import json
import decoder

class Navaid:

    record = {}
    def __init__(self):
        return

    def read(self, r, section):
        self.record["Record Type"]                  = r[0]
        self.record["Customer / Area Code"]         = r[1:4]
        self.record["Airport ICAO Identifier"]      = r[6:10]
        self.record["ICAO Code"]                    = r[10:12]
        self.record["ICAO Code (2)"]                = r[19:21]
        self.record["Cycle Date"]                   = r[128:132]
        self.record["Section Code"]                 = section.code[0]
        self.record["Subsection Code"]              = section.code[1]
        self.record["File Record No"]               = r[123:128]
        self.record["VOR Identifier"]               = r[13:17]
        self.record["Continuation Records Number"]  = r[21]

        if int(self.record["Continuation Records Number"]) < 2:
            self.record["Frequency"]                = r[22:27]
            self.record["Class"]                    = r[27:32]
            self.record["VOR Latitude"]             = r[32:41]
            self.record["VOR Longitude"]            = r[41:51]
            self.record["DME Ident"]                = r[51:55]
            self.record["DME Latitude"]             = r[55:64]
            self.record["DME Longitude"]            = r[64:74]
            self.record["Station Declination"]      = r[74:79]
            self.record["DME Elevation"]            = r[79:84]
            self.record["Figure of Merit"]          = r[84]
            self.record["ILS/DME Bias"]             = r[85:87]
            self.record["Frequency Protection"]     = r[87:90]
            self.record["Datum Code"]               = r[90:93]
            self.record["VOR Name"]                 = r[93:123]
        else:
            self.record["Application Type"]         = r[22]
            self.record["Notes"]                    = r[23:92]
            self.record["Reserved (Expansion)"]     = r[92:123]

    def dump(self, readable=True):
        if readable:
            decode = decoder.Decoder()
            print(decode.navaid_class(self.record["Class"]))
        else:
            for k, v in self.record.items():
                print("{:<26}: {}".format(k, v))

    def json(self, single_line=True):
        if single_line:
            return json.dumps(self.record)
        else:
            return json.dumps(self.record, sort_keys=True, indent=4, separators=(',', ': '))