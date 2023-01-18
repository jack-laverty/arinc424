import arinc424.decoder as decode


class VHFNavaid():

    def read_primary(self, r):
        return [
            ("Record Type",                 r[0],           decode.record),
            ("Customer / Area Code",        r[1:4],         decode.text),
            ("Section Code",                r[4:6],         decode.section),
            ("Airport ICAO Identifier",     r[6:10],        decode.text),
            ("ICAO Code",                   r[10:12],       decode.text),
            ("VOR Identifier",              r[13:17],       decode.text),
            ("ICAO Code (2)",               r[19:21],       decode.text),
            ("Continuation Records No",     r[21],          decode.cont),
            ("Frequency",                   r[22:27],       decode.freq),
            ("Class Facility",              r[27:29],       decode.facility),
            ("Class Power",                 r[29],          decode.power),
            ("Class Info",                  r[30],          decode.info),
            ("Class Collocation",           r[31],          decode.colloc),
            ("VOR Latitude",                r[32:41],       decode.gps),
            ("VOR Longitude",               r[41:51],       decode.gps),
            ("DME Ident",                   r[51:55],       decode.text),
            ("DME Latitude",                r[55:64],       decode.gps),
            ("DME Longitude",               r[64:74],       decode.gps),
            ("Station Declination",         r[74:79],       decode.text),
            ("DME Elevation",               r[79:84],       decode.dme_el),
            ("Figure of Merit",             r[84],          decode.text),
            ("ILS/DME Bias",                r[85:87],       decode.text),
            ("Frequency Protection",        r[87:90],       decode.freq),
            ("Datum Code",                  r[90:93],       decode.text),
            ("VOR Name",                    r[93:123],      decode.text),
            ("File Record No",              r[123:128],     decode.text),
            ("Cycle Date",                  r[128:132],     decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                 r[0],           decode.record),
            ("Customer / Area Code",        r[1:4],         decode.text),
            ("Section Code",                r[4:6],         decode.section),
            ("Airport ICAO Identifier",     r[6:10],        decode.text),
            ("ICAO Code",                   r[10:12],       decode.text),
            ("VOR Identifier",              r[13:17],       decode.text),
            ("ICAO Code (2)",               r[19:21],       decode.text),
            ("Continuation Records No",     r[21],          decode.cont),
            ("Application Type",            r[22],          decode.app),
            ("Notes",                       r[23:92],       decode.text),
            ("Reserved (Expansion)",        r[92:123],      decode.text),
            ("File Record No",              r[123:128],     decode.text),
            ("Cycle Date",                  r[128:132],     decode.cycle),
        ]

    def read_sim(self, r):
        return [
            ("Record Type",                 r[0],          decode.record),
            ("Customer / Area Code",        r[1:4],        decode.text),
            ("Section Code",                r[4:6],        decode.section),
            ("Airport ICAO Identifier",     r[6:10],       decode.text),
            ("ICAO Code",                   r[10:12],      decode.text),
            ("VOR Identifier",              r[13:17],      decode.text),
            ("ICAO Code (2)",               r[19:21],      decode.text),
            ("Continuation Records No",     r[21],         decode.cont),
            ("Application Type",            r[22],         decode.app),
            ("Facility Characteristics",    r[27:32],      decode.text),
            ("Reserved (Spacing)",          r[32:74],      decode.text),
            ("File Record No",              r[123:128],    decode.text),
            ("Cycle Date",                  r[128:132],    decode.cycle)
        ]

    def read_flight_plan0(self, r):
        return [
            ("Record Type",                 r[0],           decode.record),
            ("Customer / Area Code",        r[1:4],         decode.text),
            ("Section Code",                r[4:6],         decode.section),
            ("Airport ICAO Identifier",     r[6:10],        decode.text),
            ("ICAO Code",                   r[10:12],       decode.text),
            ("VOR Identifier",              r[13:17],       decode.text),
            ("ICAO Code (2)",               r[19:21],       decode.text),
            ("Continuation Records No",     r[21],          decode.cont),
            ("Application Type",            r[22],          decode.app),
            ("FIR Identifier",              r[23:27],       decode.text),
            ("UIR Identifier",              r[28:31],       decode.text),
            ("Start/End Indicator",         r[32],          decode.text),
            ("Start/End Date",              r[32:43],       decode.text),
            ("Reserved (Expansion)",        r[43:123],      decode.text),
            ("File Record No",              r[123:128],     decode.text),
            ("Cycle Date",                  r[128:132],     decode.cycle)
        ]

    def read_flight_plan1(self, r):
        return [
            ("Record Type",                 r[0],           decode.record),
            ("Customer / Area Code",        r[1:4],         decode.text),
            ("Section Code",                r[4:6],         decode.section),
            ("Airport ICAO Identifier",     r[6:10],        decode.text),
            ("ICAO Code",                   r[10:12],       decode.text),
            ("VOR Identifier",              r[13:17],       decode.text),
            ("ICAO Code (2)",               r[19:21],       decode.text),
            ("Continuation Records No",     r[21],          decode.cont),
            ("Application Type",            r[22],          decode.app),
            ("Frequency",                   r[22:27],       decode.text),
            ("Class",                       r[27:32],       decode.text),
            ("VOR Latitude",                r[32:41],       decode.text),
            ("VOR Longitude",               r[41:51],       decode.text),
            ("DME Ident",                   r[51:55],       decode.text),
            ("DME Latitude",                r[55:64],       decode.text),
            ("DME Longitude",               r[64:74],       decode.text),
            ("Station Declination",         r[74:79],       decode.text),
            ("DME Elevation",               r[79:84],       decode.text),
            ("Figure of Merit",             r[84],          decode.text),
            ("ILS/DME Bias",                r[85:87],       decode.text),
            ("Frequency Protection",        r[87:90],       decode.text),
            ("Datum Code",                  r[90:93],       decode.text),
            ("VOR Name",                    r[93:123],      decode.text),
            ("File Record No",              r[123:128],     decode.text),
            ("Cycle Date",                  r[128:132],     decode.cycle)
        ]

    def read_lim(self, r):
        return [
            ("Record Type",                 r[0],           decode.record),
            ("Customer / Area Code",        r[1:4],         decode.text),
            ("Section Code",                r[4:6],         decode.section),
            ("Airport ICAO Identifier",     r[6:10],        decode.text),
            ("ICAO Code",                   r[10:12],       decode.text),
            ("VOR Identifier",              r[13:17],       decode.text),
            ("ICAO Code (2)",               r[19:21],       decode.text),
            ("Continuation Records No",     r[21],          decode.cont),
            ("Application Type",            r[22],          decode.app),
            ("Navaid Limitation Code",      r[23],          decode.text),
            ("Component Affected Indicator", r[24],         decode.text),
            ("Sequence Number",             r[25:27],       decode.text),
            ("Sector From/Sector To",       r[27:29],       decode.text),
            ("Distance Description",        r[29],          decode.text),
            ("Distance Limiation",          r[30:36],       decode.text),
            ("Altitude Description",        r[36],          decode.text),
            ("Altitude Limiation",          r[37:43],       decode.text),
            ("Sector From/Sector To",       r[43:45],       decode.text),
            ("Distance Description",        r[45],          decode.text),
            ("Distance Limiation",          r[46:52],       decode.text),
            ("Altitude Description",        r[52],          decode.text),
            ("Altitude Limiation",          r[53:59],       decode.text),
            ("Sector From/Sector To",       r[59:61],       decode.text),
            ("Distance Description",        r[61],          decode.text),
            ("Distance Limiation",          r[62:68],       decode.text),
            ("Altitude Description",        r[68],          decode.text),
            ("Altitude Limiation",          r[69:75],       decode.text),
            ("Sector From/Sector To",       r[75:77],       decode.text),
            ("Distance Description",        r[77],          decode.text),
            ("Distance Limiation",          r[79:84],       decode.text),
            ("Altitude Description",        r[84],          decode.text),
            ("Altitude Limiation",          r[85:91],       decode.text),
            ("Sector From/Sector To",       r[91:93],       decode.text),
            ("Distance Description",        r[93],          decode.text),
            ("Distance Limiation",          r[94:100],      decode.text),
            ("Altitude Description",        r[101],         decode.text),
            ("Altitude Limiation",          r[101:107],     decode.text),
            ("Sequence End Indicator",      r[107],         decode.text),
            ("Blank (Spacing)",             r[108:123],     decode.text),
            ("File Record No",              r[123:128],     decode.text),
            ("Cycle Date",                  r[128:132],     decode.cycle),
        ]

    def read(self, line):
        if int(line[21]) < 2:
            # continuation record # 0 = primary record with no continuation
            # continuation record # 1 = primary record with continuation
            return self.read_primary(line)
        else:
            match line[22]:
                case 'A':
                    return self.read_cont(line)
                case 'C':
                    return
                case 'E':
                    return
                case 'L':
                    return self.lim(line)
                case 'N':
                    return
                case 'T':
                    return
                case 'U':
                    return
                case 'V':
                    return
                case 'P':
                    return self.read_flight_plan0(line)
                case 'Q':
                    return self.read_flight_plan1(line)
                case 'S':
                    return self.read_sim(line)
                case _:
                    # raise ValueError('Unknown Application Type')
                    return
