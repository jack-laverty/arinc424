import arinc424.decoder as decode


class CruisingTables():

    def read_primary(self, r):
        return [
            ("Record Type",                     r[0],       decode.record),
            ("Customer / Area Code",            r[1:4],     decode.text),
            ("Section Code",                    r[4]+r[12], decode.section),
            ("Cruising Table Identifier",       r[6:8],     decode.text),
            ("Sequence Number",                 r[8],       decode.text),
            ("Course From",                     r[28:32],   decode.text),
            ("Course To",                       r[32:36],   decode.text),
            ("Mag/True",                        r[36],      decode.text),
            ("Cruise Level From",               r[39:44],   decode.cont),
            ("Vertical Separation",             r[44:49],   decode.cont),
            ("Cruise Level To",                 r[49:54],   decode.text),
            ("Cruise Level From",               r[54:59],   decode.cont),
            ("Vertical Separation",             r[59:64],   decode.cont),
            ("Cruise Level To",                 r[64:69],   decode.text),
            ("Cruise Level From",               r[69:74],   decode.cont),
            ("Vertical Separation",             r[74:79],   decode.cont),
            ("Cruise Level To",                 r[79:84],   decode.text),
            ("Cruise Level From",               r[84:89],   decode.cont),
            ("Vertical Separation",             r[89:94],   decode.cont),
            ("Cruise Level To",                 r[94:99],   decode.text),
            ("File Record No",                  r[123:128], decode.text),
            ("Cycle Date",                      r[128:132], decode.cycle),
        ]

    def read(self, line):
        return self.read_primary(line)
