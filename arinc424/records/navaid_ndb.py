import arinc424.decoder as decode


class NDBNavaid():

    def read_primary(self, r):
        return [
            ("Record Type",                 r[0],       decode.record),
            ("Customer / Area Code",        r[1:4],     decode.text),
            ("Section Code",                r[4:6],     decode.section),
            ("Airport ICAO Identifier",     r[6:10],    decode.text),
            ("ICAO Code",                   r[10:12],   decode.text),
            ("NDB Identifier",              r[13:17],   decode.text),
            ("ICAO Code",                   r[19:21],   decode.text),
            ("Continuation Records No",     r[21],      decode.cont),
            ("NDB Frequency",               r[22:27],   decode.freq),
            ("NDB Class Facility",          r[27:29],   decode.facility),
            ("NDB Class Power",             r[29],      decode.power),
            ("NDB Class Info",              r[30],      decode.info),
            ("NDB Class Collocation",       r[31],      decode.colloc),
            ("NDB Latitude",                r[32:41],   decode.gps),
            ("NDB Longitude",               r[41:51],   decode.gps),
            ("Magnetic Variation",          r[74:79],   decode.text),
            ("Datum Code",                  r[90:93],   decode.text),
            ("NDB Name",                    r[93:123],  decode.text),
            ("File Record No",              r[123:128], decode.text),
            ("Cycle Date",                  r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",                 r[0],       decode.record),
            ("Customer / Area Code",        r[1:4],     decode.text),
            ("Section Code",                r[4:6],     decode.section),
            ("Airport ICAO Identifier",     r[6:10],    decode.text),
            ("ICAO Code",                   r[10:12],   decode.text),
            ("NDB Identifier",              r[13:17],   decode.text),
            ("ICAO Code",                   r[19:21],   decode.text),
            ("Continuation Records No",     r[21],      decode.cont),
            ("Application Type",            r[22],      decode.app),
            ("Notes",                       r[23:92],   decode.text),
            ("Reserved (Expansion)",        r[92:123],  decode.text),
            ("File Record No",              r[123:128], decode.text),
            ("Cycle Date",                  r[128:132], decode.cycle)
        ]

    def read_sim(self, r):
        return [
            ("Record Type",                 r[0],       decode.record),
            ("Customer / Area Code",        r[1:4],     decode.text),
            ("Section Code",                r[4:6],     decode.section),
            ("Airport ICAO Identifier",     r[6:10],    decode.text),
            ("ICAO Code",                   r[10:12],   decode.text),
            ("NDB Identifier",              r[13:17],   decode.text),
            ("ICAO Code",                   r[19:21],   decode.text),
            ("Continuation Records No",     r[21],      decode.cont),
            ("Application Type",            r[22],      decode.app),
            ("Facility Characteristics",    r[27:32],   decode.text),
            ("Facility elevation",          r[79:84],   decode.text),
            ("File Record No",              r[123:128], decode.text),
            ("Cycle Date",                  r[128:132], decode.cycle),
        ]

    def read_flight_plan0(self, r):
        return [
            ("Record Type",             r[0],       decode.record),
            ("Customer / Area Code",    r[1:4],     decode.text),
            ("Section Code",            r[4:6],     decode.section),
            ("Airport ICAO Identifier", r[6:10],    decode.text),
            ("ICAO Code",               r[10:12],   decode.text),
            ("VOR Identifier",          r[13:17],   decode.text),
            ("ICAO Code (2)",           r[19:21],   decode.text),
            ("Continuation Records No", r[21],      decode.cont),
            ("Application Type",        r[22],      decode.app),
            ("FIR Identifier",          r[23:27],   decode.text),
            ("UIR Identifier",          r[28:31],   decode.text),
            ("Start/End Indicator",     r[32],      decode.text),
            ("Start/End Date",          r[32:43],   decode.text),
            ("Reserved (Expansion)",    r[43:123],  decode.text),
            ("File Record No",          r[123:128], decode.text),
            ("Cycle Date",              r[128:132], decode.cycle)
        ]

    def read_flight_plan1(self, r):
        return [
            ("Record Type",             r[0],       decode.record),
            ("Customer / Area Code",    r[1:4],     decode.text),
            ("Section Code",            r[4:6],     decode.section),
            ("Airport ICAO Identifier", r[6:10],    decode.text),
            ("ICAO Code",               r[10:12],   decode.text),
            ("NDB Identifier",          r[13:17],   decode.text),
            ("ICAO Code",               r[19:21],   decode.text),
            ("Continuation Records No", r[21],      decode.cont),
            ("NDB Frequency",           r[22:27],   decode.freq),
            ("NDB Class Facility",      r[27:29],   decode.facility),
            ("NDB Class Power",         r[29],      decode.power),
            ("NDB Class Info",          r[30],      decode.info),
            ("NDB Class Collocation",   r[31],      decode.colloc),
            ("NDB Latitude",            r[32:41],   decode.gps),
            ("NDB Longitude",           r[41:51],   decode.gps),
            ("Magnetic Variation",      r[74:79],   decode.text),
            ("Datum Code",              r[90:93],   decode.text),
            ("NDB Name",                r[93:123],  decode.text),
            ("File Record No",          r[123:128], decode.text),
            ("Cycle Date",              r[128:132], decode.cycle)
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
                    return
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
                    raise ValueError('Unknown Application Type')
