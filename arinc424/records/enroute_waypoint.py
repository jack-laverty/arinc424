import arinc424.decoder as decode


class Waypoint():

    def read_primary(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("Region Code",            r[6:10],    decode.text),
            ("ICAO Code",              r[10:12],   decode.text),
            ("Subsection Code",        r[12],      decode.text),
            ("Waypoint Identifier",    r[13:18],   decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Waypoint Type",          r[26:29],   decode.waypoint),
            ("Waypoint Usage",         r[29:31],   decode.text),
            ("Waypoint Latitude",      r[32:41],   decode.gps),
            ("Waypoint Longitude",     r[41:51],   decode.gps),
            ("Dynamic Mag. Variation", r[74:79],   decode.text),
            ("Datum Code",             r[84:87],   decode.text),
            ("Name Format Indicator",  r[95:98],   decode.nfi),
            ("Waypoint Name / Desc",   r[98:123],  decode.text),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
        ]

    def read_cont(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("Region Code",            r[6:10],    decode.text),
            ("ICAO Code",              r[10:12],   decode.text),
            ("Subsection Code",        r[12],      decode.text),
            ("Waypoint Identifier",    r[13:18],   decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Application Type",       r[22],      decode.app),
            ("Notes",                  r[23:123],  decode.text),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
        ]

    def read_flight_plan0(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("Region Code",            r[6:10],    decode.text),
            ("ICAO Code",              r[10:12],   decode.text),
            ("Subsection Code",        r[12],      decode.text),
            ("Waypoint Identifier",    r[13:18],   decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Application Type",       r[22],      decode.app),
            ("FIR Identifier",         r[23:27],   decode.text),
            ("UIR Identifier",         r[27:31],   decode.text),
            ("Start/End Indicator",    r[31],      decode.text),
            ("Start/End Date",         r[32:43],   decode.text),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
        ]

    def read_flight_plan1(self, r):
        return [
            ("Record Type",            r[0],       decode.record),
            ("Customer / Area Code",   r[1:4],     decode.text),
            ("Section Code",           r[4:6],     decode.section),
            ("Region Code",            r[6:10],    decode.text),
            ("ICAO Code",              r[10:12],   decode.text),
            ("Subsection Code",        r[12],      decode.text),
            ("Waypoint Identifier",    r[13:18],   decode.text),
            ("ICAO Code",              r[19:21],   decode.text),
            ("Continuation Record No", r[21],      decode.cont),
            ("Waypoint Type",          r[26:29],   decode.waypoint),
            ("Waypoint Usage",         r[29:31],   decode.text),
            ("Waypoint Latitude",      r[32:41],   decode.gps),
            ("Waypoint Longitude",     r[41:51],   decode.gps),
            ("Dynamic Mag. Variation", r[74:79],   decode.text),
            ("Datum Code",             r[84:87],   decode.text),
            ("Name Format Indicator",  r[95:98],   decode.nfi),
            ("Waypoint Name / Desc",   r[98:123],  decode.text),
            ("File Record No",         r[123:128], decode.text),
            ("Cycle Date",             r[128:132], decode.cycle)
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
                    return
                case _:
                    raise ValueError('Unknown Application Type')
